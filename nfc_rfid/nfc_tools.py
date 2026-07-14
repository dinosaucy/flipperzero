#!/usr/bin/env python3
"""
NFC/RFID helper: reads card info and triggers emulation on Flipper via CLI.
Requires: pip install pyserial

Usage:
    python nfc_tools.py read
    python nfc_tools.py emulate samples/mifare_classic.nfc
"""
import serial
import time
import sys

PORT = "/dev/ttyACM0"
BAUD = 115200


def send_cmd(ser, cmd, wait=0.5):
    ser.write((cmd + "\r\n").encode())
    time.sleep(wait)
    return ser.read_all().decode(errors="ignore")


def read_card():
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        print(send_cmd(ser, "nfc detect", wait=1.0))


def emulate(nfc_file):
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        remote = f"/ext/nfc/{nfc_file.split('/')[-1]}"
        print(send_cmd(ser, f"nfc emulate {remote}", wait=1.0))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: nfc_tools.py [read|emulate] [file]")
        sys.exit(1)

    action = sys.argv[1]
    if action == "read":
        read_card()
    elif action == "emulate":
        if len(sys.argv) < 3:
            print("Provide a .nfc filename to emulate")
            sys.exit(1)
        emulate(sys.argv[2])
    else:
        print(f"Unknown action: {action}") 

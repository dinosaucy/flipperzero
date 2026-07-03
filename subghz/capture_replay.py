#!/usr/bin/env python3
"""
Sub-GHz capture/replay helper via Flipper CLI (serial).
Requires: pip install pyserial

Usage:
    python capture_replay.py read
    python capture_replay.py replay samples/example.sub
"""
import serial
import time
import sys

PORT = "/dev/ttyACM0"  # Windows: e.g. COM5
BAUD = 115200


def send_cmd(ser, cmd, wait=0.5):
    ser.write((cmd + "\r\n").encode())
    time.sleep(wait)
    return ser.read_all().decode(errors="ignore")


def read_status():
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        print(send_cmd(ser, "subghz chat", wait=0.3))


def list_files():
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        print(send_cmd(ser, "storage list /ext/subghz"))


def replay(filepath):
    """Transmit a .sub file already present on the Flipper's SD card."""
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        remote_path = f"/ext/subghz/{filepath.split('/')[-1]}"
        print(send_cmd(ser, f"subghz tx {remote_path}", wait=1.0))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: capture_replay.py [read|list|replay] [file]")
        sys.exit(1)

    action = sys.argv[1]
    if action == "read":
        read_status()
    elif action == "list":
        list_files()
    elif action == "replay":
        if len(sys.argv) < 3:
            print("Provide a .sub filename to replay")
            sys.exit(1)
        replay(sys.argv[2])
    else:
        print(f"Unknown action: {action}")

# Flipper Zero

A curated, practical reference of Command-Line Interface (CLI) commands for the [Flipper Zero](https://flipperzero.one/) multi-tool device. Built for pentesters, hardware hackers, IT/security students, and everyday Flipper Zero owners who want a fast, no-fluff command lookup instead of digging through the official docs every time.

> ⚠️ **Disclaimer:** This repository is for educational and authorized security-testing purposes only. Only use these commands on devices, networks, and signals you own or have explicit permission to test. Misuse of RFID, NFC, Sub-GHz, or BadUSB features may be illegal in your jurisdiction.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Connecting to the CLI](#connecting-to-the-cli)
- [Command Reference](#command-reference)
  - [System & Device](#system--device)
  - [Storage (SD Card)](#storage-sd-card)
  - [Sub-GHz](#sub-ghz)
  - [NFC](#nfc)
  - [RFID (125 kHz)](#rfid-125-khz)
  - [Infrared (IR)](#infrared-ir)
  - [iButton](#ibutton)
  - [GPIO](#gpio)
  - [Bluetooth (BLE)](#bluetooth-ble)
  - [Power & Logging](#power--logging)
  - [Fun Extras](#fun-extras)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

This repo assumes you have:

1. A Flipper Zero running official or a compatible custom firmware.
2. A USB-C cable to connect it to your computer.
3. A terminal (macOS/Linux: `screen` or `minicom`; Windows: `PuTTY`) or the browser-based [Flipper Lab](https://lab.flipper.net/) / [Web Serial Terminal](https://googlechromelabs.github.io/serial-terminal/).

All commands below are typed directly into the Flipper Zero CLI shell after connecting.

## Connecting to the CLI

**macOS / Linux**
```bash
ls /dev/cu.*                     # find your device (macOS)
screen /dev/cu.usbmodemflip_XXXX # connect
# exit: Ctrl+A, then K, then Y
```

**Windows**
1. Open Device Manager → Ports (COM & LPT) → note the COM number.
2. Open PuTTY → Connection type: Serial → Serial line: `COMx` → Speed: `230400` → Open.

Once connected, type `help` or `?` to list all available commands live on your device.

---

## Command Reference

### System & Device

| Command | Description |
|---|---|
| `help` / `?` | List all available CLI commands |
| `info device` / `!` | Show detailed device information |
| `info power` | Show power/battery system info |
| `date` | Display or set current date and time |
| `free` | Show heap memory allocator info |
| `free blocks` | Show heap fragmentation / free block sizes |
| `top` | Live view of running threads (like Linux `top`, Ctrl+C to quit) |
| `uptime` | Time since last reboot |
| `neofetch` | Fun system info banner, like Linux `neofetch` |
| `factory_reset` | Reset device to factory settings (SD card data kept) |
| `sysctl debug <0/1>` | Enable/disable system debug mode |

### Storage (SD Card)

| Command | Description |
|---|---|
| `storage info /ext` | Get filesystem info for the SD card |
| `storage list /ext` | List files/directories at a path |
| `storage tree /ext` | Recursively list all files and folders |
| `storage read /ext/path/file.txt` | Print file contents |
| `storage write /ext/path/file.txt` | Write text to a file (Ctrl+C to stop) |
| `storage copy <src> <dst>` | Copy a file |
| `storage rename <old> <new>` | Rename/move a file or directory |
| `storage remove /ext/path` | Delete a file or empty directory |
| `storage mkdir /ext/newfolder` | Create a new directory |
| `storage md5 /ext/path/file` | Show MD5 hash of a file |
| `storage stat /ext/path/file` | Show file/folder metadata |
| `storage format /ext` | ⚠️ Format the SD card (destructive) |

### Sub-GHz

| Command | Description |
|---|---|
| `subghz chat <freq_hz> <0/1>` | Chat with nearby Flipper Zero users over Sub-GHz radio |
| `subghz rx <freq_hz> <0/1>` | Listen for a Sub-GHz signal |
| `subghz rx raw <freq_hz>` | Receive a signal in raw format |
| `subghz tx <key_hex> <freq_hz> <te_us> <repeat> <0/1>` | Transmit a key |
| `subghz tx from file <path> <repeat> <0/1>` | Transmit a saved signal file |
| `subghz decode raw <path>` | Decode a raw signal file |

> Valid frequency ranges (Hz): `299999755–348000000`, `386999938–464000000`, `778999847–928000000`. Some frequencies are region-restricted — check [Flipper's frequency guide](https://docs.flipper.net/zero/sub-ghz/frequencies) first.

### NFC

| Command | Description |
|---|---|
| `nfc` | Enter the NFC sub-shell (`help` inside for more, `exit` to leave) |
| `dump f <path>` | Dump physical card data to a `.nfc` file |
| `emulate f <path>` | Emulate a saved NFC card file |
| `scanner` | Detect and list all protocols supported by a tag |
| `mfu info` | Basic info about a Mifare Ultralight tag |
| `mfu rdbl b <block>` | Read a specific data block |
| `mfu wrbl b <block> d <data>` | Write data to a specific block |
| `raw p <protocol> d <data>` | Send raw bytes using a chosen protocol |

### RFID (125 kHz)

| Command | Description |
|---|---|
| `rfid read` | Read a low-frequency RFID card (ASK/PSK) |
| `rfid emulate <type> <data>` | Emulate an RFID card |
| `rfid write <type> <data>` | Write data to a writable RFID tag |
| `rfid raw read <ask/psk> <file>` | Save raw card data to a file |
| `rfid raw emulate <file>` | Emulate raw data from a saved file |
| `rfid raw analyze <file>` | Analyze/decode raw data from a file |

### Infrared (IR)

| Command | Description |
|---|---|
| `ir rx` | Read and decode an incoming IR signal |
| `ir rx raw` | Read raw IR data |
| `ir tx <protocol> <address> <command>` | Send an IR command |
| `ir tx raw F <freq> DC <duty> <samples>` | Send raw IR data |
| `ir universal list <remote>` | List commands for a universal remote (tv, audio, ac, projector) |
| `ir universal <remote> <signal>` | Send a universal remote command |

### iButton

| Command | Description |
|---|---|
| `ikey read` | Read an iButton key |
| `ikey emulate <type> <data>` | Emulate an iButton key |
| `ikey write dallas <data>` | Write data to a Dallas iButton key |

### GPIO

| Command | Description |
|---|---|
| `gpio mode <pin> <0/1>` | Set pin to input (0) or output (1) |
| `gpio set <pin> <0/1>` | Set output pin value |
| `gpio read <pin>` | Read a pin's current value |

Valid pins: `PA7, PA6, PA4, PB3, PB2, PC3, PC1, PC0`

### Bluetooth (BLE)

| Command | Description |
|---|---|
| `bt` | Radio core (BLE) factory test tool |
| `bt hci_info` | Display Bluetooth HCI version info |

### Power & Logging

| Command | Description |
|---|---|
| `power off` | Power off the device |
| `power reboot` | Reboot the device |
| `power reboot2dfu` | Reboot into DFU (firmware update) mode |
| `log` | Start logging at the current level |
| `log debug` / `log trace` | Verbose logging levels (impacts performance) |
| `update install <path.fuf>` | Install a firmware update package |
| `update backup <path.tar>` | Back up internal storage |
| `update restore <path.tar>` | Restore internal storage from backup |

### Fun Extras

| Command | Description |
|---|---|
| `vibro <1/0>` | Turn the vibration motor on/off |
| `led r/g/b <0-255>` | Set status LED color components |
| `led bl <0-255>` | Set backlight brightness |
| `buzzer note <note> <duration>` | Play a musical note, e.g. `buzzer note cs3 500ms` |
| `buzzer freq <hz> <duration>` | Play a tone at a specific frequency |

---

## Contributing

Found a useful command that's missing, or want to add a script/shortcut? Pull requests are welcome:

1. Fork the repo.
2. Add your command(s) to the relevant table (or create a new section if needed).
3. Open a pull request with a short description of what it does and why it's useful.

## License

MIT — use freely, contribute back if you can.

## Credits

Command reference compiled from the [official Flipper Zero documentation](https://docs.flipper.net/zero/development/cli) and the Flipper community forum.

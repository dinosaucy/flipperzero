# flipperzero

A collection of useful tools, scripts, and custom apps for the Flipper Zero.

> ⚠️ **Use responsibly.** Sub-GHz replay, NFC/RFID cloning, and BadUSB payloads should only
> be used on devices, cards, and computers you own or are explicitly authorized to test.
> Unauthorized use may be illegal in your jurisdiction.

## Structure

```
flipperzero/
├── subghz/          Sub-GHz signal capture & replay (CLI helper + .sub samples)
├── nfc_rfid/         NFC/RFID clone & emulate tools (CLI helper + .nfc samples)
├── infrared/         IR universal remote scripts & .ir file builder
├── fap_apps/          Custom FAP applications (C, built with ufbt)
├── badusb/            BadUSB ducky-script payloads
└── scripts/           Shared Python requirements
```

## Prerequisites

- A Flipper Zero with qFlipper drivers installed
- Python 3.8+
- `pip install -r scripts/requirements.txt`
- [ufbt](https://github.com/flipperdevices/flipperzero-ufbt) for FAP development: `pip install ufbt`

## 1. Sub-GHz (`subghz/`)

`capture_replay.py` talks to the Flipper over its serial CLI to list and transmit `.sub` files.

```bash
python subghz/capture_replay.py list
python subghz/capture_replay.py replay subghz/samples/example_princeton.sub
```

Note: actual RF capture is driven from the Flipper's own Sub-GHz app UI; this script
helps automate transmission and file management of captures you've already made.

## 2. NFC / RFID (`nfc_rfid/`)

```bash
python nfc_rfid/nfc_tools.py read
python nfc_rfid/nfc_tools.py emulate nfc_rfid/samples/mifare_classic.nfc
```

## 3. Infrared (`infrared/`)

Generate `.ir` files programmatically:

```bash
cd infrared
python ir_builder.py
```

Or use the ready-made universal remote sample at `infrared/samples/tv_universal.ir`
— copy it to `/ext/infrared/` on your Flipper's SD card.

## 4. Custom FAP apps (`fap_apps/`)

Example "Hello FAP" app demonstrating GUI + input handling.

```bash
cd fap_apps/hello_fap
ufbt              # builds the .fap
ufbt launch       # flashes and runs it on a connected Flipper
```

## 5. BadUSB (`badusb/payloads/`)

Ducky-script style payloads. Copy `.txt` files to `/ext/badusb/` on the Flipper's SD card,
then run them from the BadUSB app.

- `open_notepad_demo.txt` — harmless demo, opens Notepad and types text
- `wifi_profile_export.txt` — exports saved Wi-Fi profiles on Windows (your own machine only)

## Uploading files to the Flipper

Easiest via qFlipper's file manager, or via CLI:

```bash
# from the Flipper CLI (screen /dev/ttyACM0 115200, or use qFlipper's terminal)
storage list /ext
```

Drag-and-drop through qFlipper is the simplest route for `.sub`, `.nfc`, `.ir`, and
BadUSB `.txt` files — just drop them into the matching folder on the SD card.

## Contributing

PRs welcome for new signal samples, IR device libraries, or additional FAP examples.

## License

MIT — see [LICENSE](LICENSE).
Flipperzero project. 
7929e5157079276957f3545d8d2c797072d1253e

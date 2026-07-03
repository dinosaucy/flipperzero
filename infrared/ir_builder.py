#!/usr/bin/env python3
"""
Build Flipper .ir files from NEC-protocol codes.

Usage:
    python ir_builder.py
"""


def build_nec_ir_file(entries, filename):
    """
    entries: list of dicts like
        {"name": "Power", "address": "07 00 00 00", "command": "02 00 00 00"}
    """
    lines = ["Filetype: IR signals file", "Version: 1"]
    for e in entries:
        lines.append("#")
        lines.append(f"name: {e['name']}")
        lines.append("type: parsed")
        lines.append("protocol: NEC")
        lines.append(f"address: {e['address']}")
        lines.append(f"command: {e['command']}")

    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {filename}")


if __name__ == "__main__":
    samsung_tv = [
        {"name": "Power", "address": "07 00 00 00", "command": "02 00 00 00"},
        {"name": "Vol_Up", "address": "07 00 00 00", "command": "07 00 00 00"},
        {"name": "Vol_Down", "address": "07 00 00 00", "command": "0B 00 00 00"},
    ]
    build_nec_ir_file(samsung_tv, "samples/samsung_tv_generated.ir")

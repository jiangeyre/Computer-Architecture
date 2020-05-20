#!/usr/bin/env python3

"""Main."""

import sys
from cpu import CPU

if len(sys.argv) != 2:
    print("Usage: simple.py filename", file=sys.stderr)
    sys.exit(1)

cpu = CPU()

cpu.load()
cpu.run()
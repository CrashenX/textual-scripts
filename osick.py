#!/usr/bin/env python
import sys

team = ["lone-rager",
        "hurricanerix",
        "JayF",
        "jroll",
        "mariojv",
        "Nadeem",
        "rosmaita",
        ]

try:
    text = " ".join(sys.argv[2:])
except IndexError:
    text = ""

print("%s: %s" % (" ".join(team), text))

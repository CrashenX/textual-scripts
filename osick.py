#!/usr/bin/env python
import sys

team = ["andymccr",
        "lone-rager",
        "hurricanerix",
        "JayF",
        "jimbaker",
        "jroll",
        "mariojv",
        "rosmaita",
        "thomasem",
        ]

try:
    text = " ".join(sys.argv[2:])
except IndexError:
    text = ""

print("%s: %s" % (" ".join(team), text))

#!/usr/bin/env python
import sys

team = ["aline",
        "morgabra",
        "clif_h",
        "ChrisMead",
        "JayF",
        "jroll",
        "mariojv",
        "Madasi",
        "mkam",
        "nater",
        ]

try:
    text = " ".join(sys.argv[2:])
except IndexError:
    text = ""

print("%s: %s" % (" ".join(team), text))

#! /usr/bin/env python3

import sys

VERTICAL_EDGE = "│"
HORIZONTAL_EDGE = "─"
LT_CORNER = "╭"
RT_CORNER = "┐"
LB_CORNER = "└"
RB_CORNER = "╯"


def extend_to(line, to_length):
    length = len(line)
    total_pad = to_length + 4 - length
    left_pad = total_pad // 2
    return (
        VERTICAL_EDGE
        + " " * left_pad
        + line
        + " " * (total_pad - left_pad)
        + VERTICAL_EDGE
    )


lines = [line.strip() for line in sys.stdin.readlines()]
popy = max(map(len, lines))

text = "\n".join(map(lambda x: extend_to(x, popy), lines)) + "\n"

boxes = LT_CORNER + HORIZONTAL_EDGE * (popy + 4) + RT_CORNER + "\n"
boxes += VERTICAL_EDGE + " " * (popy + 4) + VERTICAL_EDGE + "\n"
boxes += text
boxes += VERTICAL_EDGE + " " * (popy + 4) + VERTICAL_EDGE + "\n"
boxes += LB_CORNER + HORIZONTAL_EDGE * (popy + 4) + RB_CORNER

print(boxes)

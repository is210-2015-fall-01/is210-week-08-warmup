#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week8 warmup task_4."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

# You code goes here
MYLENGTH = len(MYINPUT)
if MYLENGTH > MAX_LENGTH:
    LONGSTR = 'long'


OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT

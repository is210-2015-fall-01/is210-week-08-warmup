#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""


MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

RESULT = len(MYINPUT)
if RESULT < MAX_LENGTH:
    print LONGSTR
else:
    LONGSTR = 'long'


OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT

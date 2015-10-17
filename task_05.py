#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A useful docstring."""


INPUT = raw_input('What is your systolic blood pressure? ')
OUTPUT = 'Your status is currently {}!'
SYSBP = int(INPUT)

if SYSBP <= 89:
    BP_STATUS = 'Low'
elif SYSBP >= 90 and SYSBP <= 119:
    BP_STATUS = 'Ideal'
elif SYSBP >= 120 and SYSBP <= 139:
    BP_STATUS = 'Warning'
elif SYSBP >= 140 and SYSBP <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print OUTPUT.format(BP_STATUS)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for warm up task week 8"""


MY_INPUT = int(raw_input('What is your blood pressure? '))

if MY_INPUT <= 89:
    BP_STATUS = 'Low'

elif MY_INPUT >= 90 and MY_INPUT <= 119:
    BP_STATUS = 'Ideal'

elif MY_INPUT >= 120 and MY_INPUT <= 139:
    BP_STATUS = 'Warning!'

elif MY_INPUT >= 140 and MY_INPUT <= 159:
    BP_STATUS = 'High'

else:
    BP_STATUS = 'Emergency'

BP_RESULT = 'Your status is currently: {}'.format(BP_STATUS)

print BP_RESULT

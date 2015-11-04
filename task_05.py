#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Numeric pressure is converted to descriptive term."""


BP_NUMBER = int(raw_input('What is your blood pressure? '))

if BP_NUMBER < 89:
    BP_STATUS = 'Low'
elif 90 <= BP_NUMBER <= 119:
    BP_STATUS = 'Ideal'
elif 120 <= BP_NUMBER <= 139:
    BP_STATUS = 'Warning'
elif 140 <= BP_NUMBER <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {}'.format(BP_STATUS)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is all about blood pressure readings."""

MY_BP = int(raw_input('What is your blood pressure? '))

if MY_BP <= 89:
    BP_STATUS = 'Low'
elif 90 <= MY_BP <= 119:
    BP_STATUS = 'Ideal'
elif 120 <= MY_BP <= 139:
    BP_STATUS = 'Warning'
elif 140 <= MY_BP <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print 'Your status is currently: {}'.format(BP_STATUS)

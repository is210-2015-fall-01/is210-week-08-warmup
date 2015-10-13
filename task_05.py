#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 5 BP."""

BLOODP = raw_input('What is your blood pressure reading? ')

BLOODP = int(BLOODP)

if BLOODP <= 89:
    BP_STATUS = 'Low.'

elif BLOODP <= 119:
    BP_STATUS = 'Ideal.'

elif BLOODP <= 139:
    BP_STATUS = 'Warning!'

elif BLOODP <= 159:
    BP_STATUS = 'High!'

else:
    BP_STATUS = 'Emergency!'

print 'Your status is currently: {}'.format(BP_STATUS)

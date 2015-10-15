#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 5 BP."""

BLOODP = raw_input('What is your blood pressure reading?')

BLOODP = int(BLOODP)

if BLOODP <= 89:
    BP_STATUS = 'Low.'

elif BLOODP >= 90 and BLOODP <= 119:
    BP_STATUS = 'Ideal.'

elif BLOODP >= 120 and BLOODP <= 139:
    BP_STATUS = 'Warning!'

elif BLOODP >= 140 and BLOODP <= 159:
    BP_STATUS = 'High!'

else:
    BP_STATUS = 'Emergency!'

BPRESULT = 'Your status is currently: {}'.format(BP_STATUS)

print BPRESULT

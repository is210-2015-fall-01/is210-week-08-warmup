#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A comination program using raw input, if, elif, else"""


B_P = int(raw_input('what is your blood pressure? '))

if B_P < 89:
    BP_STATUS = 'Low'
elif B_P < 119:
    BP_STATUS = 'Ideal'
elif B_P < 139:
    BP_STATUS = 'Warning'
elif B_P < 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your blood pressure is: {}'.format(BP_STATUS)
print OUTPUT

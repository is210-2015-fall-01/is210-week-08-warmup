# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Using raw_input and if, else statements"""


BP = (int(raw_input('What is your blood pressure? ')))

if BP <= 89:
    BP_STATUS = 'Low'

elif BP is 90 and BP <= 119:
    BP_STATUS = 'Ideal'

elif BP is 120 and BP <= 139:
    BP_STATUS = 'Warning'

elif BP is 140 and BP <= 159:
    BP_STATUS = 'High'

elif BP >= 160:
    BP_STATUS = 'Emergency'

NOTIFY = 'Your status is currently: {}'.format(BP_STATUS)

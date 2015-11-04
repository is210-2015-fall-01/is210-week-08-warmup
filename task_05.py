# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Using raw_input and if, else statements"""


BP = (int(raw_input('What is your blood pressure? ')))

if BP <= 89:
    BP_STATUS = 'Low'

elif 90 <= BP <= 119:
    BP_STATUS = 'Ideal'

elif 120 <= BP <= 139:
    BP_STATUS = 'Warning'

elif 140 <= BP <= 159:
    BP_STATUS = 'High'

else:
    BP_STATUS = 'Emergency'

NOTIFY = 'Your status is currently: {}'.format(BP_STATUS)

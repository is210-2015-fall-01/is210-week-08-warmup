#!user/bin/env python
# -*- coding: utf-8 -*-
"""Blood pressure test"""

MYINPUT = raw_input("Please input you blood pressure level: ")
BP_STATUS = int(MYINPUT)

if BP_STATUS <= 89:
    BP_STATUS = 'Low'
elif BP_STATUS >= 90 and BP_STATUS <= 119:
    BP_STATUS = 'Ideal'
elif BP_STATUS >= 120 and BP_STATUS <= 139:
    BP_STATUS = 'Warning'
elif BP_STATUS >= 140 and BP_STATUS <= 159:
    BP_STATUS = 'High'
else:
    if BP_STATUS >= 160:
        BP_STATUS = 'Emergency'

print "Your blood pressure level is {}.".format(BP_STATUS)

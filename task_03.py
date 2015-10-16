#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

MY_TEST = LOOKS_NICE and EXPENSE <= MAX_EXPENSE

if MY_TEST:
    SACRIFICE = True
elif not GET_OUT_ALIVE:
    SACRIFICE = GET_OUT_ALIVE

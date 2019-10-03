i#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:07:13 2019

@author: chelsea.vizer
"""

#1
numTechs = 1
numHelpers = 16
one = 1
while numTechs < 17:
    tryThis = (numTechs * 210) + (numHelpers * 185)
    if tryThis == 3345:
        print("# of technicians is " + str(numTechs))
    numTechs = numTechs + one
    numHelpers = numHelpers - one
    continue

#2
A = 1
B = 86499
one = 1
while A < 86499:
    total = (.074 * A) + (.081 * B)
    if total == 6751:
        print("$" + str(A) + " is the amount that's invested at 7.4 percent")
        print("$" + str(B) + " is the amount that's invested at 8.1 percent")
        totalAmount = A + B
        print(str(totalAmount))
    A = A + one
    B = B - one
    continue
    
#3
tryThis = 1
while tryThis <3000000:
    totalTaxes = .27 * int(tryThis)
    afterTaxes = int(tryThis) - int(totalTaxes)
    if afterTaxes == 895000:
        print("The total amount earned was $" + str(tryThis))
    tryThis = tryThis + 1
    continue

#6
beforeTaxes = 1
while beforeTaxes < 200000:
    amountInTaxes = beforeTaxes * .23
    takeHome = beforeTaxes - int(amountInTaxes)
    if takeHome == 40000:
        print("The amount earned before taxes was $" + str(beforeTaxes))
        print("The amount taken for tax was $" + str(amountInTaxes))
        print("Takehome amount was $" + str(takeHome))
    beforeTaxes = beforeTaxes + 1
    continue

#8
snowplow = 1
while snowplow <= 7200:
    truck = 7 * snowplow
    both = snowplow + truck
    if both == 7200:
        print("Snowplow costs $" + str(snowplow))
        print("Truck costs $" + str(truck))
    snowplow = snowplow + 1
    continue

#10
beforeTaxes = 1
while beforeTaxes <= 200000:
    amountInTaxes = int(beforeTaxes) * .28
    afterTaxes = int(beforeTaxes) - int(amountInTaxes)
    if int(afterTaxes) == 45824:
        print("The amount earned before taxes was $" + str(beforeTaxes))
    beforeTaxes = int(beforeTaxes) + 1
    continue

#14
A = 1
B = 528374
one = 1
while A < 528374:
    total = (.0945 * A) + (.0612 * B)
    if int(total) == 42854:
        print("$" + str(A) + " is the amount invested at 9.45%")
        print("$" + str(B) + " is the amount invested at 6.12%")
    A = int(A) + 1
    B = int(B) + 1
    continue
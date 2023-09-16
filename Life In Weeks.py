# -*- coding: utf-8 -*-
# """
# Created on Sun Sep 17 01:47:56 2023

# @author: talha.i
# """

# Life in weeks

age = input('What is your current age?')

age_in_days = (90 * 365) - (int(age) * 365)

age_in_weeks = (90 * 52) - (int(age) * 52)

age_in_months = (90 * 12) - (int(age) * 12)

print(f"You have {age_in_days} days, {age_in_weeks} weeks and {age_in_months} left.")

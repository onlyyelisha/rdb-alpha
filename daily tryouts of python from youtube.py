# reversing the order of the words in a list
# given_list = ["jolly", "elisha", "kimberly"]
# applying the list comprehesion skill
# result_list = [i[::-1] for i in given_list]
# the double :: ensures the reversing of the words
# taken to thorny for testing
# print(result_list)  # the result is as expected
# day 1 of practice
# day one addons
# using break points
# mimi = 6
# zack = 20
# breakpoint()  # applied the ide way of putting a breakpoint
# total_age = mimi + zack
# print(total_age)
# # day two making a swapped list
# # swapping the first three items with the last of three
# lis_of_numbers = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
# ]
# half_size = len(lis_of_numbers) // 2
# swapped_list = lis_of_numbers[half_size:] + lis_of_numbers[:half_size]
# print(swapped_list)  # it is as i pridicted i did it right
# day three
# been taught how to open a file in python using win32api a module in
# pywin32 code i remember
# import win32api
# import os
#
# filepath = r"C:\Users\PATIENCE\OneDrive\Pictures\Screenshots\moveent\Screenshot 2026-05-25 040058.png2.png"  # r makes it a raw str for py
# print(os.path.exists(filepath))  # this confirms that the file exists
# win32api.ShellExecute(  # so this is the functio i the module that does it
#     0,  # for there is no parent directory
#     "open",  # the command to open the file also print can be use
#     filepath,
#     None,  # for no parameters in shell where this api works
#     None,  # no parameters too thats why its none
#     1,  # to mean excute
# )
# # the os alternative
# import os
#
# filepath = r"C:\Users\PATIENCE\OneDrive\Pictures\Screenshots\moveent\Screenshot 2026-05-25 040058.png2.png"
# if os.path.exists(filepath):
#     try:
#         os.startfile(filepath)
#     except OSError as e:
#         # the OSError is one that catches all operating system level errors
#         print("file found but couldnt be open", e)
# else:
#     print("file not found according to path", filepath)
# # day 4 making an identity marix using numpy
# import numpy as np
#
# x = np.eye(4, M=6, K=1)  # the first parameter is for the rows
# # second parameter for the columns
# # the third for the data shirft for one in the matrix
# print(x)
# # project addons doing teclado exercises each day
# age_husi = 17
# print(f"she is born on August the seventh ,she is {17} years ilhiyasm ")
# days_in_27years = 365 * 27
# print(f"there are {days_in_27years}days in 27 years can i be married for more!!")
# from math import pi
#
# r = 5
# circle_area_of_5_radius = pi * r**2
# print(f"the circle_area_of_5_radius is {round(circle_area_of_5_radius,4)}units sq")
# day 5
# # teclado exercise
# her_name = input("What is the special ones name if you can recall\n:")
# age_in_weeks_lived = 52
# age_in_weeks_lived *= int(input("at what age in life did you find it\n:"))
# print(f"She is called {her_name} who was lived for {age_in_weeks_lived}weeks on earth")
# # fixing errors in given code
# # hourly_wage = input("Please enter your hourly wage: ")
# # print(hourly_wage)
# # hours_worked = input("How many hours did you work this week? ")
# # print(hours_worked)
# finished the exercise
# working with pandas putting leading zeros where they are needed
# # working with pandas according to the youtube guy
# import pandas as pd  # ensure the module is pip install
#
# # below we call a function in panda that reads csv files
# df = pd.read_csv('ids.csv')
# print(df)  # this prints the file as processed and refined with default changes on intergers
# df = pd.read_csv('ids.csv')  # to interrupt and make changes on how the file is displayed
# # column_name_to_be altered
# df[None] = (  # the none is for the column name i want to fill
#     df[None]  # here we specify it as a key in the file as a dict
#     .astype(str)  # we change the datatype to str
#     .str.pad(width=6,  # since its str we can pad it stating how long it should be
#              side="left",  # we specify where the padding should be add to make the specified
#              fillchar="0")  # we make the padding be filled with zeros instead of white space
#
# )  # we put this so that the addons can be verticall not horizontal
#
# print(df)

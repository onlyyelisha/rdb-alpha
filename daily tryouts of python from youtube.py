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
# day six  banking teclado
from re import findall

from numpy import char

greeting = "Hello, world"
greeting += "!"
print(greeting)
us_name = input("C'mon enter your  name below\n:").strip()
print(f"Hello ,{us_name.title()}!\n I am 20 years old")
title = "Joker"
director = "Todd Phillips"
release_year = 2019
print(f"{title} ({release_year}),directed by {director}")
# from the youtube teacher

import trimesh

box = trimesh.creation.box(extents=[0.22, 0.9, 0.12])
sphere = trimesh.creation.icosphere(3.290)
box.show()
sphere.show()
# making a fibbinacci python script
num = int(input("Enter the number: "))
a, b = 0, 1
print(f"{a} {b}", end=" ")
for i in range(num - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c


# intermediate level
def fib_iterative(num_b):
    a, b = 0, 1
    for i in range(1, num_b + 1):
        a, b = b, a + b
        print(f"{i:02}=>{b:02}", end=",\n")


fib_iterative(9)
# making a string integer cleaner using regex
import re

user_id = "haluwa758"

# saving the different data types as lists in variables
user_id_numbers = findall(r"\d", user_id)
user_id_letters = findall(r"[a-zA-Z]", user_id)
# the output  as it has been put in the variables
print(user_id_numbers)
print(user_id_letters)
# making the output strings again from list format
user_id_letters_str = " ".join(user_id_letters)
user_id_numbers_str = " ".join(user_id_numbers)
# cleaning text with numbers using without using regex
national_id = "husnaa20070807"
# checking for numbers in the given text
check_numbers = any(numeral.isdigit() for numeral in national_id)
print(check_numbers)#returns true or false
# # making a string integer cleaner using regex
# import re
#
# user_id = "haluwa758"
#
# # saving the different data types as lists in variables
# user_id_numbers = findall(r"\d", user_id)
# user_id_letters = findall(r"[a-zA-Z]", user_id)
# # the output  as it has been put in the variables
# print(user_id_numbers)
# print(user_id_letters)
# # making the output strings again from list format
# user_id_letters_str = " ".join(user_id_letters)
# user_id_numbers_str = " ".join(user_id_numbers)
#debugging to understanding the following code
# Check if string has numbers
# text = "user123"
# has_numbers = any(char.isdigit() for char in text)
# print(has_numbers)  # True
##the above line checks if there is any number then stops at the first number got
#
# # Check if string has letters
# has_letters = any(char.isalpha() for char in text)
# print(has_letters)  # True
##the above line checks if there is any string then stops at the first number got
#
# # If both exist, remove numbers
# if has_numbers and has_letters:
#     cleaned = ''.join(char for char in text if not char.isdigit())
#     print(cleaned)  # "user"
#
# # If both exist, remove letters
# if has_numbers and has_letters:
#     cleaned = "".join(char for char in text if not char.isalpha())
#     print(int(cleaned))  # 123
##have made a durable decoder gets
#all numbers and letters separated and becomes a series
national_id = "hu07snaa20070807"
# checking for numbers in the given text
check_numbers = list(filter(str.isdigit,  national_id))
print(check_numbers)#a list of numbers  in str type
#the numbers only  in the text given
onlyynumbers=int("".join(check_numbers))
print((onlyynumbers))#have made it a one form of numbers
# the_list_numbers=[int(num) for num in check_numbers]
# print(the_list_numbers)#a list of numbers int type
md_list_letters=list(filter(str.isalpha,national_id))
print(md_list_letters)
#just a combined string
onlyystr=("".join(md_list_letters))
print(onlyystr)

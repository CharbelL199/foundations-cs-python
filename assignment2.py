# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:07:07 2023

@author: Charbel Lawlach
"""
# Question 1
# =============================================================================
# user_input = input("Please enter a number:")
# 
# if user_input.isdigit():
#     number = int(user_input)
#     if number == 0:
#         dig_num = 1
#     else:
#         dig_num = 0
#         while number > 0:
#             dig_num += 1
#             number = number // 10
#     print(user_input,"has",dig_num,"digits.")
# else:
#     print("No input")
# =============================================================================

# Question 2
# =============================================================================
# n = int(input("Please enter a number:"))
# 
# for i in range(1,n + 1):
#     print("*" * i)
# 
# =============================================================================

# Question 3
# =============================================================================
# list1 = [54,76,2,4,98,100]
# while True:
#     try:
#         n = int(input("Please enter a number:"))
#         n1 = int(input("Please enter a second number:"))
#         break
#     except ValueError:
#         print("Please enter a number")
# 
# if n > n1:
#     n, n1 = n1, n
# 
# for item in list1:
#     if n <= item <= n1:
#         print(item)
# =============================================================================

# Question 4
# =============================================================================
# Names= ["Maria","Hala","Ghady","Ehsan","Joe","Zoe"]
# while True: 
#     letter = str(input("Please enter a letter:"))
#     search = [name for name in Names if letter in name]
# 
#     if search:
#         for name in search:
#             print(name)
#     else:
#         print("No letter found.")    
#     break
# =============================================================================



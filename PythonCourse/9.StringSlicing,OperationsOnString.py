# =========================================
# STRING SLICING & STRING OPERATIONS
# =========================================

# String slicing ka matlab hota hai
# string ke andar se koi hissa nikalna

# Python me har character ka index hota hai
# index 0 se start hota hai
# aur last character ka index length - 1 hota hai

# Slicing ka general format hota hai
# string[start : end]
# start se le kar end-1 tak characters milte hain

# Agar start na likho
# to slicing 0 se start hoti hai

# Agar end na likho
# to slicing last character tak chali jati hai

# Negative index ka matlab hota hai
# string ke end se count karna

# String operations ka matlab hota hai
# string par different actions lagana

# Common string operations:

# Concatenation
# do ya zyada strings ko jorna

# Repetition
# aik string ko multiple times repeat karna

# Membership
# check karna ke koi word ya character string me hai ya nahi

# Length
# string ke total characters count karna

# Comparison
# do strings ko compare karna

# Built in string functions
# jaise upper, lower, replace, split, find, strip
# ye sab string ko modify ya analyze karne ke liye use hote hain

# Strings programming me bahut important hoti hain
# kyunki user input, file data
# aur messages sab string ke form me hote hain


names = 'Ibrahim,Hassan'
print(names)
print(len(names)) # This give the length of names 
print(names[0:2]) # This give the br 
print(names[1:3]) # This give the br 

fruit = 'Apple'
AppleLen = len(fruit)

print(fruit[0:4])
print(fruit[:4]) # if you are not write the starting index Python Automaticaaly assign the start index 0 
print(fruit[0:]) # if you are not write the ending index Python Automaticaaly assign the last index of var

print('Negative Slicing\n')

print(fruit[0:len(fruit)-3])  # in negative slicng python will assign the len of var so 4-2 is 2
print(fruit[0:-3])  # in negative slicng python will assign the len of var so 4-2 is 2
print(fruit[-3:-1])  # This give the ng

# slicing includinbg start index but no end index

# Quick Quiz

nm = 'Ibrahim'
print(nm[-4:-2])


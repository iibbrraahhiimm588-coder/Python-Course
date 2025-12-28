# ========================================
# TAKING USER INPUT IN PYTHON (Full Explain)
# ========================================

# Python me user se input lene ke liye built-in function use hota hai:
# input()

# input() function har baar **string** return karta hai
# matlab chahe user number type kare ya text, wo string hi hota hai

# User input lene ka basic syntax:
# variable = input("Message dikhaye jo user ko bataye")

# Message wo text hai jo user ko dikhega
# aur user us input me value type karega
# uske baad wo value variable me store ho jati hai

# Example flow (without actual code):
# 1. Program user se age pooche
# 2. User 16 type kare
# 3. Program age variable me store ho jaye

# Important points:

# 1) Input hamesha string hota hai
# Agar user number type kare bhi, Python usko string treat karega
# Agar math operations karne ho to **type casting** karni padegi

# 2) Input me message optional hai
# Agar message nahi diya to cursor bas blink karega user ke liye
# Best practice hai hamesha message dena

# 3) Input ke sath type casting
# Number ke liye: int(input()) ya float(input())
# Boolean ke liye: bool(input())  (lekin caution, string ka conversion tricky hota hai)

# 4) User input se hum program me decisions le sakte hain
# Jaise if else conditions, loops, calculations

# 5) Common use cases:
# - Name ya text lena
# - Age ya number lena
# - Choices lena (yes/no, 1/2/3)
# - Password ya secret input (normal input ke liye)

# 6) Notes:
# - Python me input ka process **blocking** hota hai
#   Matlab program ruk jaata hai jab tak user input nahi deta
# - Input lene ke baad hamesha store karna chahiye variable me
#   warna value khatam ho jaati hai

a = input()
print(a)

b = input('Enter Your Name: ') # You will assign the placeholder in input
print("string with Placholder: ", b)

# while you will taking a input in number but you will
# not change the type of input yet python throw error

x = int(input('Enter First Number: ')) # python change the input srting into integer 
y = int(input('Enter Second Number: ')) # python change the input srting into integer 

print('int: ',x + y)

c = float(input('Enter First Number: ')) # python change the input srting into float 
d = float(input('Enter Second Number: ')) # python change the input srting into float 

print('float: ',c + d)
# ======================================================
# PYTHON CONDITIONAL STATEMENTS (IF, ELSE, ELIF)
# ======================================================

# Conditional statements ka kaam hota hai
# program me **decisions** lena

# Matlab program ko bolna:
# "Agar ye condition true hai to ye karo,
#  warna ye karo"

# Python me 3 main conditional statements hote hain:

# 1) if
# Ye check karta hai ke condition true hai ya nahi
# Agar true ho, to andar ka code run hota hai
# Agar false ho, to ignore kar deta hai

# Syntax:
# if condition:
#     # code to run if condition is true

# 2) else
# Ye tab use hota hai jab if condition false ho
# Matlab agar if ka code run nahi hua
# to else ka code run hota hai

# Syntax:
# if condition:
#     # code if true
# else:
#     # code if false

# 3) elif
# "else if" ka short form hai
# Ye tab use hota hai jab multiple conditions check karni ho
# Matlab pehli condition false ho, aur dusri condition true ho
# to uska code run ho

# Syntax:
# if condition1:
#     # code1
# elif condition2:
#     # code2
# elif condition3:
#     # code3
# else:
#     # code if all conditions false

# Important points:

# - Python me colon (:) zaroori hota hai
# - Indentation se code ka scope pata chalta hai
#   (generally 4 spaces ya tab)
# - Conditional statements boolean expression ko check karte hain
# - Multiple elif blocks allowed hain
# - Else block optional hai, lekin if block mandatory hai

# Conditional statements programming me
# **decision making** aur **logic flow** ke liye
# sabse zyada use hote hain

# =========================================
# NESTED IF STATEMENTS IN PYTHON
# =========================================

# Nested if ka matlab hota hai
# ek if ke andar doosra if ya conditional statement likhna

# Matlab:
# Agar pehli condition true ho to andar ka code chale
# Aur andar ek aur condition check karni ho
# to nested if use karte hain

# Syntax:
# if condition1:
#     # code if condition1 is true
#     if condition2:
#         # code if condition2 is also true
#     else:
#         # code if condition2 is false
# else:
#     # code if condition1 is false

# Important points:

# 1) Indentation bahut zaroori hai
# 2) Nested if me jitni bhi levels ho sakti hain
# 3) Har nested if ka else optional hai
# 4) Logical flow pehle outer if check karta hai
#    phir andar ka nested if run hota hai agar outer true ho
# 5) Nested if complex decisions me useful hote hain
#    jaise multiple conditions dependent ho ek dusre par

# Nested if statements program me
# decision making ko **layer by layer** organize karte hain


a = int(input('Enter Your Age: '))

if(a > 18):
    print("You can drive the car")
else:
    print('''You can't drive the car''')


ApplePrice = 210
budget = 200

if(ApplePrice <= budget):
    print('Add 1 kg apple in my cart')
else:
    print('''Don't add apple in my cart''')

# Nested If Else

print('Nested If Else')


num = int(input('Enter Your Number: '))

if (num < 0):
    print('Number is negative')
elif (num > 0):
    if(num <= 10):
        print('Number is between 1-10')
    elif(num > 10 and num <= 20):
        print('Number is between 10-20')
    else:
        print("Number is greater than 20")
else:
    print('Number is zero')


b = int(input('Enter Your Age; '))

if (b <= 10):
    print('You are able to walking')
elif(b <= 15):
    print('you are able to running fast camparision to old people')
elif(b <= 30):
    print('You are able to drive a car very easily')
elif(b > 50 and b <= 100):
    print('You are not able to drive a car')
else:
    print('you are old')
# =====================================
# FOR LOOP IN PYTHON (Full Explanation)
# =====================================

# For loop ka use hota hai
# kisi sequence par ek ek karke chalne ke liye

# Sequence ka matlab hota hai
# values ka group
# jaise list, string, tuple, range waghera

# For loop har value ko
# bari bari uthata hai
# aur us par kaam karta hai

# For loop ka basic structure hota hai:
# for variable in sequence:
#     # code block

# Yahan "variable"
# har iteration me
# nayi value store karta hai

# "in" keyword
# batata hai ke hum kis sequence par chal rahe hain

# Colon (:) loop ka start batata hai

# Indentation (space ya tab)
# batata hai ke kaunsa code
# loop ke andar hai

# For loop tab tak chalta hai
# jab tak sequence ki saari values
# use na ho jayein

# For loop ka use hota hai:
# - list ke har element par kaam karne ke liye
# - string ke har character par chalne ke liye
# - numbers ke range me repeat karne ke liye
# - data processing ke liye

# For loop control flow ka hissa hai
# aur program ko structured aur clean banata hai

# =========================================
# RANGE FUNCTION: START, STOP, STEP
# =========================================

# range() ka use numbers ki sequence banane ke liye hota hai
# ye for loop ke saath zyada use hota hai

# range() ke teen parts ho sakte hain:
# start -> number jahan se counting shuru ho
# stop  -> number jahan par counting ruk jaye (ye include nahi hota)
# step  -> har baar kitna jump kare

# 1) start
# ye batata hai ke sequence kis number se shuru hogi
# agar start na do, to by default 0 hota hai

# 2) stop
# ye batata hai ke sequence kis number tak jayegi
# lekin wo number khud include nahi hota

# 3) step
# ye batata hai ke har number ke beech me kitna gap hoga
# agar step na do, to by default 1 hota hai

# step positive bhi ho sakta hai aur negative bhi
# positive step me numbers aage badhte hain
# negative step me numbers peeche ki taraf jaate hain

# range() memory efficient hota hai
# kyunki ye poori list nahi banata
# balki numbers ko ek ek karke generate karta hai

# range start, stop aur step ke through
# tum loop ki speed aur direction control kar sakte ho


# name = 'Ibrahim'

# for i in name:
#     print(i)

# colors = ['Red', 'Green', 'Blue', 'Yellow']

# for color in colors:
#     print(color)
#     for character in color:
#         print(character)

# print('Range Function')

# for k in range(5):
#     print(k)
# for k in range(5,10,2):
#     print(k)


for a in range(1,11):
    if(a % 2 == 0):
        print(a)

x = int(input('Enter First Number: '))

for i in range(1, 11):
    print(f'{x} x {i} = {x * i}')
    if(i % 2 == 0):
        print('This is a even nuber')

Z = int(input('Enter Your Marks: ')) 

for marks in range(1,101):
    if(marks == 50):
        print('THIS IS GRADE C')


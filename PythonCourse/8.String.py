# ==============================
# STRING IN PYTHON (Full Explain)
# ==============================

# String ka matlab hota hai
# text ya characters ka collection

# Python me jo bhi cheez
# quotes ke andar hoti hai
# wo string hoti hai

# Quotes teen type ke hote hain
# single quotes  ' '
# double quotes  " "
# triple quotes  ''' '''  ya  """ """

# Single aur double quotes
# short text ke liye use hote hain

# Triple quotes
# long text ya multi line text ke liye use hote hain

# String me letters, numbers, spaces
# aur special characters sab aa sakte hain

# String immutable hoti hai
# matlab ek baar string ban gayi
# to uske characters ko change nahi kar sakte
# hume nayi string banani padti hai

# String indexing support karti hai
# matlab har character ka ek number hota hai
# jo 0 se start hota hai

# String slicing bhi hoti hai
# matlab string ka koi part nikalna

# String ke sath bahut saare built in functions hote hain
# jaise uppercase, lowercase, length, replace, split waghera
# jo string ko process karne me help karte hain

# String data user input me
# aur text processing me sabse zyada use hota hai

# Python me string powerful hoti hai
# kyunki isme data ko
# easily handle aur modify kar sakte hain

name = 'Ibrahim'
friend = 'Bilal'
anotherFriend = 'Ahmed'

# apple = "He said , "i want to eat apple"  # throw an error

apple = 'He said , "i want to eat apple'  
print(apple)

apple2 = '''He said , 
i have apple
"i want to eat apple"''' 
print(apple2)

name2 = 'M.Ibrahim' 

print(name2[0]) # assign a str 0 'M'
print(name2[1]) # assign a str 1 '.'
print(name2[2]) # assign a str 2 'I'
print(name2[3]) # assign a str 3 'b'
print(name2[4]) # assign a str 4 'r'
print(name2[5]) # assign a str 5 'a'
print(name2[6]) # assign a str 6 'h'
print(name2[7]) # assign a str 7 'i'
print(name2[8]) # assign a str 8 'M'
# print(name2[9]) # throw an error because the index 9 will not on the position

# for loop in python

print("Let's use a for loop\n")

for character in apple:
    print(character)
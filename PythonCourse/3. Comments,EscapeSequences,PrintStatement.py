# -------------------------------
# Comments, Print & Escape Sequences in Python
# -------------------------------

# 1️⃣ Comments
# -------------------------------
# Comments Python me likhi hui explanations hoti hain jo run nahi hoti

# Single-line comment: '#' ke saath
# Python ignore karega is line ko
print("This line will run")  # Ye comment ignore hoga

# Multi-line comment: '''...''' ya """..."""
"""
Ye multi-line comment hai
Python ignore karega isko
"""

# Comments kyun use karte hain?
# - Code ko explain karne ke liye
# - Complex logic samjhane ke liye
# - Temporary code ignore karne ke liye

# -------------------------------
# 2️⃣ Print Statement
# -------------------------------
# print() function screen pe 
# -------------------------------
# Escape Sequences in Python
# -------------------------------

# 1️⃣ New Line (\n)
print("Hello\nWorld")
# Output:
# Hello
# World
# Explanation: \n se "World" new line me chala gaya

# 2️⃣ Tab Space (\t)
print("Python\tProgramming\tFun")
# Output:
# Python    Programming    Fun
# Explanation: \t se words ke beech horizontal tab space aaya

# 3️⃣ Backslash (\\)
print("Folder path: C:\\Users\\Python")
# Output:
# Folder path: C:\Users\Python
# Explanation: \\ ka matlab ek real backslash print karna

# 4️⃣ Single Quote (\')
print('It\'s easy')
# Output:
# It's easy
# Explanation: \' se single quote string me add hua

# 5️⃣ Double Quote (\")
print("He said \"Hi\"")
# Output:
# He said "Hi"
# Explanation: \" se double quote string me add hua

# 6️⃣ Combine Multiple Escape Sequences
print("Line1\nLine2\tTabbed\\Backslash\'Single\"Double")
# Output:
# Line1
# Line2    Tabbed\Backslash'Single"Double
# Explanation: \n->new line, \t->tab, \\->backslash, \'->single quote, \"->double quote

# 7️⃣ Summary
# \n  -> New line
# \t  -> Tab space
# \\  -> Backslash
# \'  -> Single quote
# \"  -> Double quote
# Backslash (\) ka kaam hai string me special character represent karna

print("hi \n Ibrahim")
print('hi \t Ibrahim')
print("Folder path: C:\\Users\\Python")
print('It\'s easy')
print("He said \"Hi\"")
print("Line1\nLine2\tTabbed\\Backslash\'Single\"Double")



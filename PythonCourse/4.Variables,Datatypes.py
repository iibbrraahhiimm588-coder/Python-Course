# -------------------------------
# Variables & Data Types in Python
# -------------------------------

# 1️⃣ Variables
# -------------------------------
# Variable ek container hai jisme hum data store karte hain
# Variable ka name hota hai jisse hum value access karte hain
# Rules for variable names:
# 1. Letters, numbers, aur underscore (_) use kar sakte ho
# 2. Number se start nahi hona chahiye
# 3. Case sensitive hai (age != Age)
# Variable ka value kabhi bhi change kiya ja sakta hai

# -------------------------------
# 2️⃣ Data Types
# -------------------------------
# Python me main data types:

# Integer (int) -> Whole numbers, jaise 10, -5
# Float (float) -> Decimal numbers, jaise 3.14, -7.5
# String (str) -> Text, jaise "Hello"
# Boolean (bool) -> True ya False
# Complex (complex) -> Complex numbers, jaise 2 + 3j

# Python automatically variable ka type assign kar deta hai jab value assign karte hain
# type() function se variable ka data type check kiya ja sakta hai

# -------------------------------
# 3️⃣ Multiple Assignment
# -------------------------------
# Ek hi line me multiple variables assign kiye ja sakte hain
# Ek hi value ko ek saath multiple variables me assign bhi kiya ja sakta hai

# -------------------------------
# 4️⃣ Summary
# -------------------------------
# Variable = data store karne ka container
# Data Types = Integer, Float, String, Boolean, Complex
# type() = variable ka type check karne ke liye
# Variable ke values change kiye ja sakte hain

# -------------------------------
# End of Explanation
# -------------------------------


a = 32143242
print(a)

b = 'Ibrahim'
print(b)

print(type(b))
print(type(a))

c = 'Bilal'
d = c

print(d)

e = 2
f = 5

print(e + f)
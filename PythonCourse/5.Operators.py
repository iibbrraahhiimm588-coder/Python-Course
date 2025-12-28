# ============================
# PYTHON OPERATORS FULL GUIDE
# ============================

# 1) ARITHMETIC OPERATORS
# Ye math ke liye use hote hain

a = 10
b = 3

print(a + b)   # +  addition  -> 10 + 3 = 13
print(a - b)   # -  subtraction -> 10 - 3 = 7
print(a * b)   # *  multiply -> 10 * 3 = 30
print(a / b)   # /  division -> 10 / 3 = 3.33
print(a % b)   # %  remainder -> 10 % 3 = 1
print(a ** b)  # ** power -> 10^3 = 1000
print(a // b)  # // floor division -> 10 // 3 = 3


# 2) COMPARISON OPERATORS
# Ye True ya False return karte hain

print(a == b)   # equal
print(a != b)   # not equal
print(a > b)    # greater than
print(a < b)    # less than
print(a >= b)   # greater or equal
print(a <= b)   # less or equal


# 3) LOGICAL OPERATORS
# Conditions ko jodne ke liye

x = 5
y = 10

print(x < y and x > 2)   # and: dono condition true honi chahiye
print(x > y or x > 2)   # or: aik bhi true ho to true
print(not(x > y))      # not: ulta kar deta hai


# 4) ASSIGNMENT OPERATORS
# Value assign ya update karne ke liye

n = 10
n += 5   # n = n + 5
print(n)

n -= 3   # n = n - 3
print(n)

n *= 2
print(n)

n /= 4
print(n)


# 5) BITWISE OPERATORS
# Binary numbers ke saath kaam karte hain

p = 5   # 0101
q = 3   # 0011

print(p & q)   # AND
print(p | q)   # OR
print(p ^ q)   # XOR
print(~p)      # NOT
print(p << 1)  # left shift
print(p >> 1)  # right shift


# 6) MEMBERSHIP OPERATORS
# List ya string me value hai ya nahi check karte hain

nums = [1, 2, 3, 4, 5]

print(3 in nums)        # True
print(10 not in nums)  # True


# 7) IDENTITY OPERATORS
# Ye memory location check karte hain

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)      # same object
print(a is b)      # different object
print(a is not b)  # true


# 8) WALRUS OPERATOR :=
# Ye variable assign aur check ek hi line me karta hai

if (n := 10) > 5:
    print(n)

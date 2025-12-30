# =========================================
# FUNCTION ARGUMENTS IN PYTHON
# =========================================

# Function arguments ka matlab hota hai
# wo values jo function ko di jati hain

# Jab function call hota hai
# arguments function ke parameters me jate hain
# aur function un par kaam karta hai


# Parameter aur Argument me farq:
# Parameter function banate waqt likha jata hai
# Argument function call karte waqt diya jata hai


# Python me arguments ke types:

# 1) Positional Arguments
# Ye order ke hisaab se function me jate hain
# Pehla argument pehle parameter me
# doosra argument doosre parameter me


# 2) Keyword Arguments
# Isme hum parameter ka naam likh kar value dete hain
# Order matter nahi karta


# 3) Default Arguments
# Function me pehle se value di hoti hai
# Agar function call me value na mile
# to default value use hoti hai

# =========================================
# REQUIRED ARGUMENTS IN PYTHON
# =========================================

# Required arguments wo hote hain
# jo function ko call karte waqt dena hi dena hota hai

# Agar function ke parameters me
# koi default value na di ho
# to wo parameter required hota hai


# Matlab:
# def add(a, b):
# yahan a aur b dono required hain
# function tab tak kaam nahi karega
# jab tak dono values na di jayein


# Agar required argument miss ho jaye
# Python error de deta hai


# Required arguments positional bhi ho sakte hain
# aur keyword ke through bhi diye ja sakte hain


# Required arguments ka purpose:
# function ko batana
# ke uske kaam ke liye
# kaunsi values zaroori hain


# Required arguments bina function
# apna kaam complete nahi kar sakta


# Simple baat:
# jo arguments function ke liye must hote hain
# unko required arguments kehte hain


# 4) Variable Length Arguments
# Jab hume pata na ho
# kitne arguments aayenge
# to *args use hota hai


# 5) Keyword Variable Length Arguments
# Jab named arguments zyada hon
# to **kwargs use hota hai


# Arguments ka fayda:
# - Function flexible hota hai
# - Same function alag alag data par kaam karta hai
# - Code reusable hota hai


# Function bina arguments
# sirf fixed kaam karta hai

# Function arguments ke sath
# har bar different result de sakta hai


# Python functions ka real power
# arguments ki wajah se hota hai

# =========================================
# RETURN KEYWORD IN PYTHON
# =========================================

# return ka kaam hota hai
# function ka result wapas bhejna

# Jab function apna kaam complete karta hai
# jo value return ke sath hoti hai
# wo function call ko mil jati hai


# print aur return me farq:
# print sirf screen par dikhata hai
# return value ko bahar deta hai


# return ke baad
# function wahi par band ho jata hai
# uske baad ka code run nahi hota


# Agar function me return na ho
# to Python automatically None return karta hai


# return ka main fayda:
# function ka result kisi variable me store kar sakte hain
# aur aage program me use kar sakte hain


# return Python functions ka
# output system hai



# 1) Default Arguments
# Function me pehle se value di hoti hai
# Agar function call me value na mile
# to default value use hoti hai

print('''"Default Arguments"\n''','\n')


def average(a=3, b=3):
    print('The average is: ',(a + b)/2)

average(b=6) 

def names(fname, mname = 'Bilal', lname = 'Ahmed'):
    print('Hello',fname,mname,lname,' \n')

names('Ibrahim') # this is the default arg of fname

# 2) Keyword Arguments
# Isme hum parameter ka naam likh kar value dete hain
# Order matter nahi karta

print('''"KeyWords Arguments" \n''')

def isAverage(a, b):
    print('The average is: ', (a + b)/2)

isAverage(b=21,a = 4)

def name(fname, mname, lname):
    print('Hello',fname,mname,lname ,'\n')

name(mname= 'Ibrahim', lname = 'Ahmed', fname = 'Bilal')


# 3) Required arguments positional bhi ho sakte hain
# aur keyword ke through bhi diye ja sakte hain


# Required arguments ka purpose:
# function ko batana
# ke uske kaam ke liye
# kaunsi values zaroori hainRequired arguments positional bhi ho sakte hain
# aur keyword ke through bhi diye ja sakte hain


# Required arguments ka purpose:
# function ko batana
# ke uske kaam ke liye
# kaunsi values zaroori 

print('''"Reuired Arguments" \n''','\n')


def Calculate(a,b,c = 1): # in this case you should neccary to pass the value of a , b and the c is optional 
    print('the sum is :',(a + b + c))

Calculate(a = 5 , b = 10)

def Multiply(a,b,c = 1): # in this case you should neccary to pass the value of a , b and the c is optional 
    print('the multiply is :',(a * b * c))

Multiply(a = 5 , b = 10)

# 4) Variable Length Arguments
# Jab hume pata na ho
# kitne arguments aayenge
# to *args use hota hai

print('''"Variable Length Arguments" \n''')

def findaverage(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    print('The average is: ',sum / len(num),'\n')


findaverage(6,7)

# 5) Keyword Variable Length Arguments
# Jab named arguments zyada hon
# to **kwargs use hota hai

print('''"Keyword Variable Length Arguments" \n''')


def isnames(**name):
    return('Hello', name['fname'],name['mname'],name['lname'])

c = isnames(fname='Ibrahim', mname = 'Bilal', lname = 'Ahmed'
)
print(c)



# =========================================
# PYTHON FUNCTIONS – Full Explanation
# =========================================

# Function ka matlab hota hai
# code ka ek aisa block jo bar bar use kiya ja sakta hai

# Jab hum function banate hain
# hum apne code ko reusable bana dete hain
# aur program ko clean aur organized rakhte hain


# Function kyu use hote hain
# - Code repeat nahi hota
# - Program easy to read hota hai
# - Large program ko chhote parts me tod sakte hain
# - Bugs kam hote hain


# Function ka basic structure hota hai:
# def function_name(parameters):
#     function body
#     return value


# def ka matlab hai
# hum Python ko bata rahe hain ke ek function define ho raha hai


# Function ke parts:
# 1) Function name
# 2) Parameters (input jo function leta hai)
# 3) Function body (andar ka code)
# 4) Return value (jo function wapas deta hai)


# Jab hum function call karte hain
# tab function ka andar wala code run hota hai


# Function do tarah ke hote hain:
# 1) Built in functions (print, len, input etc)
# 2) User defined functions (jo hum khud banate hain)


# Parameters ka matlab hota hai
# function ko di jane wali values

# Return ka matlab hota hai
# function ka result wapas bhejna


# Agar return na likha ho
# to function None wapas karta hai


# Function ke fayde:
# - Code modular ban jata hai
# - Testing asaan hoti hai
# - Changes ek jagah se ho jate hain
# - Large programs manageable ho jate hain


# Local variable:
# Jo variable function ke andar banta hai
# wo sirf function ke andar hi use hota hai


# Global variable:
# Jo function ke bahar banta hai
# wo poore program me use ho sakta hai


# Function Python programming ka
# sabse important part hai
# har real world program functions par hi based hota hai

# =========================================
# PASS KEYWORD IN PYTHON
# =========================================

# pass ka matlab hota hai
# yahan Python ko ek statement chahiye tha
# lekin hum abhi koi kaam nahi karna chahte

# pass sirf ek placeholder hota hai
# taake Python error na de

# Python empty blocks allow nahi karta
# isliye jab block khali chhodna ho
# tab pass use hota hai


# pass function ke andar
# future code ke liye jagah banata hai

# pass if statement me
# tab use hota hai jab koi action na ho

# pass loops me
# structure complete karta hai bina kuch kiye


# pass kya nahi karta:
# - koi output nahi deta
# - loop ko skip nahi karta
# - loop ko stop nahi karta

# pass sirf Python ko bolta hai:
# "is line ko ignore karo aur aage badho"


def calculateGmean(a, b):

    mean = (a*b)/(a+b)
    print(mean)

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

calculateGmean(a, b)

def isGreather(x, y):
    if(x > y):
        print('firt is greather')
    else:
        print('second is greather')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

isGreather(a, b)

def isLesser(c, d):
    if(x < y):
        print('First number is less than second number')
    else:
        print('Second number is less than first number')

c = int(input('Enter first number: '))
d = int(input('Enter second number: '))

isLesser(c, d)


# def isPasser(a, b):
#     pass # This will throw the error

def Passer(a, b):
    pass # This will not throw the error
# =====================================
# TYPE CASTING IN PYTHON (Clear Explain)
# =====================================

# Type casting ka simple matlab hota hai
# aik data ko aik type se doosre type me badalna

# Jaise Python me data alag alag forms me hota hai
# number, decimal, text, true false waghera
# lekin har kaam har type se nahi hota

# Kabhi hume number chahiye hota hai
# lekin data string hota hai
# kabhi hume text chahiye hota hai
# lekin data number hota hai
# isi liye type casting use hoti hai

# Python me type casting built in hoti hai
# matlab Python khud hi functions deta hai
# jin se hum data ka type change kar sakte hain

# int() ka kaam hota hai
# kisi value ko poora number banana

# float() ka kaam hota hai
# kisi value ko decimal number banana

# str() ka kaam hota hai
# kisi value ko text banana

# bool() ka kaam hota hai
# kisi value ko True ya False banana

# Type casting do tarah se hoti hai

# Implicit casting
# isme Python khud data ko safe type me badal deta hai
# jab alag types ke numbers saath use hote hain

# Explicit casting
# isme hum khud Python ko batate hain
# ke kis type me convert karna hai

# Type casting tab use hoti hai
# jab hume kisi value par
# math, comparison, ya logic lagana ho
# aur uska type match na kar raha ho

# Agar data galat form me ho
# aur us type me convert na ho sakta ho
# to Python error deta hai
# isliye type casting hamesha soch samajh kar karni chahiye


a = 1
b = 2

c = '5'
d = '6'
print(a + b)
print(int(a) + int(b)) # This is the explict conversion

# Explicit TypeCasting Exmples

String = '50'
Number = 60

String_Number = int(String)

sum = String_Number + Number

print('The Sum Of Both Number Is: ',sum)

# Implicit TypeCasting Exmples

num1 = 5  # the python automatically change num into int 
num2 = 10  # the python automatically change num into int 

sum2 = num1 +  num2

print(sum2)
print(type(sum2))


num3 = 5.5  # the python automatically change num into int 
num4 = 10  # the python automatically change num into int 

sum3 = num3 + num4

print(sum3)
print(type(sum3))


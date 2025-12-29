# ==========================================
# PYTHON MATCH-CASE STATEMENT (Python 3.10+)
# ==========================================

# Match-case Python 3.10 me introduce hua
# Ye ek **modern way** hai multiple conditions check karne ka
# Traditional if-elif-else ka cleaner alternative hai

# Match-case ka kaam:
# - Ek variable ya expression ke value ke basis par
#   alag-alag code execute karna

# Syntax:
# match expression:
#     case value1:
#         # code if expression == value1
#     case value2:
#         # code if expression == value2
#     case _:  # default case, if no match
#         # code if nothing matches

# Important points:

# 1) match ke andar expression check hota hai
# 2) case me value likhi jaati hai jo match hone par execute hoti hai
# 3) case _ -> default case, agar koi match na ho
# 4) Ye statement **clean aur readable** hai
# 5) Multiple cases me same code run karwana ho to:
#    case value1 | value2:
#        # code
# 6) Pattern matching bhi possible hai advanced usage me
#    jaise sequences, lists, dictionaries ke structure ke saath

# Match-case ki wajah se
# long if-elif chains ko avoid kiya ja sakta hai
# aur program readable aur maintainable banta hai

# Example flow (without actual code):
# Ek variable color ho

color = 'red'

match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case _:
        print("Unknown color")


x = int(input("Enter your age: "))

match x:
    case 1:
        print('You are not able to drive a car')
    case x if x <= 10:
        print("You are able to drive a cycle")
    case x if x <= 30:
        print('Your are able to drive a car')
    case _:
        print('You are old')


a = int(input("Enter Your Number: "))

match a:
    case x if a < 0:
        print('Number is negative')
    case x if a <= 5:
        print('Number is positive')
    case x if a % 2 == 0:
        print('Number is even')
    case x if a % 2 == 1:
        print('Number is odd')
    case _:
        print('close')
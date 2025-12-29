# =========================================
# WHILE LOOP IN PYTHON (Full Explanation)
# =========================================

# While loop ka use tab hota hai
# jab hume **repeat** karna ho
# lekin number of times pehle se na pata ho

# While loop condition check karta hai
# agar condition True hai
# to loop ka code chalta hai
# aur phir dobara condition check hoti hai

# Jab condition False ho jaye
# loop automatically ruk jata hai

# Basic structure:
# while condition:
#     # code block

# Important points:

# 1) Condition boolean expression hoti hai
#    True ya False return karti hai
# 2) Loop tab tak chalega jab tak condition True hai
# 3) Indentation zaroori hai, ye batata hai
#    kaunsa code loop ke andar hai
# 4) Infinite loop se bachne ke liye
#    condition ko loop me update karna zaroori hai
# 5) While loop ka use tab hota hai
#    jab repeat karna ho, lekin exact count na pata ho
#    jaise user input validate karna, menu show karna
# 6) While loop me break aur continue
#    use karke flow control kar sakte hain

i = int(input("Enter The Number:"))
while (i < 38):
    i = int(input("Enter The Number:"))
    print(i)

print('okay')

count = 5

while (count > 0):
    print(count)
    count = count -1

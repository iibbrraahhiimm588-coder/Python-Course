# =========================================
# BREAK & CONTINUE IN PYTHON (Explanation)
# =========================================

# break statement ka kaam hota hai
# loop ko turant band kar dena

# Jab break chalta hai
# loop wahi par ruk jata hai
# aur program loop ke bahar chala jata hai

# break tab use hota hai
# jab humein koi specific condition mil jaye
# aur aage loop chalane ki zarurat na rahe


# continue statement ka kaam hota hai
# current iteration ko skip karna

# Jab continue chalta hai
# us iteration ka baaki code run nahi hota
# aur loop next iteration par chala jata hai

# continue tab use hota hai
# jab hume kisi particular value ya condition ko ignore karna ho
# aur baaki loop normally chalta rahe


# Difference samajh lo:

# break  -> loop ko poori tarah stop karta hai
# continue -> sirf current round ko skip karta hai

a = int(input('Enter The Number: '))

for i in range(1,11):
    print(a, 'x', i, '=', (a * i))
    if(i == 5):
        break  # This will break the loop 

    
x = int(input('Enter The Number: '))

for z in range(1,11):
    if(z == 5):
        print('This iteration is skipped')
        continue  # This will skip the iteration 
    print(x, 'x', z, '=', (x * z))
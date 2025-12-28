# # # -------------------------------
# # # Python Modules kya hotay hain?
# # # -------------------------------

# # # Module ek Python file hoti hai jisme ready-made functions hote hain
# # # jinko hum apne program me use kar sakte hain.

# # # Example: math ek built-in module hai

# import math
# print(math.sqrt(25))   # sqrt function math module se use ho raha hai


# # # -------------------------------
# # # Modules ke types
# # # --------------------------# -------------------------------
# # Python Modules kya hotay hain
# # -------------------------------

# # Module = Python file jisme ready-made functions hote hain
# # jinko hum apne program me use kar sakte hain

# # Built-in module example
# import math
# print("Square root of 25 is:", math.sqrt(25))


# # -------------------------------
# # Built-in module: random
# # -------------------------------
# import random
# print("Random number:", random.randint(1, 10))


# # -------------------------------
# # External module example
# # -------------------------------
# # Pehle terminal me run karo:
# # pip install requests

# import requests
# response = requests.get("https://api.github.com")
# print("Status code from API:", response.status_code)


# # -------------------------------
# # User-defined module example
# # -------------------------------
# # Iske liye same folder me ek file banao: calc.py
# # Us calc.py me yeh likho:
# #
# # def add(a, b):
# #     return a + b

# # Ab yahan use karo:
# import calc
# print("4 + 5 =", calc.add(4, 5))


# # -------------------------------
# # Summary (comments)
# # -------------------------------
# # Built-in modules: math, random (pip se install nahi karte)
# # External modules: requests (pip se install hota hai)
# # User-defined modules: calc (hum khud banate hain)
# # pip = Python ka package manager
# -----

# # # 1) Built-in modules
# # # Ye Python ke sath already aate hain
# # # jaise: math, random, datetime, os

# # import random
# print(random.randint(1, 10))


# # # 2) User-defined modules
# # # Ye hum khud banate hain
# # # Example: ek file banayi calc.py

# # # calc.py me:

# def add(a, b):
#     return a + b

# main.py me:

# import calc
# print(calc.add(4, 5))


# # # 3) External modules
# # # Ye Python ke sath nahi aate
# # # Inko pip se install karna hota hai
# # # Jaise: requests, numpy, pandas, flask


# # # -------------------------------
# # # pip kya hota hai?
# # # -------------------------------

# # # pip Python ka package manager hota hai
# # # Matlab ye internet se Python libraries download karta hai

# # # Command line me:
# # # pip install requests

# # # Uske baad code me:

# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)


# # # -------------------------------
# # # pip ke common commands
# # # -------------------------------

# # # pip install library_name     -> library install karne ke liye
# # # pip uninstall library_name  -> library remove karne ke liye
# # # pip list                    -> installed libraries dekhne ke liye
# # # pip install --upgrade pip   -> pip ko update karne ke liye


# # # -------------------------------
# # # Short Summary
# # # -------------------------------

# # # Module = Python code ka ready-made box
# # # Built-in module = Python ke sath aata hai
# # # External module = pip se install hota hai
# # # pip = Python ka Play Store

# =================================================
# PYTHON STRING METHODS, AND EXAMPLES
# =================================================

# =========================
# STRING EXAMPLES
# =========================
text = "  Hello World Python 123  "

# upper() -> sab letters capital
print(text.upper())
# OUTPUT:   HELLO WORLD PYTHON 123  

# lower() -> sab letters small
print(text.lower())
# OUTPUT:   hello world python 123  

# capitalize() -> sirf pehla letter capital
print(text.capitalize())
# OUTPUT:   hello world python 123  

# title() -> har word ka pehla letter capital
print(text.title())
# OUTPUT:   Hello World Python 123  

# strip() -> start aur end ke spaces hata deta hai
print(text.strip())
# OUTPUT: Hello World Python 123

# lstrip() -> left side ke spaces remove
print(text.lstrip())
# OUTPUT: Hello World Python 123  

# rstrip() -> right side ke spaces remove
print(text.rstrip())
# OUTPUT:   Hello World Python 123

# replace() -> word change karna
print(text.replace("Python", "Java"))
# OUTPUT:   Hello World Java 123  

# find() -> word ka index batata hai
print(text.find("World"))
# OUTPUT: 8

# count() -> word/letter kitni baar aya
print(text.count("o"))
# OUTPUT: 3

# startswith() -> string kis word se start hoti hai
print(text.strip().startswith("Hello"))
# OUTPUT: True

# endswith() -> string kis word par end hoti hai
print(text.strip().endswith("123"))
# OUTPUT: True

# split() -> string ko list me todna
print(text.split())
# OUTPUT: ['Hello', 'World', 'Python', '123']

# join() -> list ko string me jorna
words = ["Python", "is", "fun"]
print(" ".join(words))
# OUTPUT: Python is fun

# isupper() -> sab capital hai ya nahi
print("HELLO".isupper())
# OUTPUT: True

# islower() -> sab small hai ya nahi
print("hello".islower())
# OUTPUT: True

# isdigit() -> sirf numbers hai ya nahi
print("123".isdigit())
# OUTPUT: True

# isalpha() -> sirf letters hai ya nahi
print("Hello".isalpha())
# OUTPUT: True

# isalnum() -> letters aur numbers dono hai ya nahi
print("Hello123".isalnum())
# OUTPUT: True

# len() -> string ki length
print(len(text))
# OUTPUT: 24
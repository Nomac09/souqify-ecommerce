import sys
print(sys.executable)  # This will show which Python interpreter is being used
print("\nTesting imports:")
import numpy as np
import pandas as pd
print("All imports successful!")


# This is your first Python program - let's learn some basics!

# 1. Variables and printing
name = input("What's your name? ")  # This will ask for user input
print(f"Hello, {name}! Let's learn Python together!")

# 2. Numbers and basic math
age = 25
pi = 3.14159
print(f"\nSome number examples:")
print(f"Integer: {age}")
print(f"Decimal: {pi}")
print(f"Basic math: {age} + 5 = {age + 5}")

# 3. Lists (collections of items)
programming_languages = ["Python", "JavaScript", "Java"]
print(f"\nYour first list - Programming Languages:")
for language in programming_languages:
    print(f"- {language}")

# 4. Simple conditional (if statement)
if len(name) > 5:
    print(f"\nYou have a long name!")
else:
    print(f"\nYou have a short name!")
    
    
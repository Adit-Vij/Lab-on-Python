# Question 89: Importing Modules Dynamically
import importlib

# Dynamically import the 'math_utils' module
math_utils = importlib.import_module('math_utils')

# Use the 'add' function from the dynamically imported module
result = math_utils.add(15, 30)
print(result)  
print("THIS CODE IS WRITTEN BY ADIT VIJ ERP- 0221BCA042")
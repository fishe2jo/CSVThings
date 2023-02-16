# main.py

from utilsPackage.utils import *

# Call the function and store what it returns 
#  in a variable called data
data = read_CSV_file()
#print(data)
#print(data[-1])
# I want a set of all the collision types
collisionTypes = set([row[6] for row in data])
print(collisionTypes)
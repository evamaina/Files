handle = open("test.txt", "r")
# To read many lines we use the readlines() method.

data = handle.readlines()
print(data)

handle.close()
"""Here the readlines() returns a list of all
the lines in our file separated \n new line tags."""

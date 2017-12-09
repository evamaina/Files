handle = open("test.txt", "r")
data = handle.read()
counter = 0
for word in data.split():
    if word == "Python":
        counter += 1
print(counter)

"""Here we used the split() method to transform
 data into a list of words which we loop through
 and search if the word matches "Python" and adds one to the counter.
 """
 
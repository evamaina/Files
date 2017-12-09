handle = open("test-write.txt", "w")

handle.write("Hello Eva")
handle.close()
"""
When we run this on our console we see a new file text-write.txt
has been created in our project folder and the text "Hello Eva" is in it.
We need to be careful when we do this because when we use the "w"
on an existing file it will overwrite all the content in that file.
"""
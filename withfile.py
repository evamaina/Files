with open("test.txt", "r") as handle:
    data = handle.read()
    print(data)
    """
    Python has a with operator that can simplify how
     we read and write files. The operator creates a
      context manager that automatically closes the
       file when you are done.Here we open the file,
        but we do not provide a closing operation. All
         the functionality we want to do with the data from the file,
          is done in the with block.
          """
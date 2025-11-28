with open ("log.txt", "a+") as f:
    f.write("Program ran successfully\n")

with open("log.txt", "r") as f:
    print(f.read())


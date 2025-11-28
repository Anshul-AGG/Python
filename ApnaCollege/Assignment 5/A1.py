with open("names.txt", "w") as f:
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        f.write(name + "\n")

with open ("names.txt", "r") as f:
    print("\nNames in file")
    print(f.read())
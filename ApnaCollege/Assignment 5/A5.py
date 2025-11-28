try:
    with open("data.txt", "r") as f:
        f.data()

except:
    print("File not found.")

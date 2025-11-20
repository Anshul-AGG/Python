while True:
    n = int(input("Enter the number: "))
    if n > 0:
        print("Positive")
    else:
        print("Negative")
    choice = input("Exit the program? Y/N ")
    if choice == "Y":
        print("Terminated")
        break
    else:
        continue

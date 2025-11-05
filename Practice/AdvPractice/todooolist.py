#To-Do List App: A command-line application to add, view, and delete tasks.

#to_do = eval("[" + input("Add the task: ") + "]") 
to_do = input("Add the task: ")

view = (input("To view the list type 'V' : ")).lower()
if view == "v":
    print(to_do)
    
delete = (input("To delete type delete 'D' : ")).lower()
if delete == "d":
    #to_do.clear()
    to_do = ""
    print("List is empty balak")


   





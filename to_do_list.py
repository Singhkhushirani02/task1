import select


tasks=[]

def addNewTask(task):
    tasks.append(task)
    print("Add New Task:",task)

def removeTask(task):
    if task in tasks:
        tasks.remove(task)
        print("Task To Remove:",task)
    else:
        print("Unable To Find Task")

def displayTask():
    if tasks:
        print("List Of Task Are:")
        for i, task in enumerate(tasks,1):
            print(f"(i). (task)")
    else:
        print("No Task Found To Display")

while True:
    print("\nToDo List:")
    print("1.Task To Add")
    print("2.Task To Remove")
    print("3.Display Of Task")
    print("4.Quit")

    select=input("Enter your Choice:")

    if select=="1":
        task = input("Enter New Task To:")
        addNewTask(task)
    elif select=="2":
        task=input("Enter Task To Remove:")
        removeTask(task)
    elif select=="3":
        displayTask()
    elif select=="4":
        print("Quit")
        break
    else:
        print("Please Try again")





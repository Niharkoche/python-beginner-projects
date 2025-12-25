newList = []
def makeList():
    num = 1
    while True:
        userInput = input("Enter task (type 'stop' to finish): ")
        if userInput.lower() == "stop":
            break
        newList.append(f"{num}. {userInput}")
        num += 1
def Todo():
    print("Press (1) to create a new list")
    print("Press (2) to view existing list")
    user = input("Enter choice: ")
    if user == "1":
        makeList()
        with open("list.txt", "a") as file:
            for task in newList:
                file.write(task + "\n")
        print("Tasks saved successfully!")
    elif user == "2":
        print("\nYOUR TO DO LIST!!")
        try:
            with open("list.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No to-do list found!")
    else:
        print("Invalid choice")
Todo()

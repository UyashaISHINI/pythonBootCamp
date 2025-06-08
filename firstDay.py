
tasks=[]
while(True):
    print("These are the tasks : ")
    print("1. Add tasks")
    print("2. Delete task")
    print("3. Show tasks")
    print("4. Exit")
    x=int(input("Enter the number : "))
    if(x==1):
        task = input("Enter the task you have to add : ")
        tasks.append(task)
        print("You added : ",task)
    elif(x==2):
        for i,task in enumerate(tasks):
            print(f"{i + 1} . {task}")
        num = int(input("Enter the number you have to delete : "))
        tasks.pop(num-1)
        print("Existing items")
        for i,task in enumerate(tasks):
            print(f"{i + 1} . {task}")
    elif(x==3):
        for i,task in enumerate(tasks):
            print(f"{i + 1} . {task}")
    else:
        break
    
print("thankyou")

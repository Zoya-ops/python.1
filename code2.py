def main():
    tasks = []
    print (".....WELCOME TO TASK MANAGING APP.....")
    total_task = int(input("enter number of tasks you wanted to do : "))
    for i in range (1,total_task+1):
        task_name = input("enter your task = ")
        tasks.append(task_name)
        
    print("Todays tasks are \n",tasks)
    while True:
        operation = int(input("ENTER\n 1 for adding any task\n 2 for updating task \n 3 for deleting any task \n 4 for viewing any task \n 5 for exit/stop "))
        if (operation == 1):
            add = input("which task you want to add:")
            tasks.append(add)
            print("your task has been sucessfully added")

        elif (operation == 2):
            update = input("which task you want to update: ")
            if(update in  tasks):
                add = input("enter new task: ")
                ind = tasks.index(update)
                tasks[ind] = add
  #3 for deleting any task              
            print("task updated sucessfully = ",add)
        elif (operation == 3):
            delt = input ("which task you want to delete: ")
            if delt in tasks:
                ind = tasks.index(delt)
                del tasks[ind]
#4 for viewing any task
        elif (operation == 4 ):
            print("your daily tasks is",tasks)

        elif(operation == 5):
            break
        else:
            print("you select an invalid option") 
    print("THANK YOU")
main()
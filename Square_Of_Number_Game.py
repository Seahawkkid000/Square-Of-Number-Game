i=1
breaking=""
finished=0
while(i<=10*finished+10):
    if(breaking=="true"):
        break
    print("1. Find The Square Of", i)
    print("2. Restart")
    print("3. Exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        print("The square of", i, "is", i**2)
        print("You are", i*10,"%", "done")
        i=i+1
    elif(choice==2):
        i=1
        print("You have restarted")
    elif(choice==3):
        leave=input("Are you sure you would like to leave? Warning: Variables and Values will not be saved")
        leave=leave.lower()
        if(leave=="yes"):
            print("Bye! Have a great day")
            breaking="true"
            break
        elif(leave=="no"):
            i=i
        else:
            print("Invalid Input. Please Try Again!")
    else:
        print("Invalid Input")

if(i==10*finished+10):
    finished=finished+1
    print("Congratulations on completing the first round!")
    print("1. Play the next round")
    print("2. Exit")
    choice2=int(input("Enter your choice"))
    if(choice2==1):
        while(i<=10*finished+10):
            if(breaking=="true"):
                break
            print("1. Find The Square Of", i)
            print("2. Restart")
            print("3. Exit")
            choice=int(input("Enter your choice"))
            if(choice==1):
                print("The square of", i, "is", i**2)
                print("You are", (i-10)/(10*finished)*100,"%", "done")
                i=i+1
            elif(choice==2):
                i=11
                print("You have restarted")
            elif(choice==3):
                leave=input("Are you sure you would like to leave? Warning: Variables and Values will not be saved")
                leave=leave.lower()
                if(leave=="yes"):
                    print("Bye! Have a great day")
                    breaking="true"
                    break
                elif(leave=="no"):
                    i=i
                else:
                    print("Invalid Input. Please Try Again!")
            else:
                print("Invalid Input")

    elif(choice2==2):
        leave=input("Are you sure you would like to leave? Warning: Variables and Values will not be saved")
        leave=leave.lower()
        if(leave=="yes"):
            print("Bye! Have a great day")
        elif(leave=="no"):
            i=i
        else:
            print("Invalid Input. Please Try Again!")
if(i==10*finished+10):
    print("Congratulations on completing the second round!")
    print("1. Take the quiz")
    print("2. Exit")
    choice3=int(input("Enter your choice"))
    if(choice3==1):
        i=1
        while(i<=20):
            question=int(input("What is the square of", i))

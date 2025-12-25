def calculate():
    print("CALCULATOR IS STARETED!!")
    numbers=(input("Enter Calculation(EX:1+2):-"))
    num=""
    cal_list=[]
    for i in numbers:
        if i.isdigit():
            num+=i
        else:
            cal_list.append(int(num))
            cal_list.append(i)
            num=""
    cal_list.append(int(num))
    if cal_list[1]=="+":
        solution =int(cal_list[0])+int(cal_list[2])
        print("ANSWER IS",solution)
    elif cal_list[1]=="-":
        solution =int(cal_list[0])-int(cal_list[2])
        print("ANSWER IS",solution)
    elif cal_list[1]=="*":
        solution =int(cal_list[0])*int(cal_list[2])
        print("ANSWER IS",solution)
    elif cal_list[1]=="/":
        try:
            solution =int(cal_list[0])/int(cal_list[2])
            print("ANSWER IS",solution)
        except ZeroDivisionError:
            print("CAN NOT DIVIDE BY 0")
calculate()

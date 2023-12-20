"""In second year computer engineering class, group A student’s play cricket, group B 
students play badminton and group C students play football. 
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton 
b) List of students who play either cricket or badminton but not both 
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton."""

#SIMRAN SAH
#B-44

cricket,badminton,football,temp=[],[],[],[]
def accept(a,list1):
    for i in range(a):
        b=input("Enter the name of the student : ")
        list1.append(b)
def both_cric_and_bad():
    temp.clear()
    for i in cricket:
        if i in badminton:
            temp.append(i)
    print("students who play both cricket and badminton are : ",temp)
def either_cric_or_bad_but_not_both():
    temp.clear()
    for i in cricket:
        if i not in badminton:
            temp.append(i)
    for i in badminton:
        if i not in cricket:
            temp.append(i)
    print("students who play either cricket or badminton but not both are : ",temp)
def neither_cric_nor_bad():
    temp.clear()
    for i in football:
        if i not in cricket and i not in badminton:
            temp.append(i)
    print("Number of students who play neither cricket nor badminton are : ",len(temp),"\nName of the students : ",temp)
def cric_and_foot_but_not_bad():
    temp.clear()    
    for i in cricket:
        if i in football:
            if i not in badminton:
                temp.append(i)
    print("Number of students who play cricket and football but not badminton are : ",len(temp),"\nName of the students : ",temp)
def choice():
    a=input("Would you like to try other options?(y=yes/n=no) :")
    if a=='y' or a=='Y':
        menu()
    elif a=='n' or a=='N':
        print("Thank you for using the program")
    else:
        print("Enter valid entry")
        choice()
def menu():
    print("---MENU--")
    print("""1. List of students who play both cricket and badminton 
2. List of students who play either cricket or badminton but not both 
3. Number of students who play neither cricket nor badminton
4. Number of students who play cricket and football but not badminton
5.All
6.Exit""")
    a=int(input("enter your choice ="))
    if a==1:
        both_cric_and_bad()
        choice()
    elif a==2:
        either_cric_or_bad_but_not_both()
        choice()
    elif a==3:
        neither_cric_nor_bad()
        choice()
    elif a==4:
        cric_and_foot_but_not_bad()
        choice()
    elif a==5:
        both_cric_and_bad()
        either_cric_or_bad_but_not_both()
        neither_cric_nor_bad()
        cric_and_foot_but_not_bad()
    elif a==6:
        print("Thank you for using the program")
    else:
        print("Enter valid entry")
        menu()
a=int(input("Enter the number of students who play cricket="))
accept(a,cricket)
b=int(input("Enter the number of students who play badminton="))
accept(b,badminton)
c=int(input("Enter the number of students who play football="))
accept(c,football)
menu()



    

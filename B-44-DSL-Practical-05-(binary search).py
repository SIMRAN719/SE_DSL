'''a) Write a Python program to store names and mobile numbers of your friends in sorted 
order on names. Search your friend from list using binary search (recursive and nonrecursive).
Insert friend if not present in phonebook'''

#SIMRAN SAH
#B-44

name,phonebook=[],{}
def accept():
    global a
    a=int(input("Enter the number of entries you want to do :"))
    for i in range(a):
        b=input("Enter the name of the Friend :")
        c=int(input("Enter the mobile number of the friend :"))
        name.append(b)
        phonebook[b]=c
    name.sort()
#Non-recursive techniques for binary search
def non_recursive_binary_search_1():
    start=0
    end=len(name)
    mid=(start+end)//2
    a=input("Enter the name of the friend whom you want to search :")
    while(mid>=start and mid<end):
        if a in name:
            if a>name[mid]:
                start=mid
            elif a<name[mid]:
                end=mid
            elif name[mid]==a:
                print("your friend is present in the phonebook ")
                print("Phone number of %s is :"%a,phonebook[a])
                break
        else:
            print("Friend is not present in your phonebook")
            name[mid]=a
            b=int(input("Enter the phone number of the friend :"))
            phonebook[a]=b
            print(phonebook)
            break
        mid=(start+end)//2
def non_recursive_binary_search_2():
    start=0
    end=len(name)
    a=input("Enter the name of the friend whom you want to search :")
    while(start!=end):
        mid=(start+end)//2
        if name[mid]==a:
            print("your friend is present in the phonebook ")
            print("Phone number of %s is :"%a,phonebook[a])
            return 0
        elif name[mid]<a:
            start=mid+1
            continue
        else :
            end=mid
            continue
    print("Friend is not present in your phonebook")
    name.insert(mid,a)
    b=int(input("Enter the phone number of the friend :"))
    phonebook[a]=b
    print(phonebook)
#Recursive technique for binary search
def recursive_binary_search(start,end,a):
    mid=(start+end)//2
    if a in name:
        if a==name[mid]:
            print("your friend is present in the phonebook ")
            print("Phone number of %s is :"%a,phonebook[a])
        elif a>name[mid]:
            start=mid+1
            recursive_binary_search(start,end,a)
        elif a<name[mid]:
            end=mid
            recursive_binary_search(start,end,a)
    else:
        print("Friend is not present in your phonebook")
        name.insert(mid,a)
        b=int(input("Enter the phone number of the friend :"))
        phonebook[a]=b
        print(phonebook)
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
    print("""1.Binary search using non recursive technique 1
2.Binary search using non recursive technique 2
3.Binary search using recursive technique
4.Exit""")
    ch=int(input("Enter your choice :"))
    if ch==1:
        non_recursive_binary_search_1()
        choice()
    elif ch==2:
        non_recursive_binary_search_2()
        choice()
    elif ch==3:
        n=input("Enter the name of the friend who you want to serach :")
        recursive_binary_search(0,a,n)
        choice()
    elif ch==4:
        print("Thank you for using the program")
    else:
        print("please enter valid input")
        menu()
accept()
menu()
 

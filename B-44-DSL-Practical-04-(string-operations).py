'''Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not 
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string'''

#SIMRAN SAH
#B-44

a=input("Enter the String : ")
strlist=a.split()
b=len(strlist)
def longest():
    word,length=0,0
    for i in strlist:
        if len(i)>length:
            length=len(i)
            word=i
    print("longest word is",word)
def frequency():
    count=0
    s=input("enter the character whose frequency you want to check=")
    for i in a:
        if s==i:
            count+=1
    print("frequency of %s is "%(s),count)
def palindrome():
    r=a[::-1]
    if r==a:
        print("given string is palindrome")
    else:
        print("given string is not palindrome")
def index_of_appearance():
    s=input("enter the substring=")
    if s in a:
        k=a.index(s)
        print("the given substring is present at index : ",k)
    else:
        print("substring is not present in the main string")
def count_word():
    t={}
    for i in strlist:
        j=strlist.count(i)
        t[i]=j
    print("occurence of each word")
    print(t)
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
    print("---MENU---")
    print("""1. To display word with the longest length
2. To determines the frequency of occurrence of particular character in the string
3. To check whether given string is palindrome or not 
4. To display index of first appearance of the substring
5. To count the occurrences of each word in a given string
6. All the operations
7. Exit""")
    h=int(input("Enter your choice : "))
    if h==1:
        longest()
        choice()
    elif h==2:
        frequency()
        choice()
    elif h==3:
        palindrome()
        choice()
    elif h==4:
        index_of_appearance()
        choice()
    elif h==5:
        count_word()
    elif h==6:
        longest()
        frequency()
        palindrome()
        index_of_appearance()
        count_word()
        print("Thank you for using the program")
    elif h==7:
        print("Thank you for using the program")
    else:
        print("Enter valid entry")
        menu()
menu()          

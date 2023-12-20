'''Write a Python program to store first year percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using 
a) Selection Sort 
b) Bubble sort and display top five scores'''

#SIMRAN SAH
#B-44

sortlist,temp=[],[]
def accept():
    global a
    a=int(input("Enter the number of students whose marks you want to enter :"))
    for i in range(a):
        b=float(input("Enter the marks of the %s student :"%(i+1)))
        sortlist.append(b)
    
#SELECTION SORT
def selectionsort():
    temp.clear()
    for k in sortlist:
        temp.append(k)
    for i in range(a):
        rev=i
        for j in range(i+1,a):
            if temp[j]<temp[rev]:
                rev=j
        temp[i],temp[rev]=temp[rev],temp[i]
        print(temp)
    #print("sorted List :",temp)
    print("\nTop 5 scores of the class :",temp[a:a-6:-1])
#BUBBLE SORT
def bubblesort():
    temp.clear()
    for k in sortlist:
        temp.append(k)
    for i in range(a):
        for j in range(0,a-i-1):
            if temp[j]>temp[j+1]:
                temp[j+1],temp[j]=temp[j],temp[j+1]
        print(temp)
    #print("sorted List :",temp)
    print("\nTop 5 scores of the class :",temp[a:a-6:-1])
            
def menu():
    print("---MENU---")
    print("""1.selection sort
2.bubble sort""")
    ch=int(input("Enter your choice :"))
    if ch==1:
        selectionsort()
    elif ch==2:
        bubblesort()
    else:
        print("Enter valid Entry")
        menu()
accept()
menu()

    

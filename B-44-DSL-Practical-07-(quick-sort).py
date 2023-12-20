'''Write a Python program to store first year percentage of students in array. Write 
function for sorting array of floating point numbers in ascending order using quick sort 
and display top five scores.'''

#SIMRAN SAH
#B-44

sortlist=[]
def accept():
    global a
    a=int(input("Enter the number of students whose marks you want to enter :"))
    for i in range(a):
        b=float(input("Enter the marks of the %s student :"%(i+1)))
        sortlist.append(b)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
accept()
list1=quicksort(sortlist)
# Display the top five scores
print("Top 5 scores:", list1[len(list1)-5:len(list1):1])



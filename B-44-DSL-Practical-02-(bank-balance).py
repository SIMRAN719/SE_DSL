'''Write a Python program that computes the net amount of a bank account based a 
transaction log from console input. The transaction log format is shown as following: D 
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for 
withdraw and deposit) D means deposit while W means withdrawal.

Suppose the following input is supplied to the program: 
D 300, D 300 , W 200, D 100 Then, the output should be: 500
'''

#SIMRAN SAH
#B-44

print("Give spaces between your entries")
print("D=deposit, W=withdrawal")
a=input("Enter the log=")
log=a.split()
balance,d,w=0,0,0
b=len(log)
for i in range(0,b,2):
    if log[i]=="d" or log[i]=="D":
        balance+=int(log[i+1])
        d+=1
        print("Rs",int(log[i+1]),"has been credited to your account")
    elif log[i]=="w" or log[i]=="W":
        t=balance-int(log[i+1])
        if (t<0):
            print("insufficient balance")
        else:
            balance-=int(log[i+1])
            w+=1
            print("Rs",int(log[i+1]),"has been debited from your account")
print("total number of deposits=",d)
print("total number of withdraws=",w)
print("your current bank balance is :",balance)
            

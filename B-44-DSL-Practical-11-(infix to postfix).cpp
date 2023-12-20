/*Implement C++ program for expression conversion as infix to postfix and its evaluation 
using stack based on given conditions: 
1. Operands and operator, both must be single character.
2. Input Postfix expression must be in a desired format.
3. Only '+', '-', '*' and '/ ' operators are expected.
*/

// SIMRAN SAH
// B-44

#include<iostream>
#include<string.h>
using namespace std; 
int top=-1;
char infix[50];
int len;
char postfix[50];
class Stack
{
	public:
		
		void accept()
		{
			cout<<"Enter the expression:";
			cin.getline(infix,50);
			len=strlen(infix);
			
		}
		void push(char x)
		{
			top++;
			postfix[top]=x;
		}
		void pop(char x)
		{
			if(top==-1)
			{
				cout<<"invalid ";
			}
			else
			{
				top--;
				cout<<x;
			}
		}
		void check()
		{
			int y,z;
			for(int i=0;i<len;i++)
			{
				if(infix[i]>='a' && infix[i]<='z')
				{
					cout<<infix[i];
				}
				else if(infix[i]=='+' || infix[i]=='-' || infix[i]=='/' || infix[i]=='*')
				{
					if((infix[i]=='+' ||infix[i]=='-') && postfix[top]!='*' && postfix[top]!='/')
					{
						y=infix[i];
						push(y);
					}
					else if(infix[i]=='/' || infix[i]=='*')
					{
						y=infix[i];
						push(y);
					}
					
					else if((infix[i]=='+' || infix[i]=='-' )&& (postfix[top]=='/' || postfix[top]=='*'))
					{
						y=infix[i];
						for(int j=top;j>-1;j--)
						{
							z=postfix[j];
							pop(z);
						}
						push(y);
					}
				}
				
				else
				{
					cout<<"enter valid expression";	 
					break;
				} 
				
			}
		}
};

int main()
{
	Stack s;
	s.accept();
	cout<<"your postfix expression:";
	s.check();
	for(int j=top;j>-1;j--)
	{
		int z;
		z=postfix[j];
		s.pop(z);
	}
	return 0;
}


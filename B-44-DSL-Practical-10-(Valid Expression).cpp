/*In any language program mostly syntax error occurs due to unbalancing delimiter such as 
(),{},[]. Write C++ program using stack to check whether given expression is well 
parenthesized or not.*/


// SIMRAN SAH
// B-44


#include<iostream>
#include<string.h>
using namespace std;
class Stack
{
	private:
		int top=-1;
		int len;
		char stk[50],checkstk[50];
	public:
		void accept()
		{
			cout<<"Enter the expression : ";
			cin>>stk;
		}
		void push(char x)
		{
			top++;
			checkstk[top]=x;
		}
		void pop()
		{
			top--;
		}
		void check()
		{
			len=strlen(stk);
			int y;
			for(int i=0;i<len;i++)
			{
				if(stk[i]=='(' || stk[i]=='{' || stk[i]=='[' )
				{
					y=stk[i];
					push(y);
				}
				else if(stk[i]==')' && checkstk[top]=='(')
				{
					pop();
				}
				else if(stk[i]==']' && checkstk[top]=='[')
				{
					pop();
				}
				else if(stk[i]=='}' && checkstk[top]=='{')
				{
					pop();
				}
				else if(stk[i]==')' && checkstk[top]!='(')
				{
					pop();
					break;
				}
				else if(stk[i]==']' && checkstk[top]!='[')
				{
					pop();
					break;
				}
				else if(stk[i]=='}' && checkstk[top]!='{')
				{
					pop();
					break;
				}
			}
			if (top==-1)
			{
				cout<<"Expression is Valid";
			}
			else
			{
				cout<<"Expression is Invalid";
			}
		}
};
int main()
{
	Stack s;
	s.accept();
	s.check();
}

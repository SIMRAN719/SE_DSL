/*A double-ended queue (deque) is a linear list in which additions and deletions may be 
made at either end. Obtain a data representation mapping a deque into a onedimensional array. 
Write C++ program to simulate deque with functions to add and  delete elements from either end of the deque.
*/

// SIMRAN SAH
// B-44

#include<iostream>
#include<string.h>
using namespace std;
const int size=5;
int front=-1;
int rear=-1;
class deque
{
	private:
		int stk[size];
		int a;
	public:
		void add_begin(int x);
		void add_last(int x);
		void del_begin();
		void del_last();
		void display();
		void choice();
		void inialize()
		{
			for(int i=0;i<size;i++)
			{
				stk[i]=0;
			}
			a=0;
		}
};
void deque::add_begin(int x)
{
	if(a==size)
	{
		cout<<"Deque is full";
	}
	else if(rear==-1 || front==-1 || a==0)
	{
		front=rear=0;
		stk[rear]=x;
		a++;
	}
	else if(stk[0]==0)
	{
		front--;
		stk[front]=x;
		a++;
	}
	else
	{
		for(int i=rear+1;i>0;i--)
		{
			stk[i]=stk[i-1];
		}
		stk[0]=x;
		rear++;
		a++;
	}
}
void deque::add_last(int x)
{
	if(a==size)
	{
		cout<<"Deque is full";
	}
	else if(rear==-1 && front==-1)
	{
		front=rear=0;
		stk[rear]=x;
		a++;
	}
	else
	{
		rear++;
		stk[rear]=x;
		a++;
	}
}
void deque::del_begin()
{
	if((front==-1 && rear==-1) ||(a==0))
	{
		cout<<"Deque is empty";
	}
	else if(front==0 && rear==0)
	{
		stk[0]=0;
		front=rear=-1;
		a--;
	}
	else
	{
		stk[front]=0;
		front++;
		a--;
	}
}
void deque::del_last()
{
	if(front==-1 || rear==-1 || a==0)
	{
		cout<<"Deque is empty";
	}
	else if(front==0 && rear==0)
	{
		stk[0]=0;
		front=rear=-1;
		a--;
	}
	else
	{
		stk[rear]=0;
		rear--;
		a--;
	}
}
void deque::display()
{
	cout<<"rear :"<<rear<<"front :"<<front<<endl;
	for(int i=0;i<size;i++)
	{
		cout<<stk[i]<<",";
	}
	cout<<endl;
}
void deque::choice()
{
	int c,t;
	cout<<"\n"<<"---MENU ---"<<"\n";
	cout<<"\n1.addition of element at the start\n2.addition of element at the end";
	cout<<"\n3.deletion of element at the start \n4.deletion of element at the end\n5.display\n6.exit\n";
	cout<<"\nEnter your choice : ";
	cin>>c;
	switch(c)
	{
		case 1:
			cout<<"Enter element :";
			cin>>t;
			add_begin(t);
			choice();
			break;
		case 2:
			cout<<"Enter element :";
			cin>>t;
			add_last(t);
			choice();
			break;
		case 3:
			del_begin();
			choice();
			break;
		case 4:
			del_last();
			choice();
			break;
		case 5:
			display();
			choice();
			break;
		case 6:
			cout<<"\n***thank you for using the program***\n";
		default:
			cout<<"Enter valid entry";
			choice();
			break;
	}
}
int main()
{
	deque d;
	d.inialize();
	d.choice();

}

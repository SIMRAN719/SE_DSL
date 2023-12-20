/*Queues are frequently used in computer programming, and a typical example is the 
creation of a job queue by an operating system. If the operating system does not use 
priorities, then the jobs are processed in the order they enter the system. Write C++ 
program for simulating job queue. Write functions to add job and delete job from queue.
*/

//SIMRAN SAH
//B-44

#include<iostream>
#include<string.h>
#include<vector>
using namespace std;
int rear=-1;
int front=-1;
class queue
{
	private:	
		string a[20][30];
		int n;
	public:
		void accept()
		{
			cout<<"Enter the number of jobs to be added in the list : ";
			cin>>n;
			front=0;
			rear=0;
			for(int i=0;i<n;i++)
			{
				cout<<"enter the  "<<i+1<<"  job title : ";
				cin>>a[i][30];
				rear++;
			}
		}
		void add()
		{
			if(rear==19)
			{
				cout<<"\nqueue is full\n";
			}
			else
			{
				char ch;              
				do{
					cout<<"enter the job title : ";
					cin>>a[rear][30];
					rear++;
					cout<<"do you want to continue?";
					cout<<"enter choice(y=yes/n=no) : ";
					cin>>ch;
				}while(ch=='y'||ch=='Y');
			}
			
		}
		void del()
		{
			if(front==-1||rear==-1)
			{
				cout<<"queue is empty ";
			}
			else
			{
				for(int i=0;i<rear;i++)
				{
					a[i][30]=a[i+1][30];
				}
				rear--;
			}
		}
		void display()
		{
			cout<<"\n--elements in the queue--\n";
			for(int i=0;i<rear;i++)
			{
				cout<<a[i][30]<<"  ";
			}
			cout<<"\n";
		}
		void choice()
		{
			int c;
			cout<<"\n"<<"---MENU FOR JOBS---"<<"\n";
			cout<<"\n1.addition\n2.deletion\n3.display\n4.exit\n";
			cout<<"\nenter your choice : ";
			cin>>c;
			switch(c)
			{
				case 1:
					add();
					choice();
					break;
				case 2:
					del();
					choice();
					break;
				case 3:
					display();
					choice();
					break;
				case 4:
					cout<<"\n***thank you for using the program***\n";
			}
		}
};
int main()
{
	queue a;
	a.accept();
	a.choice();
	return 0;
}

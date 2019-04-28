#include <iostream>

using namespace std;

struct node {
	int data;
	node *next;
};

class LinkedList {
private:
	node* head, *tail; //2 nodes pointers
public:
	LinkedList() {
		head = NULL; //constructors
		tail = NULL;
	}

	void addNode(int n) {
		node *tmp = new node;
		tmp->data = n;
		tmp->next = NULL;
		if (head == NULL) {
			head = tmp;
			tail = tmp;
		}
		else {
			tail->next = tmp;
			tail = tail->next;
		}

	}
	node* gethead()
	{
		return head;
	}

	static void display(node *head)
	{
		if (head == NULL)
		{
			cout << "NULL" << endl;
		}
		else
		{
			cout << head->data << endl;
			display(head->next);
		}
	}

	static void concatenate(node *a, node *b)
	{
		if (a != NULL && b != NULL)
		{
			if (a->next == NULL)
				a->next = b;
			else
				concatenate(a->next, b);
		}
		else
		{
			cout << "Either a or b is NULL\n";
		}
	}
};

int main() {
	LinkedList a;
	a.addNode(1);
	a.addNode(2);
	LinkedList b;
	a.addNode(3);
	a.addNode(4);
	std::cin.get();
	LinkedList::concatenate(a.gethead(), b.gethead());
	LinkedList::display(a.gethead());
}
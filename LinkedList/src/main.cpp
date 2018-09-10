#include "../include/linkedlist.hpp"

int main(){
	LinkedList<int> l ;
	l.insertBeginning(2);
	l.insertBeginning(3);
	l.insertBeginning(4);
	//l.removeEnd();
	l.swap(4,3);
	l.print();
	return 0;
}

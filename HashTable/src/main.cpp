#include "../include/hashtable.hpp"

int main(){
	chainedHashtable<int> s1(5);
	s1.insert(2);
	s1.insert(-80);
	s1.insert(1000);
	s1.insert(7);
	s1.insert(13);
	s1.insert(11);
	s1.insert(19);
	s1.insert(5);
	s1.insert(12);
	//cout << "Encontrou: " << s1.findEl(-100) << endl;
	s1.del(7);
	//cout << "Tam: " << s1.size() << endl;
	return 0;
}
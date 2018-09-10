#ifndef STACK_
#define STACK_

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include<vector>
using std::vector;

#include<list>
using std::list;

#include <algorithm>
using std::find;

#include <stdlib.h>

template<class T>
class chainedHashtable{
	private:
		vector<list<T>> hashvector;
		unsigned _size;
		//
	public:
		chainedHashtable(unsigned size):hashvector(size),_size(0){}
		~chainedHashtable(){
		}
		unsigned size(){ //
			return _size;
		}
		bool empty(){
			return !size();
		}
		unsigned capacity(){
			return hashvector.size();
		}
		unsigned hash(const T & value){
			return value >> 1; //Desloca 1 bit da esquerda
		}
		void insert(const T & value){
			unsigned idx = hash(value)%capacity();
			hashvector[idx].push_back(value);
			_size+=1;
		}

		void del(const T & value){
			unsigned idx = hash(value)%capacity();
			auto pos = find(hashvector[idx].begin(),hashvector[idx].end(),value);
			if(pos != hashvector[idx].end()){
				hashvector[idx].erase(pos);
				_size-=1;
				cout << value << " deletado com sucesso." << endl;
			}
			else{
				cout << "Elemento " << value << " não encontrado." << endl;
				exit(EXIT_FAILURE);
			} 
		}

		bool findEl(const T & value){
			unsigned idx = hash(value)%capacity();
			const auto & pos = find(hashvector[idx].begin(),hashvector[idx].end(),value);
			return pos != hashvector[idx].end();
		}
};
#endif

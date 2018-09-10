#ifndef LLIST_
#define LLIST_

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <stdlib.h>

template<class T>
class LinkedList{
	private:
		struct Node{
			public:
				T chave;
				Node * next;
				Node * prev;
				Node () = default;
				Node(T _chave):chave(_chave),next(nullptr),prev(nullptr){};

		};
		Node * inicio;
		Node * fim;
		unsigned tam;
	public:
		LinkedList(){
			this->inicio = new Node;
			this->fim = new Node;
			this->inicio->next = this->fim;
			this->fim->prev = this->inicio;
			this->tam = 0;
		}
		~LinkedList(){
			Node * it = inicio->next;
			while(it != this->fim){
				it = it->next;
				delete it->prev;
			}
			delete this->inicio;
			delete this->fim;
		}
		unsigned size(){
			return tam;
		}
		bool empty(){
			return this->tam == 0;
		}
		void insertBeginning(T chave_){
			Node * novo = new Node(chave_);
			if(empty()){
				novo->next = novo;
				novo->prev = novo;
				this->fim = novo;
				this->inicio = novo;
			}
			else{
				novo->next = this->inicio;
				novo->prev = this->fim;
				this->fim->next = novo;
				this->inicio->prev = novo;
				this->inicio = novo;
			}
			tam+=1;

		}
		void removeEnd(){
			if(empty()){
				cout << "List vazia" << endl;
				 exit(EXIT_FAILURE);
			}
			else if(this->tam == 1){
				Node * tmp = this->fim;
				this->fim = nullptr;
				this->inicio = nullptr;
				delete tmp;
			}
			else{
				Node * tmp = this->fim;
				this->fim->prev->next = this->inicio;
				this->fim =this->fim->prev;
				this->inicio->prev = this->fim;
				delete tmp;
			}
			tam-=1;
		}
		void print(){
			if(empty()){
				cout << "Lista vazia" << endl;
				 exit(EXIT_FAILURE);
			} 
			Node * it = this->inicio;
			do{
				cout << it->chave << endl;
				it = it->next;
			}while(it!= this->inicio);
		}
		void swap(T a, T b){
			if(empty()){
				cout << "Lista vazia" << endl;
				 exit(EXIT_FAILURE);
			}
			else{
				if(a == b){
					 exit(EXIT_FAILURE);
				}
				Node * x = this->inicio;
				Node * y = this->inicio;
				bool xx = 0, yy = 0;
				do{
					if(x->chave == a){
						xx = 1;
						break;
					}
					x = x->next;
				}while(x!=this->inicio);

				do{
					if(y->chave == b){
						yy = 1;
						break;
					}
					y = y->next;
				}while(y!=this->inicio);
				if(xx && yy){
					T tmp = x->chave;
					x->chave = y->chave;
					y->chave = tmp;
				}
				else{
					cout << "Um dos elementos não foi encontrado" << endl;
					 exit(EXIT_FAILURE);
				}
			}
		}
};
#endif

#include <iostream>
using namespace std;

template <typename T> class CircularList {
    int front = -1;
    int rear = -1;
    int size;
    T* arr;

    CircularList(int n){
        size = n;
        arr = new T[n];
    }
    ~CircularList(){
        delete[] arr;
    }

    void pushBack(T data){

        if ((rear + 1) % size == front){
            cout << "Error: Lista llena. No se puede agregar el elemento.\n";
        }

        else if (front == -1){
            front = 0;
            rear = 0;
            arr[rear] = data;
        }       

        else{
            rear = (rear + 1) % size;
            arr[rear] = data;
        }
    }

    void pushFront(T data){
        if ((rear + 1) % size == front){
            cout << "Error: Lista llena. No se puede agregar el elemento.\n";
        }

        else if (front == -1){
            front = 0;
            rear = 0;
            arr[rear] = data;
        }       

        else{
            front = (front + 1) % size;
            arr[front] = data;
        }
    }

    void popBack(){
        if (front == -1){
            cout << "Error: Lista vacia. No se puede eliminar el elemento.\n";
        }

        else if (front == rear){
            front = -1;
            rear = -1;
        }       

        else{
            rear = (rear-1) % size;
        }
    }

    void popFront(){
        if (front == -1){
            cout << "Error: Lista vacia. No se puede eliminar el elemento.\n";
        }

        else if (front == rear){
            front = -1;
            rear = -1;
        }       

        else{
            front = (front + 1) % size;
        }
    }

    void printf(){
        if (rear >= front){
            cout << "Elementos en el arreglo: ["

            for (int i = front; i < rear + 1, i++){
                if (i != rear) cout << arr[i] <<" ";
                else cout << arr[i] <<"";
            }
            cout << "]";
        }

        else {
            cout <<"Elementos en el arreglo: [";

            for (int i = front;  i < size, i++){
                if (i != rear) cout << arr[i] <<" ";
            }
            for (int j = 0;  i < rear + 1, i++){
                if (i != rear) cout << arr[i] <<" ";
                else cout << arr[i] <<"";
            }
            cout << "]";
        }
};

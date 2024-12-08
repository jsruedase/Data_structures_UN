#include <iostream>
using namespace std;

template <typename T>
class CircularList {
    int front = -1;
    int rear = -1;
    int size;
    T* arr;

public:
    CircularList(int n) {
        size = n;
        arr = new T[n];
    }

    ~CircularList() {
        delete[] arr;
    }

    void pushBack(T data) {
        if ((rear + 1) % size == front) {
            cout << "Error: Lista llena. No se puede agregar el elemento.\n";
        } else if (front == -1) {
            front = 0;
            rear = 0;
            arr[rear] = data;
        } else {
            rear = (rear + 1) % size;
            arr[rear] = data;
        }
    }

    void pushFront(T data) {
        if ((rear + 1) % size == front) {
            cout << "Error: Lista llena. No se puede agregar el elemento.\n";
        } else if (front == -1) {
            front = 0;
            rear = 0;
            arr[rear] = data;
        } else {
            front = (front - 1 + size) % size;  // Decremento circular
            arr[front] = data;
        }
    }

    void popBack() {
        if (front == -1) {
            cout << "Error: Lista vacía. No se puede eliminar el elemento.\n";
        } else if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            rear = (rear - 1 + size) % size;  // Decremento circular
        }
    }

    void popFront() {
        if (front == -1) {
            cout << "Error: Lista vacía. No se puede eliminar el elemento.\n";
        } else if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % size;  // Incremento circular
        }
    }

    void print() {
        if (front == -1) {
            cout << "La lista está vacía.\n";
            return;
        }

        cout << "Elementos en el arreglo: [";
        int i = front;
        while (true) {
            cout << arr[i];
            if (i == rear) break;
            cout << " ";
            i = (i + 1) % size;
        }
        cout << "]\n";
    }
};

int main() {
    CircularList<int>* lst = new CircularList<int>(3);
    lst->pushBack(1);
    lst->pushBack(2);
    lst->print();  // [1 2]
    lst->pushBack(3);  // Error: Lista llena
    lst->popFront();
    lst->print();  // [2]
    lst->pushBack(3);
    lst->print();  // [2 3]
    lst->pushFront(0);
    lst->print();  // [0 2 3]
    delete lst;
    return 0;
}

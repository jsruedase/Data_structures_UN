#include <iostream>
#include <string>

using namespace std; 

class List {
    public:
    int lst_elem_index = -1;
    int size;
    int* array;
    List(int n){
        size = n;
        array = new int[size];
    }

    ~List() {
        delete[] array;  // Liberar memoria en el destructor
    }

    void addLast(int elem){
        if (lst_elem_index == size-1){
            cout << "Error: Lista llena. No se puede agregar el elemento.\n";
        }
        else {
            array[lst_elem_index + 1] = elem;
            lst_elem_index += 1;
        }
    }
    void removeLast(){
        if (lst_elem_index == -1){
            cout << "Error: Lista vacia. No se puede eliminar el elemento.\n";
        }
        else {
            lst_elem_index -= 1;
        }
    }

    void print() {
        cout << "Elementos en el arreglo: [";
        for (int i = 0; i <= lst_elem_index; i++) {
            cout << array[i];
            if (i < lst_elem_index) cout << " ";
        }
        cout << "]\n";
    }

    void addFirst(int elem){
        if (lst_elem_index == size-1){
            cout << "Error: Lista llena. No se puede agregar el elemento.\n";
        }
        else {
            for (int i = 0; i < lst_elem_index + 1; i++){
                array[lst_elem_index + 1 - i] = array[lst_elem_index - i];
            }
            array[0] = elem;
            lst_elem_index += 1;
        }
    }
    
    void removeFirst(){
        if (lst_elem_index == -1){
            cout << "Error: Lista vacia. No se puede eliminar el elemento.\n";
        }
        else {
            if (lst_elem_index != size){
                for (int i = 0; i < lst_elem_index; i++){
                    array[i] = array[i+1];
                }
            }
            else {
                for (int i = 0; i < lst_elem_index-1; i++){
                    array[i] = array[i+1];
                }   
            }
            lst_elem_index -= 1;
        }
    } 
};

int main(){
    int size;
    cout << "Size: ";
    cin >> size;
    List lst = List(size); 
    bool running = true;
    int data;
    while (cin >> data)
    {
        if (data == 1){
            lst.print();
        } 
        else if (data == 2) {
            int elem;
            cout << "Number: ";
            cin >> elem;
            lst.addLast(elem);
        }
        else if (data == 3) {
            lst.removeLast();
        }
        else if (data == 4) {
            int elem;
            cout << "Number: ";
            cin >> elem;
            lst.addFirst(elem);
        }
        else if (data == 5) {
            lst.removeFirst();
        }
        else running = false;
    }
}

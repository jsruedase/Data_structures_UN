#include <iostream>
using namespace std;

class Node{
    private:
    int val;
    Node* next;

    public:
    Node(int key){
        val = key;
        next = nullptr;
    }
    
    int getKey(){
        return val; 
    }

    Node* getNext(){
        return next;
    }

    void setKey(int key){
        val = key;
    }

    void setNext(Node* n){
        next = n;
    }
};
 
class LinkedList{
    Node* head;

    public:
    LinkedList(){
        head = nullptr;
    }

    ~LinkedList(){
        Node* next = head;
        while (next->getNext() != nullptr){
            Node* prev = next;
            next = next->getNext();
            delete prev;
        }
    }
    
    void pushFront(int val){
        Node* newNode = new Node(val); 
        newNode->setNext(head);  
        head = newNode;
    }
    
    void pushBack(int val){
        Node* newNode = new Node(val);
        Node* next = head;
        if (head == nullptr){
            head = newNode;
            return;
        }
        while (next->getNext() != nullptr){
            next = next->getNext();
        }
        next->setNext(newNode);
    }
    
    void popFront(){
        if (head == nullptr){
            cout << "Error: Lista vacia. No se puede eliminar el elemento." << endl;
            return;
        }
        Node* next = head;
        head = next->getNext();
        delete next;
    }
    
    void popBack(){
        if (head == nullptr){ 
            cout << "Error: Lista vacia. No se puede eliminar el elemento." << endl;
            return;
        }
        else if (head->getNext() == nullptr){
            delete head;
            head = nullptr;
            return;
        }
        Node* next = head;
        Node* prev = nullptr;
        while (next->getNext() != nullptr){
            prev = next;
            next = next->getNext();
        }
        prev->setNext(nullptr);
        delete next;
    }

    void print(){
        cout << "Elementos en la lista enlazada: [";
        Node* next = head;
        while (next != nullptr){
            if (next->getNext() == nullptr){
                cout <<next->getKey();
                break;
            }
            else {
                cout <<next->getKey()<<" ";
            }
            next = next->getNext();
        }
        cout <<"]"<<endl;
    }
};

int main(){
    LinkedList* lista = new LinkedList();
    int data;
    while (cin >> data){
            if (data == 1){
                lista->print();
            }

            else if (data == 2){
                int val;
                cin >> val;
                lista->pushBack(val);
            }

            else if (data == 3){
                lista->popBack();
            }

            else if (data == 4){
                int val;
                cin >> val;
                lista->pushFront(val);
            }

            else if (data == 5){
                lista->popFront();
            }
    }
    return 0;
}

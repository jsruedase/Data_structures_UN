#include <iostream>
#include <chrono>
using namespace std;

template <typename T> 
class Node{
    private:
    T val;
    Node<T>* next;

    public:
    Node(T key){
        val = key;
        next = nullptr;
    }
    
    T getKey(){
        return val; 
    }

    Node<T>* getNext(){
        return next;
    }

    void setKey(T key){
        val = key;
    }

    void setNext(Node<T>* n){
        next = n;
    }
};

template <typename T> 
class DoubleNode{
    private:
    T val;
    DoubleNode<T>* next;
    DoubleNode<T>* prev;

    public:
    DoubleNode(T key){
        val = key;
        next = nullptr;
    }
    
    T getKey(){
        return val; 
    }

    DoubleNode<T>* getNext(){
        return next;
    }

    DoubleNode<T>* getPrev(){
        return prev;
    }

    void setKey(T key){
        val = key;
    }

    void setNext(DoubleNode<T>* n){
        next = n;
    }

    void setPrev(DoubleNode<T>* p){
        prev = p;
    }
};


//Interface(abstract class) for the List.
template <typename T> class List {
    public:
    virtual void pushFront(T val) = 0;
    virtual void pushBack(T val) = 0;
    virtual void popFront() = 0;
    virtual void popBack() = 0;
    virtual T topFront() = 0;
    virtual T topBack() = 0;
    virtual T find(T key) = 0;
    virtual void erase(T key) = 0;
    virtual bool isEmpty() = 0;
    virtual void addBefore(T key, T newKey) = 0;
    virtual void addAfter(T key, T newKey) = 0;
    virtual void print() = 0;
};

template <typename T> class LinkedList : public List<T>{
    Node<T>* head;

    public:
    LinkedList(){
        head = nullptr;
    }

    ~LinkedList(){
        Node<T>* next = head;
        while (next->getNext() != nullptr){
            Node<T>* prev = next;
            next = next->getNext();
            delete prev;
        }
    }
    
    void pushFront(T val){
        Node<T>* newNode = new Node<T>(val); 
        newNode->setNext(head);  
        head = newNode;
    }
    
    void pushBack(T val){
        Node<T>* newNode = new Node<T>(val);
        Node<T>* next = head;
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
        Node<T>* next = head;
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
        Node<T>* next = head;
        Node<T>* prev = nullptr;
        while (next->getNext() != nullptr){
            prev = next;
            next = next->getNext();
        }
        prev->setNext(nullptr);
        delete next;
    }

    T topFront(){
        return head->getKey();
    }

    T topBack(){
        Node<T>* next = head;
        while (next->getNext() != nullptr){
            next = next->getNext();
        }
        return next->getKey();
    }

    int find(T key){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return -1;
        }
        Node<T>* next = head;
        int i = 0;
        while (next->getNext() != nullptr){
            if (next->getKey() == key){
                return i;
            }
            next = next->getNext();
            i++;
        }
        return -1;
    }

    void erase(T key){
        if (head == nullptr){
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        Node<T>* next = head;
        Node<T>* prev = nullptr;
        for (int i = 0; i < n; i++){
            prev = next;
            next = next->getNext();
        }
        prev->setNext(next->getNext());
        delete next;
    }

    bool isEmpty(){
        return head == nullptr;
    }   

    void addBefore(T key, T newKey){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        Node<T>* next = head;
        Node<T>* prev = nullptr;
        for (int i = 0; i < n; i++){
            prev = next;
            next = next->getNext();
        }
        Node<T>* newNode = new Node<T>(newKey);
        prev->setNext(newNode);
        newNode->setNext(next);
    }

    void addAfter(T key, T newKey){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        Node<T>* next = head;
        for (int i = 0; i < n; i++){
            next = next->getNext();
        }
        Node<T>* newNode = new Node<T>(newKey);
        newNode->setNext(next->getNext());
        next->setNext(newNode);
    }

    void print(){
        cout << "Elementos en la lista enlazada: [";
        Node<T>* next = head;
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

 
template <typename T> class TailedLinkedList: public List<T>{
    Node<T>* head;
    Node<T>* tail;

    public:
    TailedLinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    ~TailedLinkedList(){
        Node<T>* next = head;
        while (next->getNext() != nullptr){
            Node<T>* prev = next;
            next = next->getNext();
            delete prev;
        }
    }
    
    void pushFront(T val){
        Node<T>* newNode = new Node<T>(val); 
        newNode->setNext(head);  
        head = newNode;
        if (tail == nullptr){
            tail = head;        
        }
    }
    
    void pushBack(T val){
        Node<T>* newNode = new Node<T>(val);
        if (head == nullptr){
            head = newNode;
            tail = newNode;
            return;
        }
        tail->setNext(newNode);
        tail = newNode;
    }
    
    void popFront(){
        if (head == nullptr){
            cout << "Error: Lista vacia. No se puede eliminar el elemento." << endl;
            return;
        }
        Node<T>* next = head;
        head = next->getNext();
        if (head == nullptr){
            tail = nullptr;
        }
        delete next;
    }
    
    void popBack(){
        if (head == nullptr){ 
            cout << "Error: Lista vacia. No se puede eliminar el elemento." << endl;
            return;
        }
        else if (head == tail){
            head = nullptr;
            tail = nullptr;
            return;
        }
        Node<T>* next = head;
        Node<T>* prev = nullptr;
        while (next->getNext() != nullptr){
            prev = next;
            next = next->getNext();
        }
        prev->setNext(nullptr);
        tail = prev;
        delete next;
    }

    T topFront(){
        return head->getKey();
    }

    T topBack(){
        return tail->getKey();
    }

    int find(T key){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return -1;
        }
        Node<T>* next = head;
        int i = 0;
        while (next->getNext() != nullptr){
            if (next->getKey() == key){
                return i;
            }
            next = next->getNext();
            i++;
        }
        return -1;
    }

    void erase(T key){
        if (head == nullptr){
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        Node<T>* next = head;
        Node<T>* prev = nullptr;
        for (int i = 0; i < n; i++){
            prev = next;
            next = next->getNext();
        }
        prev->setNext(next->getNext());
        delete next;
    }   

    bool isEmpty(){
        return head == nullptr;
    }

    void addBefore(T key, T newKey){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        Node<T>* next = head;
        Node<T>* prev = nullptr;
        for (int i = 0; i < n; i++){
            prev = next;
            next = next->getNext();
        }
        Node<T>* newNode = new Node<T>(newKey);
        prev->setNext(newNode);
        newNode->setNext(next);
    }

    void addAfter(T key, T newKey){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        Node<T>* next = head;
        for (int i = 0; i < n; i++){
            next = next->getNext();
        }
        Node<T>* newNode = new Node<T>(newKey);
        newNode->setNext(next->getNext());
        next->setNext(newNode);
    }

    void print(){
        cout << "Elementos en la lista enlazada: [";
        Node<T>* next = head;
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

template <typename T> class TailedDoublyLinkedList: public List<T>{
    DoubleNode<T>* head;
    DoubleNode<T>* tail;

    public:
    TailedDoublyLinkedList(){
        head = nullptr;
        tail = nullptr;
    }

    ~TailedDoublyLinkedList(){
        DoubleNode<T>* next = head;
        while (next->getNext() != nullptr){
            DoubleNode<T>* prev = next;
            next = next->getNext();
            delete prev;
        }
    }
    
    void pushFront(T val){
        DoubleNode<T>* newNode = new DoubleNode<T>(val); 
        newNode->setNext(head);
        if (head != nullptr){
            head->setPrev(newNode);
        }
        head = newNode;
        if (tail == nullptr){
            tail = head;        
        }
    }
    
    void pushBack(T val){
        DoubleNode<T>* newNode = new DoubleNode<T>(val);
        if (head == nullptr){
            head = newNode;
            tail = newNode;
            return;
        }
        tail->setNext(newNode);
        newNode->setPrev(tail);
        tail = newNode;
    }
    
    void popFront(){
        if (head == nullptr){
            cout << "Error: Lista vacia. No se puede eliminar el elemento." << endl;
            return;
        }
        DoubleNode<T>* next = head;
        head = next->getNext();
        if (head == nullptr){
            tail = nullptr;
        }
        delete next;
    }
    
    void popBack(){
        if (head == nullptr){ 
            cout << "Error: Lista vacia. No se puede eliminar el elemento." << endl;
            return;
        }
        else if (head == tail){
            head = nullptr;
            tail = nullptr;
            return;
        }
        DoubleNode<T>* prev = tail->getPrev();
        prev->setNext(nullptr);
        delete tail;
        tail = prev;
    }

    T topFront(){
        return head->getKey();
    }

    T topBack(){
        return tail->getKey();
    }

    int find(T key){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return -1;
        }
        DoubleNode<T>* next = head;
        int i = 0;
        while (next->getNext() != nullptr){
            if (next->getKey() == key){
                return i;
            }
            next = next->getNext();
            i++;
        }
        return -1;
    }

    void erase(T key){
        if (head == nullptr){
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        DoubleNode<T>* next = head;
        DoubleNode<T>* prev = nullptr;
        for (int i = 0; i < n; i++){
            prev = next;
            next = next->getNext();
        }
        prev->setNext(next->getNext());
        delete next;
    }

    bool isEmpty(){
        return head == nullptr;
    }

    void addBefore(T key, T newKey){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        DoubleNode<T>* next = head;
        DoubleNode<T>* prev = nullptr;
        for (int i = 0; i < n; i++){
            prev = next;
            next = next->getNext();
        }
        DoubleNode<T>* newNode = new DoubleNode<T>(newKey);
        prev->setNext(newNode);
        newNode->setNext(next);
    }

    void addAfter(T key, T newKey){
        if (head == nullptr){
            cout << "Error: Elemento no encontrado." << endl;
            return;
        }
        int n = find(key);
        if (n == -1){
            cout << "Error: Elemento no encontrado." << endl;
        }
        DoubleNode<T>* next = head;
        for (int i = 0; i < n; i++){
            next = next->getNext();
        }
        DoubleNode<T>* newNode = new DoubleNode<T>(newKey);
        newNode->setNext(next->getNext());
        next->setNext(newNode);
    }

    void print(){
        cout << "Elementos en la lista enlazada: [";
        DoubleNode<T>* next = head;
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

// int main(){
//     TailedLinkedList* lista = new TailedLinkedList();
//     int data;
//     while (cin >> data){
//             if (data == 1){
//                 lista->print();
//             }

//             else if (data == 2){
//                 int val;
//                 cin >> val;
//                 lista->pushBack(val);
//             }

//             else if (data == 3){
//                 lista->popBack();
//             }

//             else if (data == 4){
//                 int val;
//                 cin >> val;
//                 lista->pushFront(val);
//             }

//             else if (data == 5){
//                 lista->popFront();
//             }
//     }
//     delete lista;
//     return 0;
// }

int main(){
    LinkedList<int>* lista = new LinkedList<int>();
    int sizes[5] = {100, 1000, 10000, 50000, 100000};
    double time_per_size[5];
    double time_per_size_pop[5];

    for (int i = 0; i < 5; i++){
        auto start = chrono::high_resolution_clock::now();
        for (int j = 0; j < sizes[i]; j++){
            lista->pushFront(j);
        }
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>((end - start));
        time_per_size[i] = (double)duration.count() / sizes[i];
        //cout << "Time for size " << sizes[i] << ": " << time_per_size[i] << " microseconds" << endl;

        start = chrono::high_resolution_clock::now();
        for (int j = 0; j < sizes[i]; j++){
            lista->popFront();
        }
        end = chrono::high_resolution_clock::now();
        duration = chrono::duration_cast<chrono::microseconds>((end - start));
        time_per_size_pop[i] = (double)duration.count()/ sizes[i];
        cout << "Time for pop size " << sizes[i] << ": " << time_per_size_pop[i] << " microseconds" << endl;
    }
    cout << "Time per size: [" << time_per_size[0] << ", " << time_per_size[1] << ", " << time_per_size[2] << ", " << time_per_size[3] << ", " << time_per_size[4] <<"]" << endl;
    cout << "Time per size pop: [" << time_per_size_pop[0] << ", " << time_per_size_pop[1] << ", " << time_per_size_pop[2] << ", " << time_per_size_pop[3] << ", " << time_per_size_pop[4]<< "]" << endl; 
}

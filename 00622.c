// https://leetcode.com/problems/design-circular-queue

typedef struct {
    int *queue;
    int size;
    int rear;  // fim da fila (quem sai)
    int front; // entrada da fila (quem entra)
    // leetcode entende ao contrário, por isso funções rear e front estão invertidas.
} MyCircularQueue;


MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *q = (MyCircularQueue *) malloc(sizeof(MyCircularQueue));
    q->queue = (int *) malloc(k*sizeof(int));
    q->size = k;
    q->rear = -1;
    q->front = -1;
    return q;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if(obj->rear == -1){ // fila vazia
        obj->queue[0] = value;
        obj->rear = 0;
        obj->front = (obj->size > 1)? 1 : 0; // apenas para tratar caso de tam. fila = 1
        return true;
    }
    else if(obj->rear == obj->front) // fila cheia
        return false;
    else{ // inserção normal
        obj->queue[obj->front] = value;
        obj->front = (obj->front+1)%obj->size;
        return true;
    }
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if(obj->rear == -1)
        return false;

    obj->rear = (obj->rear+1)%obj->size;
    if(obj->rear == obj->front){ // ficou vazia
        obj->rear = -1;
        obj->front = -1;
    }
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    return (obj->rear == -1)? -1 : obj->queue[obj->rear];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    return (obj->rear == -1)? -1 : obj->queue[(obj->front-1+obj->size)%obj->size];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return (obj->rear == -1);
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return (obj->rear != -1 && obj->rear == obj->front);
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->queue);
    free(obj);
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 
 * bool param_2 = myCircularQueueDeQueue(obj);
 
 * int param_3 = myCircularQueueFront(obj);
 
 * int param_4 = myCircularQueueRear(obj);
 
 * bool param_5 = myCircularQueueIsEmpty(obj);
 
 * bool param_6 = myCircularQueueIsFull(obj);
 
 * myCircularQueueFree(obj);
*/

// https://leetcode.com/problems/min-stack/

typedef int KEYTYPE;

// nó da pilha
typedef struct _StackNode{
	KEYTYPE key;
	int min; // diz quem é o minimo da pilha até ESSE nó.
	struct _StackNode *next;
} StackNode;

// estrutura da pilha
typedef struct _MinStack{
    StackNode *head;
} MinStack;

MinStack* minStackCreate();
void minStackPush(MinStack* obj, int val);
void minStackPop(MinStack* obj);
int minStackTop(MinStack* obj);
int minStackGetMin(MinStack* obj);
void minStackFree(MinStack* obj);

MinStack* minStackCreate() {
    MinStack *stack = (MinStack *) malloc(sizeof(MinStack));
    if(stack == NULL) // falha aloc
    	exit(1);
    
    stack->head = NULL;
    
    return stack;
}

void minStackPush(MinStack* obj, int val) {
	StackNode *newNode = (StackNode *) malloc(sizeof(StackNode));
	newNode->key = val;
	
	if(newNode == NULL) 
		exit(1);
	
	if(obj->head == NULL){
		obj->head = newNode;
		newNode->next = NULL;
		newNode->min = val;
	}
	else{
		newNode->next = obj->head;
		if(val < obj->head->min)
			newNode->min = val;
		else
			newNode->min = obj->head->min;
		
		obj->head = newNode;
	}
}

void minStackPop(MinStack* obj) {
    StackNode *remove = obj->head;
	if(remove == NULL)
    	exit(2); // underflow
    
    obj->head = remove->next;
    free(remove);
}

int minStackTop(MinStack* obj) {
    if(obj->head == NULL)
    	exit(2);
    
    return obj->head->key;
}

int minStackGetMin(MinStack* obj) {
    if(obj->head == NULL)
    	exit(2);
    
    return obj->head->min;
}

void minStackFree(MinStack* obj) {
	if(obj == NULL || obj->head == NULL)
		return;
	
    StackNode *current = obj->head;
    while(current != NULL){
		StackNode *remove = current;
		current = current->next;
		free(remove);
	}
}

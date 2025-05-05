// https://leetcode.com/problems/zigzag-conversion/

// minha abordagem usando listas
// feito inicialmente em python, fiz em C para comparar runtime

typedef char KEYTYPE;

typedef struct _ListNode{
	KEYTYPE key;
	struct _ListNode *next;
} ListNode;

typedef struct{
	ListNode *head;
	ListNode *end;
} List;

void init(List *list){
	list->head = NULL;
	list->end = NULL;
}

void insertAtLast(List *list, KEYTYPE value){
	ListNode *head = list->head;
	
	ListNode *newNode = (ListNode *) malloc(sizeof(ListNode));
	newNode->key = value;
	newNode->next = NULL;
	
	if(head == NULL)
		list->head = list->end = newNode;
	else{
		list->end->next = newNode;
		list->end = newNode;
	}
}

void freeList(List *list){
	ListNode *current = list->head;
	while(current != NULL){
		ListNode *remove = current;
		current = current->next;
		free(remove);
	}
	list->head = NULL;
	list->end = NULL;
}

char* convert(char* s, int numRows) {
    int lenght = strlen(s);
    if(lenght <= numRows || numRows == 1)
    	return strdup(s);
    	
    List *rowList = (List *) malloc(numRows * sizeof(List));
    for(int i = 0; i < numRows; ++i)
    	init(rowList+i);
    insertAtLast(rowList, s[0]);
    
	int i = 1; 
    
    while(true){
		int j;
		for(j = 1; j < numRows; ++j){
			insertAtLast(rowList+j, s[i++]);
			if(i == lenght)
                goto ENDLOOP;
		}
		for(j-=2; j >= 0; --j){
			insertAtLast(rowList+j, s[i++]);
			if(i == lenght)
                goto ENDLOOP;
		}
	}
	ENDLOOP: 
	
    char *converted_str = (char *) malloc(lenght+1);
	converted_str[lenght] = '\0';
    
    for(int j = 0, i = 0; j < numRows; ++j){
		ListNode *current = rowList[j].head;
		while(current != NULL){
			converted_str[i++] = current->key;
			current = current->next;
		}
		freeList(rowList+j); // (*)
	}
	
    free(rowList); 
    
    return converted_str;
}

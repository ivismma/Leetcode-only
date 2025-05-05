// https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

struct ListNode* removeNthFromEnd(struct ListNode *head, int n){
	struct ListNode *nodes[100];
	int i = 0;
	struct ListNode* current = head;
	while(current != NULL){
		nodes[i++] = current;
		current = current->next;
	}
	if(i - n == 0){
		struct ListNode* newNode = head->next;
		free(head);
		return newNode;
	}	
	nodes[i-n-1]->next = nodes[i-n]->next;
	free(nodes[i-n]);
	return head;
}

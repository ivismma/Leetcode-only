// https://leetcode.com/problems/swap-nodes-in-pairs/

struct ListNode* swapPairs(struct ListNode* head) {
    if(head == NULL || head->next == NULL)
        return head;

    {
        struct ListNode* temp = head->next;
        head->next = temp->next;
        temp->next = head;
        head = temp;
    }
    struct ListNode* pointerToPair = head->next;
    struct ListNode* current = pointerToPair->next;

    while(current != NULL){
        struct ListNode *temp = current->next;
        if(temp == NULL) // trata caso em que nó atual está sozinho (ñ tem mais par)
            break;
        pointerToPair->next = temp;
        current->next = temp->next;
        temp->next = current;
        pointerToPair = current;
        current = pointerToPair->next;
    }

    return head;
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/

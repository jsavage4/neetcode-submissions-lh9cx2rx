/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        if (head->next == nullptr) return;
        ListNode* lastNodeFirstHalf = nullptr;
        ListNode* slow = head; 
        ListNode* fast = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            lastNodeFirstHalf = slow;
            slow = slow->next;
        }
        // If odd length, fast landed on the last node (not null)
        // so the middle node belongs to the first half
        if (fast != nullptr) {
            lastNodeFirstHalf = slow;
            slow = slow->next;
        }
        // Rever the second half
        lastNodeFirstHalf->next = nullptr;
        ListNode* prev = nullptr;
        ListNode* curr = slow;

        while (curr) {
            ListNode* currNext = curr->next;
            curr->next = prev;
            prev = curr;
            curr = currNext;
        }
        ListNode* firstHalf = head;
        ListNode* secondHalf = prev;
        while (firstHalf != nullptr and secondHalf != nullptr) {
            ListNode* nextSecondHalf = secondHalf->next;
            ListNode* nextFirstHalf = firstHalf->next;

            firstHalf->next = secondHalf;
            secondHalf->next = nextFirstHalf;

            firstHalf = nextFirstHalf;
            secondHalf = nextSecondHalf;
        }
    }
};

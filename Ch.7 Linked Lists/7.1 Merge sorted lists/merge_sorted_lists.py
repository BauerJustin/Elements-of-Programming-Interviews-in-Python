#code
def merge_sorted_lists(L1,L2):
    head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return head.next

# Linked list classes and base code
class ListNode:
    def __init__(self,data=0,next_node=None):
        self.data = data
        self.next = next_node
    
    def __str__(self):
        return str(self.data)

def print_list(LL):
    while LL:
        print(LL, end=" ")
        LL = LL.next
    print("\n")

LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(2, ListNode(4, ListNode(6)))

# Test
print_list(merge_sorted_lists(LL1, LL2))
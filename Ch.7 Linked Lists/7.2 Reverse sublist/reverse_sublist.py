#code
def reverse_sublist(L,s,f):
    dummy_head = sublist_head = ListNode(0, L)
    
    for _ in range(1,s):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(f-s):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next

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

LL = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, ListNode(28))))))

# Test
print_list(reverse_sublist(LL,2,4))
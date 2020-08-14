#code
def pivot_list(L, k):
    less = less_head = ListNode()
    equal = equal_head = ListNode()
    greater = greater_head = ListNode()
    while L:
        if L.data < k:
            less.next = L
            less = less.next
        elif L.data == k:
            equal.next = L
            equal = equal.next
        else:
            greater.next = L
            greater = greater.next
        L = L.next
    greater.next = None
    equal.next = greater_head.next
    less.next = equal_head.next
    return less_head.next

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

LL1 = ListNode(3, ListNode(2, ListNode(2, ListNode(11, ListNode(7, ListNode(5, ListNode(11)))))))

# Test
print_list(pivot_list(LL1, 7))
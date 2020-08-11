#code
def is_overlap(L1, L2):
    temp = []
    while L1:
        temp.append(L1)
        L1 = L1.next
    while L2:
        if L2 in temp:
            return L2
        L2 = L2.next
    return None

# Linked list classes and base code
class ListNode:
    def __init__(self,data=0,next_node=None):
        self.data = data
        self.next = next_node
    
    def __str__(self):
        return str(self.data)

LL1 = ListNode(11, ListNode(23))
LL2 = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, ListNode(28))))))
LL3 = ListNode(124, ListNode(35, ListNode(3, ListNode(315, ListNode(25, ListNode(58))))))
LL4 = ListNode(55, ListNode(2, LL3.next.next.next))

# Test
print(is_overlap(LL1, LL2))
print(is_overlap(LL3, LL4))
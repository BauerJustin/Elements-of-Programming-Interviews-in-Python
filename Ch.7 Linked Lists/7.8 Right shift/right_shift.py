#code
def right_shift(L, k):
    if k == 0:
        return L

    tail = L
    count = 1
    while tail.next:
        count += 1
        tail = tail.next

    tail.next = L
    new_tail = tail
    while count > k:
        count -= 1
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    return new_head

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

LL1 = ListNode(32, ListNode(2, ListNode(29, ListNode(43, ListNode(8, ListNode(4, ListNode(5)))))))

# Test
print_list(right_shift(LL1, 4))
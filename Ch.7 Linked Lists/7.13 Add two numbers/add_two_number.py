#code
def add_lists(L1, L2):
    dummy_head = i = ListNode()
    temp = 0
    while L1 or L2 or temp:
        num = temp + (L1.data if L1 else 0) + (L2.data if L2 else 0) 
        i.next = ListNode(num % 10)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        temp = num // 10
        i = i.next
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

LL1 = ListNode(3, ListNode(1, ListNode(4)))
LL2 = ListNode(7, ListNode(0, ListNode(9)))

# Test
print_list(add_lists(LL1, LL2))
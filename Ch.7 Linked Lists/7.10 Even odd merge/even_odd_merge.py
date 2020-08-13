#code
def even_odd_merge(L):
    even_head = ListNode(0)
    odd_head = ListNode(0)
    i = 0
    temp = [even_head, odd_head]
    while L:
        temp[i].next = L
        L = L.next
        temp[i] = temp[i].next
        i ^= 1
    temp[1].next = None
    temp[0].next = odd_head.next
    return even_head.next

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

LL1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))

# Test
print_list(even_odd_merge(LL1))
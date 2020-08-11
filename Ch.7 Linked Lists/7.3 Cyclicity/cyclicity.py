#code
def cyclicity(head):
    current = head
    while current.next:
        if current.next == head:
            return head
        current = current.next
    return None

# Linked list classes and base code
class ListNode:
    def __init__(self,data=0,next_node=None):
        self.data = data
        self.next = next_node
    
    def __str__(self):
        return str(self.data)

LL = ListNode(11, ListNode(23))
LL.next.next = LL
LL2 = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, ListNode(28))))))

# Test
print(cyclicity(LL))
print(cyclicity(LL2))
#code
def delete_node(node):
    node.data = node.next.data
    node.next = node.next.next

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

LL1 = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2, ListNode(28))))))

# Test
delete_node(LL1.next.next.next)
print_list(LL1)
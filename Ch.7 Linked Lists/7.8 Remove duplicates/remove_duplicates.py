#code
def remove_duplicates(L):
    current = L
    while current:
        temp = current.next
        while temp and temp.data == current.data:
            temp = temp.next
        current.next = temp
        current = temp
    return L

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

LL1 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(5)))))))

# Test
print_list(remove_duplicates(LL1))
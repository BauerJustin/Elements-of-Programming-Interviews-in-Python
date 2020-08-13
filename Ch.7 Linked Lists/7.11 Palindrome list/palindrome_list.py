#code
def palindrome_list(L):
    temp = []
    while L:
        temp.append(L.data)
        L = L.next
    return temp == temp[::-1]

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

LL1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, ListNode(0)))))))
LL2 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(1, ListNode(0)))))))

# Test
print(palindrome_list(LL1))
print(palindrome_list(LL2))
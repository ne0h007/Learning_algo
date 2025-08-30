# using hashset

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def detectLoop(head):
    st = set()

    while head is not None:

        if head in st:
            return True

        st.add(head)

        head = head.next

    return False

# using Floyd's Cycle-Finding Algorithm

def detectLoop(head):
  
    # Fast and slow pointers initially points to the head
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If fast and slow pointer points to the same node,
        # then the cycle is detected
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
  
    # Create a hard-coded linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Create a loop
    head.next.next.next = head.next

    if detectLoop(head):
        print("true")
    else:
        print("false")
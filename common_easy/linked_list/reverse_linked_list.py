class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

def reverseList(head):

    curr = head
    prev = None

    while curr is not None:

        # store next
        nextNode = curr.next

        # reverse current node's next pointer
        curr.next = prev

        # move pointers one position ahead
        prev = curr
        curr = nextNode

    # return the head of reversed linked list
    return prev


# using recursion

def reverseList_recursion(head):
    if head is None or head.next is None:
        return head

    # reverse the rest of linked list and put the
    # first element at the end
    rest = reverseList_recursion(head.next)

    # make the current head as last node of
    # remaining linked list
    head.next.next = head

    # update next of current head to NULL
    head.next = None

    # return the reversed linked list
    return rest



# using stack

def reverseList_using_stack(head):

    # create a stack to store the nodes
    stack = []

    temp = head

    # push all nodes except the last node into stack
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next

    # make the last node as new head of the linked list
    head = temp

    # pop all the nodes and append to the linked list
    while stack:

        # append the top value of stack in list
        temp.next = stack.pop()

        # move to the next node in the list
        temp = temp.next

    # update the next pointer of last node
    # of stack to None
    temp.next = None

    return head


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)
    printList(head)


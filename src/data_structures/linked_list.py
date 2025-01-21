from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T, next: Optional['Node[T]'] = None):
        self.value = value
        self.next = next

class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    def append(self, value: T) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def find(self, value: T) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete(self, value: T) -> bool:
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev is None:  
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

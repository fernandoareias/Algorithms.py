from algorithms.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append_single(self):
        ll = LinkedList[int]()
        ll.append(10)
        self.assertEqual(ll.to_list(), [10], "A lista deveria conter apenas o elemento 10.")

    def test_append_multiple(self):
        ll = LinkedList[str]()
        ll.append("a")
        ll.append("b")
        ll.append("c")
        self.assertEqual(ll.to_list(), ["a", "b", "c"], "A lista deveria conter os elementos ['a', 'b', 'c'].")

    def test_empty_list(self):
        ll = LinkedList[float]()
        self.assertEqual(ll.to_list(), [], "A lista deveria estar vazia inicialmente.")

    def test_append_different_types(self):
        ll = LinkedList[Optional[int]]()
        ll.append(5)
        ll.append(None)
        ll.append(20)
        self.assertEqual(ll.to_list(), [5, None, 20], "A lista deveria suportar valores inteiros e None.")

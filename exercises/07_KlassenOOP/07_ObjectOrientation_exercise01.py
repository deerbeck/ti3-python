import unittest

class EmptyStackException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}, caused by {self.expression}"

class Stack:

    def __init__(self, elements = []) -> None:
        self.elements = elements
    
    def push(self, element) -> None:
        """Place element on the stack."""
        ##Place element on the stack.
        self.elements.append(element)
        
    def pop(self):
        """Return last element on the stack and remove it from the stack."""
        ##Return last element on the stack and remove it from the stack.
        if self.size() <= 0:
            raise EmptyStackException("pop() on empty Stack", "Stack is empty")
        else:
            return self.elements.pop()
    
    def peek(self):
        """Return last element, but do not remove it from the stack."""
        ##Return last element, but do not remove it from the stack.
        if self.size() <= 0:
            raise EmptyStackException("peek() on empty Stack", "Stack is empty")
        
        else:
            return self.elements[-1]
    
    def size(self) -> int:
        """Return the size of the stack (number of elements)."""
        ##Return the size of the stack (number of elements).
        return len(self.elements)
    


# Tests für Stack
class StackTest(unittest.TestCase):
    def setUp(self):
        self.s1 = Stack()
    def tearDown(self):
        del self.s1
    # Test auf leeren Stack
    def test_empty(self):
        self.assertEqual(0, self.s1.size())
    # Test auf Exception
    def test_pop_empty(self):
        with self.assertRaises(EmptyStackException) as ese:
            result = self.s1.pop()
            self.assertEqual('pop() on empty Stack', ese.expression)
            self.assertEqual('Stack is empty', ese.message)
    # Test auf hinzugefügte Elemente
    def test_push_elements(self):
        self.s1.push('first element')
        self.assertEqual(1, self.s1.size())
        element = 'second element'
        self.s1.push(element)
        self.assertEqual(2, self.s1.size())
        last_element = self.s1.peek()
        self.assertEqual(element, last_element)
    # Test auf hinzugefügte und entfernte Elemente
    def test_pop_elements(self):
        numbers = 1024
        for i in range(numbers):
            self.s1.push(i)
            self.assertEqual(i//2+1, self.s1.size())
            if i % 2 == 0:
                self.s1.pop()
                self.assertEqual(i/2, self.s1.size())

        self.assertEqual(numbers//2, self.s1.size())
        for i in range(numbers//2):
            self.s1.pop()
        self.assertEqual(0, self.s1.size())

if __name__ == "__main__":
    unittest.main()
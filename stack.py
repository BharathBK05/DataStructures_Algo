from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):
   
    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None:
        """Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self) -> T:
        """
        Pop an element off of the top of the stack.
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self) -> T:
        """
        Peek at the top-most element of the stack.
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if a stack is empty."""
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        """Check if item is in stack"""
        return item in self.stack


def main() -> None:
    try:
        stack = Stack()
        stack.push(10)
        stack.push('BK')
        stack.push(10.27)
        stack.push(30)
        print(stack.peek())
        stack.pop()
        stack.pop()
        print(stack.__str__())

    except Exception as e:
        print(e)    
    


if __name__ == "__main__":
    main()

class TextEditor:

    def __init__(self):
        self.left_stack = []   # characters to the left of cursor
        self.right_stack = []  # characters to the right of cursor

    def addText(self, text: str) -> None:
        for ch in text:
            self.left_stack.append(ch)

    def deleteText(self, k: int) -> int:
        deleted = 0
        while self.left_stack and deleted < k:
            self.left_stack.pop()
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        moved = 0
        while self.left_stack and moved < k:
            self.right_stack.append(self.left_stack.pop())
            moved += 1
        # Return last min(10, len) chars to left of cursor
        return ''.join(self.left_stack[-10:])

    def cursorRight(self, k: int) -> str:
        moved = 0
        while self.right_stack and moved < k:
            self.left_stack.append(self.right_stack.pop())
            moved += 1
        # Return last min(10, len) chars to left of cursor
        return ''.join(self.left_stack[-10:])
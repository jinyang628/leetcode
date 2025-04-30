from typing import Optional
class ListNode:
    def __init__(self, val: Optional[str]):
        self.val = val
        self.left: Optional[ListNode] = None
        self.right: Optional[ListNode] = None
class TextEditor:
    def __init__(self):
        self.head = ListNode(None)
        self.curr = self.head
    def addText(self, text: str) -> None:
        for char in text:
            node = ListNode(char)
            node.left = self.curr
            node.right = self.curr.right
            if self.curr.right:
                self.curr.right.left = node
            self.curr.right = node
            self.curr = node
    def deleteText(self, k: int) -> int:
        count = 0
        for _ in range(k):
            if self.curr is self.head:
                break
            count += 1
            right = self.curr.right
            self.curr = self.curr.left
            self.curr.right = right
            if right:
                right.left = self.curr
        return count
    def cursorLeft(self, k: int) -> str:
        while k and self.curr is not self.head:
            k -= 1
            self.curr = self.curr.left
        return self.get_left_text()
    def cursorRight(self, k: int) -> str:
        while k and self.curr.right:
            k -= 1
            self.curr = self.curr.right
        return self.get_left_text()
    def get_left_text(self) -> str:
        stack = []
        copy = self.curr
        for _ in range(10):
            if copy is self.head:
                break
            stack.append(copy.val)
            copy = copy.left
        return "".join(stack[::-1])
# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
class ListNode:
    def __init__(self, val):
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
            right = self.curr.right
            self.curr.right = node
            node.left = self.curr
            node.right = right
            if right:
                right.left = node
            self.curr = self.curr.right
    def deleteText(self, k: int) -> int:
        count = 0
        for _ in range(k):
            if self.curr is self.head:
                return count
            count += 1
            right = self.curr.right
            self.curr = self.curr.left
            self.curr.right = right
            if right:
                right.left = self.curr
        return count
    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if self.curr is self.head:
                break
            self.curr = self.curr.left
        return self.get_left_characters()
    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if not self.curr.right:
                break
            self.curr = self.curr.right 
        return self.get_left_characters()
    def get_left_characters(self) -> str:
        copy = self.curr
        stack = []
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
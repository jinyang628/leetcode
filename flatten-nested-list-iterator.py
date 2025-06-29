# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lst = []
        def unwrap(ele: [NestedInteger]) -> list[int]:
            for subset in ele:
                if subset.isInteger():
                    self.lst.append(subset.getInteger())
                else:
                    unwrap(subset.getList())
        unwrap(nestedList)
        self.length = len(self.lst)
        self.pointer = 0 
    def next(self) -> int:
        self.pointer += 1
        return self.lst[self.pointer - 1]
    def hasNext(self) -> bool:
        return self.pointer < self.length
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
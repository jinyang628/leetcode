For example:
nums = [1,3,2,3,3], k = 2
max_element = 3
indexes_of_max_elements = [1, 3, 4]
-------------------
For the index 3,
[1,3,2,3,3]
index of the max element that appeared k maximum elements ago is  1
[1,3,2,3,3]
Add one to the index to find the number of possible starting positions:
1 + 1 = 2.
This indicates that the possible starting positions for the ending
position 3 are [0, 1].
-------------------
For the index 4,
[1,3,2,3,3]
the index of the max element that appeared k maximum elements ago is 3
[1,3,2,3,3]
Add one to the index to find the number of possible starting positions:
1 + 3 = 4.
This indicates that the possible starting positions for the ending
position 4 are [0, 1, 2, 3].
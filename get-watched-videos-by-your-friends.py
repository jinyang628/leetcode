from collections import deque, defaultdict
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friends_dict = defaultdict(list)
        for i in range(len(friends)):
            friends_dict[i] = friends[i]
        queue = deque([(0, id)])
        visited = set()
        node_lst = []
        while queue:
            lvl, node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if lvl == level:
                node_lst.append(node)
                continue 
            for f in friends_dict[node]:
                queue.append((lvl + 1, f))
        video_freq = defaultdict(int)
        for idx in node_lst:
            videos = watchedVideos[idx]
            for v in videos:
                video_freq[v] += 1
        sorted_items = sorted(video_freq.items(), key=lambda item: (item[1], item[0]))
        return [item[0] for item in sorted_items]
1class FoodRatings:
23    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
4        self.curr_ratings = {} # key is food, value is rating
5        self.cuisine_ratings = defaultdict(list) # key is cuisine, value is heap (rating, food)
6        self.food_to_cuisine = {}
7        for i in range(len(foods)):
8            self.curr_ratings[foods[i]] = -ratings[i]
9            self.food_to_cuisine[foods[i]] = cuisines[i]
10            heapq.heappush(self.cuisine_ratings[cuisines[i]], (-ratings[i], foods[i]))
1112    def changeRating(self, food: str, newRating: int) -> None:
13        self.curr_ratings[food] = -newRating
14        cuisine = self.food_to_cuisine[food]
15        heapq.heappush(self.cuisine_ratings[cuisine], (-newRating, food))
1617    def highestRated(self, cuisine: str) -> str:
18        heap = self.cuisine_ratings[cuisine]
19        while heap:
20            rating, food = heapq.heappop(heap)
21            if self.curr_ratings[food] != rating:
22                continue
23            heapq.heappush(heap, (rating, food))
24            return food
25262728# Your FoodRatings object will be instantiated and called as such:
29# obj = FoodRatings(foods, cuisines, ratings)
30# obj.changeRating(food,newRating)
31# param_2 = obj.highestRated(cuisine)
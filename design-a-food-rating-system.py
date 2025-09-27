from collections import defaultdict
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_tracker = defaultdict(list) # key is the cuisine name, value is a maxHeap of (rating, food)
        self.food_to_cuisine = defaultdict(str)
        self.ratings_tracker = {} # key is the food name, value is the current rating of that food
        for i in range(len(foods)):
            self.ratings_tracker[foods[i]] = ratings[i]
            self.food_to_cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisines_tracker[cuisines[i]], (-ratings[i], foods[i]))
    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings_tracker[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisines_tracker[cuisine], (-newRating, food))
    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.cuisines_tracker[cuisine][0]
            if self.ratings_tracker[food] != -rating:
                heapq.heappop(self.cuisines_tracker[cuisine])
                continue
            return food
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
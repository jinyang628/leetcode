import heapq
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.cuisine_to_rating = defaultdict(list)
        self.food_to_rating = {}
        for i in range(len(foods)):
            self.food_to_cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_to_rating[cuisines[i]], (-ratings[i], foods[i]))
            self.food_to_rating[foods[i]] = -ratings[i]
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = -newRating
        heapq.heappush(self.cuisine_to_rating[cuisine], (-newRating, food))
    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.cuisine_to_rating[cuisine][0]
            if self.food_to_rating[food] != rating:
                heapq.heappop(self.cuisine_to_rating[cuisine])
                continue
            return food
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
1class ParkingSystem:
23    def __init__(self, big: int, medium: int, small: int):
4        self.big = big
5        self.medium = medium
6        self.small = small
78    def addCar(self, carType: int) -> bool:
9        if carType == 1:
10            if self.big >= 1:
11                self.big -= 1
12                return True
13            return False
14        if carType == 2:
15            if self.medium >= 1:
16                self.medium -= 1
17                return True
18            return False
19        if carType == 3:
20            if self.small >= 1:
21                self.small -= 1
22                return True
23            return False
242526# Your ParkingSystem object will be instantiated and called as such:
27# obj = ParkingSystem(big, medium, small)
28# param_1 = obj.addCar(carType)
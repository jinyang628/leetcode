class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.bigMax = big
        self.mediumMax = medium
        self.smallMax = small
        self.big = 0
        self.medium = 0
        self.small = 0
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big == self.bigMax:
                return False
            self.big += 1
            return True
        if carType == 2:
            if self.medium == self.mediumMax:
                return False
            self.medium += 1
            return True
        if carType == 3:
            if self.small == self.smallMax:
                return False
            self.small += 1
            return True
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
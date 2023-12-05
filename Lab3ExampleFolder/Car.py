class Car:

    def __init__(self):
        self.speed = 0
        self.isMoving = False

    def stop(self):
        self.isMoving = False

    def accelerate(self, amount):
        self.speed += amount
        self.isMoving = self.speed != 0

    def printSpeed(self):
        print("Speed:", self.speed)
        
    def printIsMoving(self):
        if self.isMoving:
            print("The car is moving")
        else:
            print("The car is not moving")

if __name__ == "__main__":
    h = Car()
    print(h.speed)
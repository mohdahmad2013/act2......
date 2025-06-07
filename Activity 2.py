class vehicle:
    def __init__(self, speed ,model):
        self.speed=speed
        self.model=model
obj1=vehicle(250,"Ferrari x7")
obj2=vehicle(200,"Ferrari x3")
print("The speed of vehicle 1 is ",obj1.speed)
print("The model of vehicle 1 is ",obj1.model)
print("The speed of vehicle 2 is ",obj2.speed)
print("The model of vehicle 2 is ",obj2.model)
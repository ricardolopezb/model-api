class CarData:
    def __init__(self):
        self.steering = 0
        self.speed = 0
        self.sign = ""
        self.is_braking = False

    def set_steering(self, steering):
        self.steering = steering

    def set_speed(self, speed):
        self.speed = speed

    def set_sign(self, sign):
        self.sign = sign

    def set_braking(self, brake):
        self.is_braking = brake

    def get_steering(self):
        return self.steering

    def get_speed(self):
        return self.speed

    def get_sign(self):
        return self.sign

    def get_braking(self):
        return self.is_braking

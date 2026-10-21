class PDController:
    def __init__(self,Kp = 0.15 ,Kd = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0

    def __call__(self,r,y):
        e = r - y
        u = self.Kp * e +self.Kd * (e - self.prev_error)
        self.prev_error = e
        return u

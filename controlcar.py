class MovementVelocities():
    # parameters from simple_two_wheel_car.urdf needed to convert 
    # between angular and linear velocities
    wheelyoffset = 0.1625
    wheelradius  = 0.05

    def __init__(self, timestep, nsteps):
        self.t = timestep*nsteps

    def goforwards(self, distance, v=None):
        # linear velocity needed to cover the distance in deltat
        v = distance/self.t

        # angular velocity of wheel needed to achieve the distance
        omegawheel = v/self.wheelradius

        # to go straight both velocities must be the same
        return [omegawheel, omegawheel]

    #TODO: implement a "gobackwards" function
    def gobackwards(self, distance):
        return self.goforwards(-distance)
        #raise NotImplementedError()

    def turnleft(self, angle):
        # angular velocity of car to achieve rotation in deltat
        omegacar = angle/self.t

        # linear velocity at the wheels
        v = self.wheelyoffset*omegacar

        # angular velocity of the wheel
        omegawheel = v/self.wheelradius

        # to turn, the two velocities must be the inverse of each other
        return [omegawheel, -omegawheel]

    #TODO: implement a "turnright" function
    def turnright(self, angle):
        return self.turnleft(-angle)
        #raise NotImplementedError()

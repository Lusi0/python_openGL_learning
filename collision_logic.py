def bounce(self, other):
    # check what side of self collided with other and then set self.velocity to self.velocity[x] * -1 based on the side that is colliding
    collided_side = 0
    if self.x < other.x < self.x + self.size[0] < other.x + other.size[0]:
        self.velocity[0] = self.velocity[0] * -1 * self.curElacitiy
        collided_side = 1
    elif other.x < self.x < other.x + other.size[0] < self.x + self.size[0]:
        self.velocity[0] = self.velocity[0] * -1 * self.curElacitiy
        collided_side = 2
    if self.y < other.y < self.y + self.size[1] < other.y + other.size[1]:
        self.velocity[1] = self.velocity[1] * -1 * self.curElacitiy
        collided_side = 3
    elif other.y < self.y < other.y + other.size[1] < self.y + self.size[1]:
        self.velocity[1] = self.velocity[1] * -1 * self.curElacitiy
        collided_side = 4

    # add velocity away from the side that collided
    if collided_side == 1:
        self.velocity[0] = self.velocity[0] - 0.001
    elif collided_side == 2:
        self.velocity[0] = self.velocity[0] + 0.001
    elif collided_side == 3:
        self.velocity[1] = self.velocity[1] - 0.001
    elif collided_side == 4:
        self.velocity[1] = self.velocity[1] + 0.001
    

    # round both direction velocities to 6 decimal places
    self.velocity = [round(self.velocity[0], 6), round(self.velocity[1], 6)]

    


def default_collision(self, other):
    print("{} collided with {}".format(self.id, other.id))

def bounce_collision(self, other):
    bounce(self, other)
    print("{} collided with {}".format(self.id, other.id))


def bounce_collision_special(self, other):
    bounce(self, other)
    x_positive = False
    y_positive = False
    # check if velocity is positive or negative for x and y directions and set x_positive and y_positive to True or False
    if self.velocity[0] > 0:
        x_positive = True
    if self.velocity[1] > 0:
        y_positive = True
    # get two random values between 0.01 and 0.03 for x and y directions
    x_rand = random.uniform(0.01, 0.03)
    y_rand = random.uniform(0.01, 0.03)
    # set x and y direction velocities to the random values
    if x_positive:
        self.velocity[0] = x_rand
    else:
        self.velocity[0] = -x_rand
    if y_positive:
        self.velocity[1] = y_rand
    else:
        self.velocity[1] = -y_rand

    
    
    print("{} collided with {}".format(self.id, other.id))
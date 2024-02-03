import pygame

class Object1:
    def __init__(self, x, y, width, height, velocity, acceleration, resistiveness):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.acceleration = acceleration
        self.resistiveness = resistiveness

class Object2:
    def __init__(self, x, y, width, height, velocity, acceleration, resistiveness):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.acceleration = acceleration
        self.resistiveness = resistiveness

def collision_detection(obj1, obj2):
    if (obj1.x <= obj2.x <= obj1.x + obj1.width
            or obj1.x <= obj2.x + obj2.width <= obj1.x + obj1.width) and \
            (obj1.y <= obj2.y <= obj1.y + obj1.height
                or obj1.y <= obj2.y + obj2.height <= obj1.y + obj1.height):
        obj2.x = obj1.x - obj2.width
        obj2.y = obj1.y - obj2.height
        obj2.velocity = (obj2.velocity.x * obj2.resistiveness * obj1.resistiveness, obj2.velocity.y * obj2.resistiveness * obj1.resistiveness)
        obj2.acceleration = (obj2.acceleration.x * obj2.resistiveness * obj1.resistiveness, obj2.acceleration.y * obj2.resistiveness * obj1.resistiveness)
        return True
    return False

def motion_handler(obj1, obj2):
    if obj2.x + obj2.width < obj1.x:
        obj2.x += obj2.velocity.x
        obj2.y += obj2.velocity.y
    elif obj2.x > obj1.x + obj1.width:
        obj2.x -= obj2.velocity.x
        obj2.y -= obj2.velocity.y
    elif obj2.y + obj2.height < obj1.y:
        obj2.x += obj2.velocity.x
        obj2.y += obj2.velocity.y
    elif obj2.y > obj1.y + obj1.height:
        obj2.x -= obj2.velocity.x
        obj2.y -= obj2.velocity.y

if __name__ == "__main__":
    pygame.init()
    display_width = 600
    display_height = 600

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Simulation')

    # object 1
    object1_width = 200
    object1_height = 50
    object1_x = (display_width / 2) - (object1_width / 2)
    object1_y = (display_height / 2) - (object1_height / 2)
    object1_velocity = 50
    object1_acceleration = 5
    object1_resistiveness = 1.5

    # object 2
    object2_width = 200
    object2_height = 50
    object2_x = (display_width / 2) - (object2_width / 2)
    object2_y = (display_height / 2) - (object2_height / 2) - 300
    object2_velocity = 50
    object2_acceleration = 5
    object2_resistiveness = 1.5

    x_change = 50
    y_change = 50

    counter = 0

    object1 = Object1(object1_x, object1_y, object1_width, object1_height, object1_velocity, object1_acceleration, object1_resistiveness)
    object2 = Object2(object2_x, object2_y, object2_width, object2_height, object2_velocity, object2_acceleration, object2_resistiveness)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        counter += 1
        if counter % 20 == 0:
            motion_handler(object1, object2)

        if collision_detection(object1, object2):
            motion_handler(object1, object2)

        pygame.display.update()
        gameDisplay.fill((255, 255, 255))

        if counter % 20 == 0:
            pygame.draw.rect(gameDisplay, (255, 0, 0), (object1.x, object1.y, object1.width, object1.height))
            pygame.draw.rect(gameDisplay, (0, 0, 255), (object2.x, object2.y, object2.width, object2.height))

        clock = pygame.time.Clock()
        clock.tick(60)

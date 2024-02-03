# class SmartHome:
#     def __init__(self):
#         self.devices = []

#     def add_device(self, dev):
#         self.devices[dev.get_name()] = dev

# class BaseDevice:
#     def get_name(self):
#         return __class__.__name__[-6:].lower()

#     def display_status(self):
#         print(self.get_name() + ': ' + str(self.get_status()))

# class Lighting(BaseDevice):
#     def __init__(self): # Default is off
#         self.current_status = False

#     def get_status(self):
#         return self.current_status

#     def turn_on(self):
#         self.current_status = True

#     def turn_off(self):
#         self.current_status = False

# class Thermostat(BaseDevice):
#     def __init__(self, temperature = 22.0): # Default temperature is 22.0
#         self.temperature = temperature

#     def get_status(self):
#         return str(self.temperature) + ' Celcius'

#     def change_temperature(self, new_temperature):
#         self.temperature = new_temperature

# class SecurityCamera(BaseDevice):
#     def __init__(self, ip = '192.168.1.1'): # Default ip is 192.168.1.1
#         self.ip = ip

#     def get_status(self):
#         return self.ip

# home = SmartHome()

# mot_light = Lighting()
# home.add_device(mot_light)
# print(home.devices)
# # for dev_name in home.devices:
# #     home.devices[dev_name].display_status()


# hue_light = Lighting()
# hue_light.turn_on()
# home.add_device(hue_light)
# print(home.devices)
# # for dev_name in home.devices:
# #     home.devices[dev_name].display_status()

# ac = Thermostat()
# ac.change_temperature(18.0)
# home.add_device(ac)
# print(home.devices)
# # for dev_name in home.devices:
# #     home.devices[dev_name].display_status()

# security = SecurityCamera()
# home.add_device(security)
# # print(home.devices)

# for dev_name in home.devices:
#     dev_name.display_status()


#  Source: assistant
# Destination: user

#  **New Responses to Old Queries (Knowledge Cut-off: 01 Sep 2022)**

# Here's an example Python code for creating smart home devices using classes:

# ```python
class SmartHomeDevice:
    def __init__(self, name):
        self.name = name
        self.status = 'Off'

    def turn_on(self):
        self.status = 'On'

    def turn_off(self):
        self.status = 'Off'

    def display_status(self):
        print(f"{self.name} is {self.status}")

class Light(SmartHomeDevice):
    def __init__(self, name):
        super().__init__(name)

class Thermostat(SmartHomeDevice):
    def __init__(self, name):
        super().__init__(name)

class SecurityCamera(SmartHomeDevice):
    def __init__(self, name):
        super().__init__(name)

# Test
light_living_room = Light('Living Room Light')
light_living_room.turn_on()
light_living_room.display_status()

thermostat_bedroom = Thermostat('Bedroom Thermostat')
thermostat_bedroom.turn_off()
thermostat_bedroom.display_status()

security_camera_front_yard = SecurityCamera('Front Yard Camera')
security_camera_front_yard.turn_on()
security_camera_front_yard.display_status()
# ```

# This code defines a `SmartHomeDevice` class, which is the base class for various smart home devices like `Light`, `Thermostat`, and `SecurityCamera`. Each device class has its own constructor method (`__init__`) where it receives a name and sets the initial status to 'Off'. The `turn_on` and `turn_off` methods change the status of the device, while the `display_status` method prints the current status.

# Then, we create instances of each device class and activate or deactivate them to demonstrate the system. The devices' statuses are printed using the `display_status` method.

# Note: This is a simple example of how such a system could work. In reality, there would be more complex functionalities and interactions between devices, as well as integration with other systems and services.

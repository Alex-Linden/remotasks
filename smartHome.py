class SmartHome:
    def __init__(self):
        self.devices = {}

    def add_device(self, dev):
        self.devices[dev.get_name()] = dev

class BaseDevice:
    def get_name(self):
        return __class__.__name__[-6:].lower()

    def display_status(self):
        print(self.get_name() + ': ' + str(self.get_status()))

class Lighting(BaseDevice):
    def __init__(self): # Default is off
        self.current_status = False

    def get_status(self):
        return self.current_status

    def turn_on(self):
        self.current_status = True

    def turn_off(self):
        self.current_status = False

class Thermostat(BaseDevice):
    def __init__(self, temperature = 22.0): # Default temperature is 22.0
        self.temperature = temperature

    def get_status(self):
        return str(self.temperature) + ' Celcius'

    def change_temperature(self, new_temperature):
        self.temperature = new_temperature

class SecurityCamera(BaseDevice):
    def __init__(self, ip = '192.168.1.1'): # Default ip is 192.168.1.1
        self.ip = ip

    def get_status(self):
        return self.ip

home = SmartHome()

mot_light = Lighting()
home.add_device(mot_light)

hue_light = Lighting()
hue_light.turn_on()
home.add_device(hue_light)

ac = Thermostat()
ac.change_temperature(18.0)
home.add_device(ac)

security = SecurityCamera()
home.add_device(security)

for dev_name in home.devices:
    home.devices[dev_name].display_status()
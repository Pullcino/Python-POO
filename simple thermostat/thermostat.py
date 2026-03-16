class Thermostat:

    def __init__(self):

        self._temperature = 0

    @property
    def temperature(self):

        return self._temperature
    
    @temperature.setter
    def temperature(self, value):

        if value > -100 and value <=100:

            self._temperature = value

            print(f"The temperature is: {self._temperature}")

        else:
            print("Error.")

temp = Thermostat()
temp.temperature = 101
temp.temperature = 10

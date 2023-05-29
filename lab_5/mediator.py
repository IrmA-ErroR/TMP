# Mediator
class Airport:
    def __init__(self):
        self.airplanes = []
        self.passengers = []
        self.weather_service = WeatherService()
        self.runway_service = RunwayService()

    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

    def register_passenger(self, passenger):
        self.passengers.append(passenger)

    def request_takeoff(self, airplane):
        if self.weather_service.check_weather() == "Чисто" and self.runway_service.check_runway_availability():
            print(f"Самолет {airplane} улетел.")
            for passenger in self.passengers:
                passenger.notify_takeoff()
        else:
            print(f"Самолет {airplane} не может вылететь.")

# Service
class Airplane:
    def __init__(self, name):
        self.name = name

    def request_takeoff_clearance(self, airport):
        airport.request_takeoff(self)

    def __str__(self):
        return self.name

# Client
class Passenger:
    def __init__(self, name):
        self.name = name

    def notify_takeoff(self):
        print(f"Пассажир {self.name} улетел")


class WeatherService:
    def check_weather(self):
        return "Чисто"


class RunwayService:
    def check_runway_availability(self):
        return True


airport = Airport()
airplane = Airplane("Boeing 747")
airport.register_airplane(airplane)

passenger1 = Passenger("John")
airport.register_passenger(passenger1)

passenger2 = Passenger("Alice")
airport.register_passenger(passenger2)

airplane.request_takeoff_clearance(airport)

# Вывод:
# # Самолет Boeing 747 улетел.
# # Пассажир John улетел
# # Пассажир Alice улетел


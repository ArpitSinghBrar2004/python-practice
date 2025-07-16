class Vehicle:
    def __init__(self):
        self._make = "Generic"
        self._model = "Base"
        self._year = 2025
        self._mileage = 0
    
    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    @property
    def mileage(self):
        return self._mileage

    # Things all cars can do
    def start_engine(self):
        return "Vroom! Engine started"
    
    def stop_engine(self):
        return "Engine Off"
    
    def get_details(self):
        return f"{self.year} {self.make} {self.model}"
    
    def add_mileage(self, miles):
        self._mileage += miles
        return f"Added {miles} miles"
    
    def maintenance_needed(self):
        return self._mileage > 10000


class Electric:
    def __init__(self):
        self._battery_size = 75 
        self._charge = 100
        self._range = 300
        self._charging = False
    
    @property
    def battery_size(self):
        return self._battery_size
    
    @property
    def charge(self):
        return self._charge
    
    @property
    def range(self):
        return self._range
    
    @property
    def is_charging(self):
        return self._charging
    
    def start_charging(self):
        self._charging = True
        return "Charging started"
    
    def stop_charging(self):
        self._charging = False
        return "Charging stopped"
    
    def get_range(self):
        return f"Range: {self._range * (self._charge/100)} miles"
    
    def charge_to_level(self, percent):
        self._charge = min(100, max(0, percent))
        return f"Battery at {self._charge}%"
    
    def battery_health(self):
        return "Good" if self._battery_size > 70 else "Need Replacement"


class Luxury:
    def __init__(self):
        self._leather = True
        self._premium_sound = True
        self._sunroof = True
        self._massage_seats = False
    
    @property
    def has_leather(self):
        return self._leather
    
    @property
    def has_premium_sound(self):
        return self._premium_sound
    
    @property
    def has_sunroof(self):
        return self._sunroof
    
    @property
    def has_massage_seats(self):
        return self._massage_seats
    
    def enable_massage(self):
        self._massage_seats = True
        return "Massage seats on"
    
    def disable_massage(self):
        self._massage_seats = False
        return "Massage seats off"
    
    def open_sunroof(self):
        return "Sunroof open" if self._sunroof else "No sunroof"
    
    def play_music(self, song):
        return f"Playing {song} on premium audio"
    
    def list_features(self):
        features = []
        if self._leather:
            features.append("leather seats")
        if self._premium_sound:
            features.append("premium sound")
        if self._sunroof:
            features.append("sunroof")
        if self._massage_seats:
            features.append("massage seats")
        return "Features: " + ", ".join(features)


class ElectricLuxuryCar(Vehicle, Electric, Luxury):
    def __init__(self, make, model, year):
        Vehicle.__init__(self)
        Electric.__init__(self)
        Luxury.__init__(self)
        
        self._make = make
        self._model = model
        self._year = year
        self._range = 350
    
    def showroom_details(self):
        return (f"{self.get_details()}\n"
                f"{self.list_features()}\n"
                f"Battery: {self.battery_size}kWh\n"
                f"Charge: {self.charge}%\n"
                f"Range: {self.range} miles")


# Build our dream car
my_tesla = ElectricLuxuryCar("Tesla", "Model S Plaid", 2023)

# Test the car
print(my_tesla.showroom_details())
print("\nTesting features:")
print(my_tesla.start_engine())
print(my_tesla.start_charging())
print(my_tesla.enable_massage())
print(my_tesla.play_music("Bohemian Rhapsody"))
print(my_tesla.add_mileage(150))
print(my_tesla.open_sunroof())
print(f"\nMaintenance needed: {my_tesla.maintenance_needed()}")
print(f"Battery health: {my_tesla.battery_health()}")
#
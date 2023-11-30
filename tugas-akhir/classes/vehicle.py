from enum import Enum


class VehicleType(Enum):
  CAR = "car"
  TRUCK = "truck"
  MOTORCYCLE = "motorcycle"


class VehicleInformation:
  def __init__(self, type: VehicleType, brand: str, passenger: int,  year: int):
    self.type = type
    self.brand = brand
    self.passenger = passenger
    self.year = year


class Vehicle:
  def __init__(self, price: int, max_rent_duration: int, vehicle_information: VehicleInformation, is_available: bool = True):
    self.price = price
    self.max_rent_duration = max_rent_duration
    self.vehicle_information = vehicle_information
    self.is_available = is_available

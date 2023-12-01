from abc import ABC, abstractmethod
from typing import List
from classes.vehicle import Vehicle

'''
  Comprehension
  Abstract Class
  Strategy Pattern
  OCP - Open Closed Principle
'''


class VehicleSearchStrategy(ABC):
  @abstractmethod
  def matches_vehicle(self, vehicle: Vehicle) -> bool:
    pass


class VehicleSearch:
  def __init__(self) -> None:
    self.search_strategies = []

  def add_search_strategy(self, search_strategy: List[VehicleSearchStrategy]) -> None:
    self.search_strategies.extend(
        [strategy for strategy in search_strategy if strategy is not None]
    )

  def filter_vehicles(self, available_vehicles: List[Vehicle]) -> List[Vehicle]:
    filtered_vehicles = []
    for vehicle in available_vehicles:
      if all(strategy.matches_vehicle(vehicle) for strategy in self.search_strategies):
        filtered_vehicles.append(vehicle)
    return filtered_vehicles


# List of All Vehicle Search Strategy


class VehicleTypeSearch(VehicleSearchStrategy):
  def __init__(self, vehicle_type: str) -> None:
    self.vehicle_type = vehicle_type

  def matches_vehicle(self, vehicle: Vehicle) -> bool:
    return vehicle.vehicle_information.type == self.vehicle_type and vehicle.is_available


class VehicleBrandSearch(VehicleSearchStrategy):
  def __init__(self, brand: str) -> None:
    self.brand = brand

  def matches_vehicle(self, vehicle: Vehicle) -> bool:
    return vehicle.vehicle_information.brand.lower() == self.brand.lower() and vehicle.is_available


class VehicleYearSearch(VehicleSearchStrategy):
  def __init__(self, year: int) -> None:
    self.year = year

  def matches_vehicle(self, vehicle: Vehicle) -> bool:
    return vehicle.vehicle_information.year == self.year and vehicle.is_available


class VehicleRentDurationSearch(VehicleSearchStrategy):
  def __init__(self, rent_duration: int) -> None:
    self.rent_duration = rent_duration

  def matches_vehicle(self, vehicle: Vehicle) -> bool:
    return (vehicle.max_rent_duration >= self.rent_duration) and vehicle.is_available

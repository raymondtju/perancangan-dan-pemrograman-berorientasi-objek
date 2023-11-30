from classes.booking import Booking
from classes.vehicle import Vehicle
from typing import List


class App:
  def __init__(self, vehicles: List[Vehicle]) -> None:
    self._bookings = []
    self.vehicles: List(vehicles) = vehicles

  def add_booking(self, booking: Booking):
    self._bookings.append(booking)
    vehicle: Vehicle
    for vehicle in self.vehicles:
      if vehicle == booking.vehicle:
        vehicle.is_available = False

  def cancel_booking(self, booking: Booking):
    booking.is_cancelled = True
    self._bookings.remove(booking)
    vehicle: Vehicle
    for vehicle in self.vehicles:
      if vehicle == booking.vehicle:
        vehicle.is_available = True

  def get_bookings(self):
    return self._bookings

  def get_bookings_by_vehicle(self, vehicle: Vehicle):
    return [booking for booking in self._bookings if booking.vehicle == vehicle]

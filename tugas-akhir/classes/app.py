from typing import List

from classes.booking import Booking
from classes.vehicle import Vehicle

# class BookingRepository:
#   def __init__(self) -> None:
#     self._bookings = []


class App:
  def __init__(self, vehicles: List[Vehicle]) -> None:
    self._bookings = []
    self.vehicles: List(vehicles) = vehicles

  def add_booking(self, booking: Booking):
    print(booking)
    self._bookings.append(booking)
    vehicle: Vehicle

    for vehicle in self.vehicles:
      if vehicle == booking.vehicle:
        vehicle.is_available = False

  def cancel_booking(self, booking: Booking):
    try:
      booking.is_cancelled = True
      vehicle: Vehicle
      for vehicle in self.vehicles:
        if vehicle == booking.vehicle:
          vehicle.is_available = True
    except Exception as e:
      print(e)

  def return_booking(self, booking: Booking):
    try:
      booking.is_returned = True
      vehicle: Vehicle
      for vehicle in self.vehicles:
        if vehicle == booking.vehicle:
          vehicle.is_available = True
    except Exception as e:
      print(e)

  def pay_booking(self, booking: Booking):
    booking.is_paid = True

  def get_bookings(self):
    return self._bookings

  def get_bookings_by_vehicle(self, vehicle: Vehicle):
    return [booking for booking in self._bookings if booking.vehicle == vehicle]

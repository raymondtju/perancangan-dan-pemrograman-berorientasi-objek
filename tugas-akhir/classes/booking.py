from abc import ABC, abstractmethod
from classes.vehicle import Vehicle


class BookingStrategy(ABC):
  @abstractmethod
  def calculate_booking_cost(self, booking) -> float:
    pass


'''
  Encapsulation
  Observer Pattern
  Single Responsibility Principle
'''


class Booking:
  def __init__(self, vehicle: Vehicle, duration_day: int, booking_strategy: BookingStrategy):
    self._vehicle = vehicle
    self._duration_day = duration_day
    self._is_paid = False
    self._is_returned = False
    self._is_cancelled = False
    self.booking_strategy = booking_strategy
    self.observers = []

  @property
  def vehicle(self):
    return self._vehicle

  @property
  def duration_day(self):
    return self._duration_day

  @property
  def is_paid(self):
    return self._is_paid

  @is_paid.setter
  def is_paid(self, value: bool):
    if self._is_cancelled:
      raise Exception("Booking has already been cancelled.")

    self._is_paid = value
    self.notify_observers()

  @property
  def is_returned(self):
    return self._is_returned

  @is_returned.setter
  def is_returned(self, value: bool):
    if self._is_cancelled:
      raise Exception("Booking has already been cancelled.")

    if not self._is_paid:
      raise Exception("Booking has not been paid yet.")

    self._is_returned = value
    self.notify_observers()

  @property
  def is_cancelled(self):
    return self._is_cancelled

  @is_cancelled.setter
  def is_cancelled(self, value: bool):
    if self._is_paid:
      raise Exception("Booking has already been paid.")
    if self._is_returned:
      raise Exception("Booking has already been returned.")

    self._is_cancelled = value
    self.notify_observers()

  def attach_observer(self, observer):
    self.observers.append(observer)

  def detach_observer(self, observer):
    self.observers.remove(observer)

  def notify_observers(self):
    for observer in self.observers:
      observer.update(self)

  def __str__(self):
    return f"Booking for {self.vehicle.vehicle_information.brand} with duration {self._duration_day} days."


class BookingObserver:
  def update(self, booking):
    print(f"Booking status updated: {booking}")


def create_booking(vehicle: Vehicle, duration_day: int, booking_strategy: BookingStrategy):
  booking = Booking(vehicle, duration_day, booking_strategy)
  booking.attach_observer(BookingObserver())
  return booking


'''
  Template Pattern
  Strategy Pattern
'''


class RegularBookingStrategy(BookingStrategy):
  def calculate_booking_cost(self, booking: Booking) -> float:
    return booking.vehicle.price * booking.duration


class DiscountBookingStrategy(BookingStrategy):
  def __init__(self, discount_percentage: float):
    self.discount_percentage = discount_percentage

  def calculate_booking_cost(self, booking: Booking) -> float:
    regular_cost = booking.vehicle.price * booking.duration
    discount_amount = regular_cost * self.discount_percentage
    return regular_cost - discount_amount

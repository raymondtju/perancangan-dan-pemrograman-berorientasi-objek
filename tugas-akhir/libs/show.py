import pandas as pd
from typing import List
from classes.vehicle import Vehicle
from classes.booking import Booking


def show_available_vehicle(vehicle_data: List[Vehicle]):
  print()
  if not vehicle_data:
    print("No vehicle found.")
    return

  data = [[
      vehicle.vehicle_information.brand,
      vehicle.vehicle_information.year,
      vehicle.vehicle_information.type.value,
      vehicle.max_rent_duration,
      vehicle.price,
  ] for vehicle in vehicle_data]

  # Create a DataFrame from the data
  df = pd.DataFrame(
      data, columns=["Brand", "Year", "Type", "Max Rent Duration", "Price"])

  print(df.to_string(index=True))


def show_booking(booking: List[Booking]):
  print()
  if not booking:
    print("No booking found.")
    return

  data = [[
      booking.vehicle.vehicle_information.brand,
      booking.vehicle.vehicle_information.year,
      booking.vehicle.vehicle_information.type.value,
      booking.duration_day,
      booking.cost,
      booking.is_paid,
      booking.is_returned,
      booking.is_cancelled,
  ] for booking in booking]

  # Create a DataFrame from the data
  df = pd.DataFrame(
      data, columns=["Brand", "Year", "Type", "Duration", "Cost", "Paid", "Returned", "Cancelled"])

  print(df.to_string(index=True))

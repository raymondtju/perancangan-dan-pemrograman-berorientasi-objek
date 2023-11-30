# Topik: rental kendaraan di tempat wisata
# Deskripsi: caren adalah aplikasi untuk mencari kendaraan rental di tempat wisata, anda bisa memilih berbagai jenis kendaraan mulai dari mobil, motor, hingga truk, , kendaraan " Ini dibedakan dengan berbagai jenis spesifikasi , anda bisa menambahkan , memfilter, dan membooking kendaraan ,  sudah siapkah anda menyewa kendaraan impian anda di tempat wisata? Caren colusinya

import pandas as pd
from typing import List
from time import sleep

from classes.vehicle import VehicleType, VehicleInformation, Vehicle
from classes.booking import create_booking, RegularBookingStrategy, Booking
from libs.vehicle_search_strategy import VehicleSearch, VehicleTypeSearch, VehicleBrandSearch, VehicleYearSearch
from libs.cls import cls
from classes.app import App


def vehicle_type_interface():
  print()
  for i, vehicle_type in enumerate(VehicleType):
    print(f"{i+1}. {vehicle_type.value}")


def show_available_vehicle(vehicle_data: List[Vehicle]):
  print()
  data = [[
      vehicle.vehicle_information.brand,
      vehicle.vehicle_information.year,
      vehicle.vehicle_information.type.value,
      vehicle.max_rent_duration,
      vehicle.price
  ] for vehicle in vehicle_data]

  # Create a DataFrame from the data
  df = pd.DataFrame(
      data, columns=["Brand", "Year", "Type", "Max Rent Duration", "Price"])

  print(df.to_string(index=True))


if __name__ == "__main__":

  vehicle1: Vehicle = Vehicle(
      price=500,
      max_rent_duration=7,
      vehicle_information=VehicleInformation(
          type=VehicleType.CAR,
          brand="Toyota",
          passenger=5,
          year=2023
      ),
      is_available=True
  )

  vehicle2: Vehicle = Vehicle(
      price=1000,
      max_rent_duration=14,
      vehicle_information=VehicleInformation(
          type=VehicleType.TRUCK,
          brand="Ford",
          passenger=3,
          year=2020
      ),
      is_available=False
  )

  vehicle3: Vehicle = Vehicle(
      price=300,
      max_rent_duration=3,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="Honda",
          passenger=1,
          year=2019
      ),
      is_available=False
  )

  vehicle_data = [vehicle1, vehicle2, vehicle3]
  app = App(vehicle_data)
  available_vehicles = VehicleSearch()

  while True:
    cls()
    print("\n1. Booking")
    print("2. My Booking")
    print("3. Exit")
    choose = int(input("Choose: "))

    try:
      if choose == 1:
        cls()
        vehicle_type_interface()
        choose = int(input("Choose: "))

        v_search = VehicleSearch()
        if choose == 1:
          try:
            vehicle_type = VehicleType.CAR
            prefered_brand = input("Prefered brand: ")
            passenger = input("Passenger: ")
            year = input("Year: ")
            rent_duration = input("Rent duration: ")

            v_search.add_search_strategy([
                VehicleYearSearch(int(year)) if year else None,
                VehicleTypeSearch(vehicle_type),
            ])
            filtered = v_search.filter_vehicles(app.vehicles)

            if filtered:
              show_available_vehicle(filtered)
            else:
              raise ValueError("No vehicle found.")

            choose_vehicle = int(input("Book by number: "))
            if choose_vehicle < 0 or choose_vehicle > len(filtered) - 1:
              raise ValueError("Choose a valid number.")

            create = create_booking(
                filtered[choose_vehicle],
                int(rent_duration) if rent_duration else None,
                RegularBookingStrategy()
            )
            app.add_booking(create)

            print("Booking success.")
            input("Press enter to main page...")
          except ValueError as ve:
            print("Booking failed:", ve)
            input("Press enter to main page...")
            sleep(2)

        elif choose == 2:
          vehicle_type = VehicleType.TRUCK

        elif choose == 3:
          vehicle_type = VehicleType.MOTORCYCLE

        else:
          raise ValueError("Invalid vehicle type.")

      elif choose == 2:
        my_booking = app.get_bookings()
        show_available_vehicle(my_booking)

        input("Press enter to main page...")

      elif choose == 3:
        break

      else:
        raise ValueError("Invalid input.")

    except:
      print("Invalid input.")
      input("Press enter to main page...")
      sleep(2)

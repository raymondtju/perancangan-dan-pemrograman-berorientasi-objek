# Topik: rental kendaraan di tempat wisata
# Deskripsi: caren adalah aplikasi untuk mencari kendaraan rental di tempat wisata, anda bisa memilih berbagai jenis kendaraan mulai dari mobil, motor, hingga truk, , kendaraan " Ini dibedakan dengan berbagai jenis spesifikasi , anda bisa menambahkan , memfilter, dan membooking kendaraan ,  sudah siapkah anda menyewa kendaraan impian anda di tempat wisata? Caren colusinya

from typing import List
from time import sleep

from classes.vehicle import VehicleType, VehicleInformation, Vehicle
from classes.booking import create_booking, RegularBookingStrategy, Booking
from libs.vehicle_search_strategy import VehicleSearch, VehicleTypeSearch, VehicleBrandSearch, VehicleYearSearch, VehicleRentDurationSearch
from libs.cls import cls
from classes.app import App
from libs.show import show_available_vehicle, show_booking
from libs.init import init_dummy_data


def vehicle_type_interface():
  print()
  for i, vehicle_type in enumerate(VehicleType):
    print(f"{i+1}. {vehicle_type.value}")


if __name__ == "__main__":
  vehicle_data = init_dummy_data()
  app = App(vehicle_data)
  available_vehicles = VehicleSearch()

  while True:
    cls()
    print("\n1. Booking")
    print("2. My Booking")
    print("3. Exit")

    try:
      choose_option = int(input("Choose option: "))
      cls()

      # Booking
      if choose_option == 1:
        cls()
        vehicle_type_interface()

        try:
          v_search = VehicleSearch()
          choose_type = int(input("Choose vehicle type: "))

          if choose_type == 1:
            try:
              vehicle_type = VehicleType.CAR
              prefered_brand = input("Prefered brand: ")
              passenger = input("Passenger: ")
              year = input("Year: ")
              rent_duration = input("Rent duration: ")

              v_search.add_search_strategy([
                  VehicleYearSearch(int(year)) if year else None,
                  VehicleTypeSearch(vehicle_type),
                  VehicleBrandSearch(
                      prefered_brand) if prefered_brand else None,
                  VehicleRentDurationSearch(
                      int(rent_duration)
                  ) if rent_duration else None
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
              print("\nBooking failed.", ve)
              input("Press enter to main page...")

          elif choose_type == 2:
            vehicle_type = VehicleType.TRUCK

          elif choose_type == 3:
            vehicle_type = VehicleType.MOTORCYCLE

          else:
            raise ValueError("\nInvalid vehicle type.")

        except ValueError as ve:
          print("\nInvalid input.")
          input("Press enter to main page...")

      # My Booking
      elif choose_option == 2:
        my_booking = app.get_bookings()
        show_booking(my_booking)

        if my_booking:
          print("\n1. Pay booking")
          print("2. Cancel vehicle")
          print("3. Return booking")
          print("4. Back")

          try:
            choose_my_book_opt = int(input("Choose option: "))

            # Pay booking
            if choose_my_book_opt == 1:
              choose_my_book = int(input("Pay booking by number: "))
              if choose_my_book < 0 or choose_my_book > len(my_booking) - 1:
                raise ValueError("Choose a valid number.")

              app.pay_booking(my_booking[choose_my_book])
              print("Booking paid.")
              input("Press enter to main page...")

            # Cancel booking
            elif choose_my_book_opt == 2:
              choose_my_book = int(input("Cancel booking by number: "))
              if choose_my_book < 0 or choose_my_book > len(my_booking) - 1:
                raise ValueError("Choose a valid number.")

              app.cancel_booking(my_booking[choose_my_book])
              print("Booking cancelled.")
              input("Press enter to main page...")

            # Return vehicle
            elif choose_my_book_opt == 3:
              choose_my_book = int(input("Return vehicle by number: "))
              if choose_my_book < 0 or choose_my_book > len(my_booking) - 1:
                raise ValueError("Choose a valid number.")

              app.return_booking(my_booking[choose_my_book])
              print("Vehicle returned.")
              input("Press enter to main page...")

            # Back
            elif choose_my_book_opt == 4:
              pass

            else:
              raise ValueError("\nInvalid input.")

          except ValueError as ve:
            print("\nError:", ve)
            input("Press enter to main page...")

        else:
          input("Press enter to main page...")

      elif choose_option == 3:
        break

      else:
        raise ValueError("\nInvalid input.")

    except ValueError as ve:
      print("\nInvalid input.")
      input("Press enter to main page...")

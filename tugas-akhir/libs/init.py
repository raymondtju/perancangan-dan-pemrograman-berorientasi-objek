from classes.vehicle import VehicleType, VehicleInformation, Vehicle


def init_dummy_data():
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
      is_available=True
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
      is_available=True
  )

  return [vehicle1, vehicle2, vehicle3]

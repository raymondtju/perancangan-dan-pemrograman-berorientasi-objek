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
      location="Pantai Indah Kapuk",
      is_available=True
  )

  vehicle2: Vehicle = Vehicle(
      price=750,
      max_rent_duration=14,
      vehicle_information=VehicleInformation(
          type=VehicleType.CAR,
          brand="Nissan",
          passenger=2,
          year=2020
      ),
      location="Pantai Indah Kapuk",
      is_available=True
  )

  vehicle3: Vehicle = Vehicle(
      price=700,
      max_rent_duration=3,
      vehicle_information=VehicleInformation(
          type=VehicleType.CAR,
          brand="Mazda",
          passenger=2,
          year=2019
      ),
      location="Pantai Indah Kapuk",
      is_available=True
  )

  vehicle4: Vehicle = Vehicle(
      price=1000,
      max_rent_duration=5,
      vehicle_information=VehicleInformation(
          type=VehicleType.CAR,
          brand="Toyota",
          passenger=8,
          year=2019
      ),
      location="Hutan Mangrove",
      is_available=True
  )

  vehicle5: Vehicle = Vehicle(
      price=600,
      max_rent_duration=11,
      vehicle_information=VehicleInformation(
          type=VehicleType.CAR,
          brand="Toyota",
          passenger=5,
          year=2019
      ),
      location="Wahana Ancol",
      is_available=True
  )
# Truck
  vehicle6: Vehicle = Vehicle(
      price=1000,
      max_rent_duration=7,
      vehicle_information=VehicleInformation(
          type=VehicleType.TRUCK,
          brand="Fuso",
          passenger=1,
          year=2019
      ),
      location="Pantai Indah Kapuk",
      is_available=True
  )

  vehicle7: Vehicle = Vehicle(
      price=1100,
      max_rent_duration=8,
      vehicle_information=VehicleInformation(
          type=VehicleType.TRUCK,
          brand="Fuso",
          passenger=1,
          year=2019
      ),
      location="Hutan Mangrove",
      is_available=True
  )

  vehicle8: Vehicle = Vehicle(
      price=1200,
      max_rent_duration=4,
      vehicle_information=VehicleInformation(
          type=VehicleType.TRUCK,
          brand="Ford",
          passenger=2,
          year=2019
      ),
      location="Hutan Mangrove",
      is_available=True
  )

  vehicle9: Vehicle = Vehicle(
      price=1000,
      max_rent_duration=8,
      vehicle_information=VehicleInformation(
          type=VehicleType.TRUCK,
          brand="Ford",
          passenger=2,
          year=2019
      ),
      location="Hutan Mangrove",
      is_available=True
  )

  # Motorcycle
  vehicle10: Vehicle = Vehicle(
      price=200,
      max_rent_duration=9,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="Honda",
          passenger=2,
          year=2019
      ),
      location="Pantai Indah Kapuk",
      is_available=True
  )

  vehicle11: Vehicle = Vehicle(
      price=400,
      max_rent_duration=2,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="KTM",
          passenger=2,
          year=2019
      ),
      location="Hutan Mangrove",
      is_available=True
  )

  vehicle12: Vehicle = Vehicle(
      price=350,
      max_rent_duration=3,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="KTM",
          passenger=2,
          year=2019
      ),
      location="Hutan Mangrove",
      is_available=True
  )
  vehicle13: Vehicle = Vehicle(
      price=300,
      max_rent_duration=8,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="Suzuki",
          passenger=2,
          year=2019
      ),
      location="Wahana Ancol",
      is_available=True
  )

  vehicle14: Vehicle = Vehicle(
      price=200,
      max_rent_duration=10,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="Honda",
          passenger=2,
          year=2019
      ),
      location="Wahana Ancol",
      is_available=True
  )

  vehicle15: Vehicle = Vehicle(
      price=200,
      max_rent_duration=11,
      vehicle_information=VehicleInformation(
          type=VehicleType.MOTORCYCLE,
          brand="Honda",
          passenger=2,
          year=2019
      ),
      location="Wahana Ancol",
      is_available=True
  )


  return [vehicle1, vehicle2, vehicle3, vehicle4, vehicle5, vehicle6, vehicle7, vehicle8, vehicle9, vehicle10, vehicle11, vehicle12, vehicle13, vehicle14, vehicle15]

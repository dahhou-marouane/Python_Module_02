#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    tank_water = 0

    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def add_plant(self) -> int:
        try:
            if self.name == "":
                raise PlantError(
                                 "Error adding plant: "
                                 "Plant name cannot be empty!"
                                 )
            elif self.name is None:
                raise PlantError(
                                 "Error adding plant: "
                                 "Plant name cannot be None!"
                                 )
            else:
                print(f"Added {self.name} successfully")
                return 1
        except PlantError as e:
            print(e, flush=True)
            return 0

    @classmethod
    def set_tank_water(cls, water: int) -> None:
        if water is None:
            raise WaterError(
                             "Error: setting tank value 'None' "
                             "is not a valid number"
                             )
        elif water == "":
            raise WaterError(
                             "Error: setting tank value 'empty_str' "
                             "is not a valid number"
                             )
        try:
            cls.tank_water = int(water)
        except ValueError:
            raise WaterError(
                             f"Error: setting tank value '{water}' "
                             "is not a valid number"
                             )

    def water_plants(self) -> None:
        if GardenManager.tank_water >= 3:
            print(f"Watering {self.name} - success")
            GardenManager.tank_water -= 3
        else:
            raise WaterError(f"Watering {self.name} - fail")

    def check_plant_health(self) -> None:
        if not self.water_level:
            raise PlantError(
                             f"Error checking {self.name}: Water level "
                             f"'{self.water_level}' is not a valid number"
                             )
        try:
            self.water_level = int(self.water_level)
        except ValueError:
            raise PlantError(
                             f"Error checking {self.name}: Water level "
                             f"'{self.water_level}' is not a valid number"
                             )
        if self.water_level < 1:
            raise PlantError(
                            f"Error checking {self.name}: Water level "
                            f"{self.water_level} is too low (min 1)"
                            )
        elif self.water_level > 10:
            raise PlantError(
                            f"Error checking {self.name}: Water level "
                            f"{self.water_level} is too high (max 10)"
                            )
        if not self.sunlight_hours:
            raise PlantError(
                             f"Error checking {self.name}: Sunlight hours "
                             f"'{self.sunlight_hours}' is not a valid number"
                             )
        try:
            self.sunlight_hours = int(self.sunlight_hours)
        except ValueError:
            raise PlantError(
                             f"Error checking {self.name}: Sunlight hours "
                             f"'{self.sunlight_hours}' is not a valid number"
                             )
        if self.sunlight_hours < 2:
            raise PlantError(
                            f"Error checking {self.name}: Sunlight hours "
                            f"{self.sunlight_hours} is too low (min 2)"
                            )
        elif self.sunlight_hours > 12:
            raise PlantError(
                            f"Error checking {self.name}: Sunlight hours "
                            f"{self.sunlight_hours} is too high (max 12)"
                            )
        print(
              f"{self.name}: healthy (water: {self.water_level}, "
              f"sun: {self.sunlight_hours})"
              )


def test_garden_management(plants: list, tank_water: int) -> None:
    print("=== Garden Management System ===\n")
    try:
        if plants is None:
            raise PlantError("Error: no provided plants")
    except PlantError as e:
        print(e)
        return
    print("Adding plants to garden...")
    for plant in plants[:]:
        if plant is None:
            print("Error adding plant: Plant cannot be None!")
            plants.remove(plant)
        elif not plant.add_plant():
            plants.remove(plant)
    print()
    try:
        GardenManager.set_tank_water(tank_water)
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plant in plants:
                plant.water_plants()
        except WaterError as e:
            print(e)
            print(
                  "Error: not enough water in the tank: "
                  f"'{GardenManager.tank_water}' (min 3)!"
                  )
        finally:
            print("Closing watering system (cleanup)")
    except WaterError as e:
        print(e)
    print("\nChecking plant health...")
    for plant in plants:
        try:
            plant.check_plant_health()
        except PlantError as e:
            print(e)
    print("\nTesting error recovery...")
    try:
        if GardenManager.tank_water < 3:
            raise GardenError("Caught GardenError: Not "
                              "enough water in tank"
                              )
        else:
            print("No error: enough water in tank")
    except GardenError as e:
        print(e)
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


def main() -> None:
    plants = [
            GardenManager("tomato", 5, 8),
            GardenManager("lettuce", 15, 8),
            GardenManager("", 5, 8)
            ]
    tank_water = 6
    test_garden_management(plants, tank_water)


if __name__ == "__main__":
    main()

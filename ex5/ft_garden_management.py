#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    water_tank = 6

    def __init__(self) -> None:
        self.plants: list[dict[str, int | str]] = []

    def set_water_tank(self, water: int) -> None:
        if water.__class__ is not int:
            raise ValueError("Error: water tank should be int")
        else:
            GardenManager.water_tank = water

    def add_plants(self, plants: list[tuple[str, int, int]]) -> None:
        print("Adding plants to garden...")
        for plt in plants[:]:
            try:
                if plt.__class__ is not tuple:
                    plants.remove(plt)
                    raise PlantError(
                        "Error: inside plant list should be "
                        "'tuple[str, int, int]'")
                name, water_level, sunlight_hours = plt
                if name == "":
                    raise PlantError(
                        "Error adding plant: Plant name cannot be empty!")
                if name.__class__ is not str or not name:
                    plants.remove(plt)
                    raise PlantError(
                        f"Error adding plant: Plant name cannot be "
                        f"{name.__class__.__name__}!")
                else:
                    plant: dict[str, int | str] = {
                        "name": name,
                        "water_level": water_level,
                        "sunlight_hours": sunlight_hours
                    }
                    self.plants.append(plant)
                    print(f"Added {name} successfully")
            except PlantError as e:
                print(e)

    def water_plants(self, plants: list[tuple[str, int, int]]) -> None:
        print("Watering plants...")
        print("Opening watering system")
        for plt in plants[:]:
            try:
                name, water_level, _ = plt
                try:
                    water_level = int(water_level)
                except (ValueError, TypeError):
                    plants.remove(plt)
                    raise WaterError(
                        f"Error: water_level of plant {name} should be int")
                if self.water_tank >= 3:
                    print(f"Watering {name} - success")
                    self.water_tank -= 3
                else:
                    print(f"Error watering {name}: Not enough water in tank")
            except GardenError as e:
                print(e)

    def check_plant_health(self, plants: list[tuple[str, int, int]]) -> None:
        print("Checking plant health...")
        for plt in plants:
            try:
                name, water_level, sun = plt
                try:
                    sun = int(sun)
                    water_level = int(water_level)
                except ValueError:
                    raise PlantError(
                        f"Error: sunlight hours of plant {name} should be int")
                if water_level < 1:
                    raise WaterError(
                        f"Error checking {name}: Water level {water_level} "
                        "is too low (min 1)")
                elif water_level > 10:
                    raise WaterError(
                        f"Error checking {name}: Water level {water_level} "
                        "is too high (max 10)")
                elif sun < 2:
                    raise PlantError(
                        f"Error checking {name}: sunlight hours "
                        f"{sun} is too low (min 2)")
                elif sun > 12:
                    raise PlantError(
                        f"Error checking {name}: sunlight hours "
                        f"{sun} is too high (max 12)")
                else:
                    print(f"{name}: healthy (water: {water_level}, "
                          f"sun: {sun})")
            except GardenError as e:
                print(e)


def test_garden_management() -> None:
    manager = GardenManager()
    plants: list[tuple[str, int, int]] = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
        ("", 5, 6)
    ]
    water: int = 9
    if plants.__class__ is not list:
        raise ValueError("Plants should be list")
    manager.set_water_tank(water)
    try:
        print("=== Garden Management System ===\n")
        manager.add_plants(plants)
    except Exception as e:
        print(e)
    print()
    try:
        manager.water_plants(plants)
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
    print()
    try:
        manager.check_plant_health(plants)
    except Exception as e:
        print(e)
    print()
    try:
        print("Testing error recovery...")
        if manager.water_tank < 3:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    try:
        test_garden_management()
    except Exception as e:
        print(e)

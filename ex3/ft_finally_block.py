#!/usr/bin/env python3
def test_watering_system() -> None:
    plants_valid = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    plants_bad = [
        "tomato",
        None
    ]
    try:
        print("=== Garden Watering System ===\n")
        print("Testing normal watering...")
        water_plants(None)
        print("\nTesting with error...")
        water_plants(plants_bad)
        print("\nCleanup always happens, even with errors!")
    except Exception as e:
        print(e)


def water_plants(plant_list: list) -> None:
    if int(plant_list):
        raise TypeError(f"Error: Plant list cannot be '{plant_list}'")
    print("pp")
    try:
        if not plant_list:
            raise TypeError(f"Error: Plant list cannot be '{plant_list}'")
    except TypeError as e:
        print(e)
        return
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Error: Cannot water {plant} - "
                                 "invalid plant!")
            elif plant == "":
                raise ValueError(
                    "Error: Cannot water empty str - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as e:
        print(e)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


if __name__ == "__main__":
    test_watering_system()

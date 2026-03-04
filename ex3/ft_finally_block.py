def test_watering_system() -> None:
    try:
        print("=== Garden Watering System ===\n")
        plants = ["tomato", "lettuce", "carrots"]
        print("Testing normal watering...")
        water_plants(plants)
        plants = ["tomato", None, "carrots"]
        print("\nTesting with error...")
        water_plants(plants)
        print("\nCleanup always happens, even with errors!")
    except Exception as e:
        print(e)


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Error: Cannot water {plant} - "
                                 "invalid plant!")
            elif plant == "":
                raise ValueError("Error: Cannot water empty str - "
                                 "invalid plant!")
            else:
                print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    test_watering_system()

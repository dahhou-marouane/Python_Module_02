def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    try:
        if plant_name == "" or None:
            raise ValueError(f"Error: Plant name cannot be empty!")
        elif plant_name == None:
            print("Error: Plant name cannot be None!")
        else:
            print(f"Plant '{plant_name}' is healthy!")
        if water_level < 1:
            raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
        else:
            print(f"Water level {water_level} is good ")
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        else:
            print(f"Sunlight hours {sunlight_hours} is good")
    except ValueError as e:
        print(e)

def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    try:
        print("Testing good values...")
        check_plant_health("tomato",5, 5)
        print()
    except Exception as e:
        print(e)

    try:
        print("Testing empty plant name...")
        check_plant_health("",0, 0)
        print()
    except Exception as e:
        print(e)

    try:
        print("Testing bad water level...")
        check_plant_health("tomato",15, 5)
        print()
    except Exception as e:
        print(e)
    print("All error raising tests completed!")

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato",5, 0)
        print()
    except Exception as e:
        print(e)

    print("All error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()
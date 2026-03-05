#!/usr/bin/env python3
def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    elif plant_name == None:
        raise ValueError("Error: Plant name cannot be None!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    plant_name = "tomato"
    water_level = 15
    sunlight_hours = 0

    try:
        print("Testing good values...")
        check_plant_health(plant_name, 5, 5)
    except Exception as e:
        print(e)
    print()
    try:
        print("Testing empty plant name...")
        check_plant_health("",0, 0)
        print(f"Plant '{plant_name}' is healthy!")
    except Exception as e:
        print(e)
    print()
    try:
        print("Testing bad water level...")
        check_plant_health("tomato",water_level, sunlight_hours)
        print(f"Water level {water_level} is good", end="\n\n")
    except Exception as e:
        print(e)
    print()
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato",water_level, sunlight_hours)
        print(f"Sunlight hours {sunlight_hours} is good")
    except Exception as e:
        print(e)
    print()
    print("All error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water(water: int) -> None:
    if water > 3:
        print("Enough water in the tank")
        return
    else:
        raise WaterError("Not enough water in the tank!")


def plant_wilting(water: int) -> None:
    if water > 3:
        print("The tomato plant is good")
        return
    else:
        raise PlantError("The tomato plant is wilting!")


def custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_wilting(0)
        print()
    except PlantError as e:

        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        water(0)
        print()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    for test in (plant_wilting, water):
        try:
            test(0)
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    custom_errors()

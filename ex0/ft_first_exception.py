def check_temperature(temp_str) -> int:
    try:
        try:
            formatted = int(temp_str)
        except ValueError:
            raise ValueError(f"Error: '{temp_str}' is not a valid number")
        if formatted > 40:
            raise ValueError(f"Error: {formatted}°C is too hot for plants (max 40°C)")
        if formatted < 0:
            raise ValueError(f"Error: {formatted}°C is too cold for plants (min 0°C)")
    except ValueError as e:
        raise
    return formatted

def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    tests = None
    for i in tests:
        print(f"Testing temperature: {i}")
        try:
            formatted = check_temperature(i)
            print(f"Temperature {formatted}°C is perfect for plants!\n")
        except ValueError as e:
            print(e, end="\n\n")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(e)
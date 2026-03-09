#!/usr/bin/env python3
def check_temperature(temp_str: str) -> int:
    try:
        try:
            formatted = int(temp_str)
        except ValueError:
            raise ValueError(
                f"Error: '{temp_str}' is not a "
                "valid number")
        if formatted > 40:
            raise ValueError(
                f"Error: {formatted}°C is too hot "
                "for plants (max 40°C)")
        if formatted < 0:
            raise ValueError(
                f"Error: {formatted}°C is too cold "
                "for plants (min 0°C)")
    except ValueError:
        raise
    return formatted


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50",]
    try:
        if tests is None:
            raise ValueError(
                "Error: 'NoneType' is not a valid number")
        for i in tests:
            if not i:
                raise ValueError(
                    f"Error: '{i}' is not a valid number")
            print(f"Testing temperature: {i}")
            try:
                formatted = check_temperature(None)
                print(
                    f"Temperature {formatted}°C is perfect for plants!\n")
            except ValueError as e:
                print(e, end="\n\n")
    except Exception as e:
        print(e)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

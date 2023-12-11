def temperature_converter():
    try:
        value = float(input("Enter the temperature value: "))
        source_unit = input("Enter the source unit (Celsius or Fahrenheit): ").lower()
        target_unit = input("Enter the target unit (Celsius or Fahrenheit): ").lower()

        if source_unit == "celsius" and target_unit == "fahrenheit":
            result = (value * 9/5) + 32
        elif source_unit == "fahrenheit" and target_unit == "celsius":
            result = (value - 32) * 5/9
        else:
            print("Unsupported units for temperature conversion.")
            return

        print(f"{value} {source_unit} is equal to {result} {target_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

def length_converter():
    try:
        value = float(input("Enter the length value: "))
        source_unit = input("Enter the source unit (Meters or Feet): ").lower()
        target_unit = input("Enter the target unit (Meters or Feet): ").lower()

        if source_unit == "meters" and target_unit == "feet":
            result = value * 3.28084
        elif source_unit == "feet" and target_unit == "meters":
            result = value / 3.28084
        else:
            print("Unsupported units for length conversion.")
            return

        print(f"{value} {source_unit} is equal to {result} {target_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for length.")

def weight_converter():
    try:
        value = float(input("Enter the weight value: "))
        source_unit = input("Enter the source unit (Kilograms or Pounds): ").lower()
        target_unit = input("Enter the target unit (Kilograms or Pounds): ").lower()

        if source_unit == "kilograms" and target_unit == "pounds":
            result = value * 2.20462
        elif source_unit == "pounds" and target_unit == "kilograms":
            result = value / 2.20462
        else:
            print("Unsupported units for weight conversion.")
            return

        print(f"{value} {source_unit} is equal to {result} {target_unit}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for weight.")

def main():
    print("Welcome to the Unit Converter!")
    print("1. Temperature Converter\n2. Length Converter\n3. Weight Converter")

    choice = input("Select a converter (1, 2, or 3): ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        weight_converter()
    else:
        print("Invalid choice. Please select a valid converter (1, 2, or 3).")

if __name__ == "__main__":
    main()

class UnitConverter:

    def meter_to_kilometer(self, meter):
        return meter / 1000

    def kilometer_to_meter(self, kilometer):
        return kilometer * 1000

    def centimeter_to_meter(self, centimeter):
        return centimeter / 100

    def meter_to_centimeter(self, meter):
        return meter * 100

    def kilogram_to_gram(self, kilogram):
        return kilogram * 1000

    def gram_to_kilogram(self, gram):
        return gram / 1000

    def kilogram_to_pound(self, kilogram):
        return kilogram * 2.204

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


def main():
    unit = UnitConverter()

    print("=== Unit Converter ===")

    while True:

        print("""
1. Length Converter
2. Weight Converter
3. Temperature Converter
4. Exit
""")

        main_choice = input("Enter your choice: ")

        try:

            if main_choice == '1':

                print("""
1. Meter → Kilometer
2. Kilometer → Meter
3. Centimeter → Meter
4. Meter → Centimeter
""")

                length_choice = input("Enter your choice: ")

                if length_choice == '1':
                    meter = float(input("Enter Meter: "))
                    print(f"{meter} Meter -> {unit.meter_to_kilometer(meter):.2f} Kilometer")

                elif length_choice == '2':
                    kilometer = float(input("Enter Kilometer: "))
                    print(f"{kilometer} Kilometer -> {unit.kilometer_to_meter(kilometer):.2f} Meter")

                elif length_choice == '3':
                    centimeter = float(input("Enter Centimeter: "))
                    print(f"{centimeter} Centimeter -> {unit.centimeter_to_meter(centimeter):.2f} Meter")

                elif length_choice == '4':
                    meter = float(input("Enter Meter: "))
                    print(f"{meter} Meter -> {unit.meter_to_centimeter(meter):.2f} Centimeter")

                else:
                    print("Invalid choice!")

            elif main_choice == '2':

                print("""
1. Kilogram → Gram
2. Gram → Kilogram
3. Kilogram → Pound
""")

                weight_choice = input("Enter your choice: ")

                if weight_choice == '1':
                    kg = float(input("Enter Kilogram: "))
                    print(f"{kg} Kg -> {unit.kilogram_to_gram(kg):.2f} Gram")

                elif weight_choice == '2':
                    gram = float(input("Enter Gram: "))
                    print(f"{gram} Gram -> {unit.gram_to_kilogram(gram):.2f} Kg")

                elif weight_choice == '3':
                    kg = float(input("Enter Kilogram: "))
                    print(f"{kg} Kg -> {unit.kilogram_to_pound(kg):.2f} Pound")

                else:
                    print("Invalid choice!")

            elif main_choice == '3':

                print("""
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
""")

                temp_choice = input("Enter your choice: ")

                if temp_choice == '1':
                    celsius = float(input("Enter Celsius: "))
                    print(f"{celsius}°C -> {unit.celsius_to_fahrenheit(celsius):.2f}°F")

                elif temp_choice == '2':
                    fahrenheit = float(input("Enter Fahrenheit: "))
                    print(f"{fahrenheit}°F -> {unit.fahrenheit_to_celsius(fahrenheit):.2f}°C")

                else:
                    print("Invalid choice!")

            elif main_choice == '4':
                print("Thanks for visiting!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")


if __name__ == "__main__":
    main()
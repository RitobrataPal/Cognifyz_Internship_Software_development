def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Temperature Converter")
    
    # Accept temperature input
    temp = float(input("Enter the temperature value: "))
    
    # Allow users to choose conversion direction
    print("Choose conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        # Convert Celsius to Fahrenheit
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    elif choice == '2':
        # Convert Fahrenheit to Celsius
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        
# Test the program
temperature_converter()

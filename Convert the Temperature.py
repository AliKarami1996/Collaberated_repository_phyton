temp_celsius = float(input("Enter the temperature in celsius: "))

kelvin = temp_celsius + 273.15
fahrenheit = temp_celsius * 1.80 + 32.00

format_kelvin = format(kelvin)
format_fahrenheit = format(fahrenheit)

temperature_array = [format_kelvin, format_fahrenheit]


print(temperature_array)

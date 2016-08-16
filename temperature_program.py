def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0

def above_freezing(celsius):
    return celsius > 0

fahrenheit = float(input('Enter the temperature in degrees fahrenheit: '))
celsius = convert_to_celsius(fahrenheit)
if above_freezing(celsius):
    print('It is above freezing.')
else:
    print('It is below freezing.')

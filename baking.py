import temperature_program

def get_preheating_instruction(fahrenheit):
    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F ('+ cels +' degrees C).'
fahr = float(input('Enter the baking temperature in degrees Fahrenheit: '))
print(get_preheating_instruction(fahr))

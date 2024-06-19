def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32  # Fórmula de conversión
    return fahrenheit
celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
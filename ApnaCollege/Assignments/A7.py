"""Ask the user for a temperature in Celsius (string input).
 Convert it to float, then calculate and print temperature in Fahrenheit.

Conversion formula: Fahrenheit Temp = (Celsius Temp * (9/5)) + 32
"""

temp = input("Enter the temperature in celcius: ")

fer_temp = (float(temp) * (9 / 5)) + 32

print(fer_temp)

''' Ask the user for: Principal (P), Rate (R), Time (T).
Convert all to float and compute simple interest: 
SI = (P * R * T )/100
'''

p = float(input("Enter the principal: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))

SI = (p*r*t)/100

print(SI)
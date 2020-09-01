temperature = int(input("Enter temperature: "))
response = input("Enter unit in F/f or C/c: ")
if response == 'F' or response == 'f' :
  fahrenheit = (temperature - 32) * 5/9
  print (f"{temperature}\N{degree sign} in Fahrenheit is equivalent to {fahrenheit}\N{degree sign} Celsius.")
elif response == 'C' or response == 'c':
  celsius = (temperature * 9/5) + 32
  print (f"{temperature}\N{degree sign} in Celsius is equivalent to {celsius}\N{degree sign} Fahrenheit.")
else:
  print ("Invalid unit({response}).")

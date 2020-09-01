temperature = int(input("Enter temperature: "))
response = input("Enter unit in F/f or C/c: ")
if response == 'F' or response == 'f' :
  fahrenheit = (temperature - 32) * 5/9
  print (f"{temperature}\N{degree sign} in fahrenheit is equivalent to {fahrenheit}\N{degree sign} celsius.")
elif response == 'C' or response == 'c':
  celsius = (temperature * 9/5) + 32
  print (f"{temperature}\N{degree sign} in celsius is equivalent to {celsius}\N{degree sign} fahrenheit.")
else:
  print ("Invalid unit(bad).")

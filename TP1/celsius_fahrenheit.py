celsius = 0
fahrenheit = 0
Convert = input("Ecrit Celsius pour une convertion de fahrenheit a celsius. Ecrit Fahrenheit pour une convertion de celsuis a fahreneith.")
if Convert == "Celsius":
    fahrenheit += int(input("Combiens de Fahreneith ? "))
    celsius += (fahrenheit + -32)/1.8
    print(celsius," degrès Celsius" )
elif Convert == "Fahrenheit":
    celsius += int(input("Combiens de Celsius ?"))
    fahrenheit += celsius*1.8 + 32
    print(fahrenheit, "degrès Fahrenheit")

personas = [["M", 10], ["F", 20], ["M", 30], ["F", 40], ["M", 50], ["F", 60], ["M", 70], ["F", 80], ["M", 90], ["F", 100]]

for persona in personas:
    genero = persona[0]
    edad = persona[1]
    
    if edad >= 70:
        print(f"Persona de género {genero} con edad {edad} es considerada de tercera edad.")
        print("Vacuna tipo C")
    elif edad >= 16 and edad <= 70 and genero == "F":
        print(f"Persona de género {genero} con edad {edad} es considerada adulta.")
        print("Vacuna tipo B")
    elif genero == "M": 
        print(f"Persona de género {genero} con edad {edad} es considerada adulta.")
        print("Vacuna tipo A")
    elif edad <= 16:
        print(f"Persona de género {genero} con edad {edad} es considerada menor de edad.")
        print("Vacuna tipo A")
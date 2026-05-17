animales = [{
    "nombre": "Perro",
    "genero": "M"
}, {
    "nombre": "Gato",
    "genero": "F"
},
    {
    "nombre": "Pájaro",
    "genero": "M"
}, {
    "nombre": "Elefante",
    "genero": "F"
}, {
    "nombre": "Tigre",
    "genero": "M"
}]

M = 0
F = 0

for animal in animales:
    if animal["genero"] == "M":
        M += 1
    elif animal["genero"] == "F":
        F += 1
        
print(f"Cantidad de animales machos: {M}")
print(f"Cantidad de animales hembras: {F}")
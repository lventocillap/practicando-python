
pelotas = ["S", "M", "L", "M", "S", "L", "M", "M", "L", "M", "S", "L", "M", "S", "L", "M", "S"]

for i in range(len(pelotas)):
    tamaño_pelota = pelotas[i]
    if tamaño_pelota == "S":
        print(f"Pelota {i+1}: Tamaño pequeño")
    elif tamaño_pelota == "M":
        print(f"Pelota {i+1}: Tamaño mediano")
    elif tamaño_pelota == "L":
        print(f"Pelota {i+1}: Tamaño grande")
    else:
        print("Tamaño de pelota no válido")
        break
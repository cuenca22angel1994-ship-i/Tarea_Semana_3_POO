def registrar_mascota():
    print("=== Registro de Mascota ===")
    nombre = input("Ingrese el nombre: ").strip()
    especie = input("Ingrese la especie (ej: perro, gato, loro): ").strip()
    
    while True:
        try:
            edad = int(input("Ingrese la edad en años: "))
            if edad >= 0:
                break
            else:
                print("La edad no puede ser negativa. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")
    
    return nombre, especie, edad

def mostrar_mascota(datos):
    print("\n=== Información de la Mascota ===")
    print(f"Nombre:   {datos[0]}")
    print(f"Especie:  {datos[1]}")
    print(f"Edad:     {datos[2]} años")

def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)

if __name__ == "__main__":
    main()
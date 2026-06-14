from mascota import Mascota

def main():
    
    mascota1 = Mascota("Rex", "Perro", 3)
    mascota2 = Mascota("Coco", "Gato", 1)

    print("=== DATOS DE LA PRIMERA MASCOTA ===")
    mascota1.mostrar_informacion()
    print(f"Sonido: {mascota1.hacer_sonido()}\n")

    print("=== DATOS DE LA SEGUNDA MASCOTA ===")
    mascota2.mostrar_informacion()
    print(f"Sonido: {mascota2.hacer_sonido()}")

if __name__ == "__main__":
    main()
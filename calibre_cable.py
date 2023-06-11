from math import log

repetir = True

while repetir:
    print("\n######## Determinación de calibre de un conductor eléctrico (mm a AWG) ########\n")

    print("Ingresa lo siguiente...")
    diametro_mm = float(input("Diámetro (mm): "))

    if 0.015 < diametro_mm < 11.684:
        awg = round(((log(diametro_mm)-log(11.684))/(log(0.89)))-3)
        print(f"El calibre AWG correspondiente al diámetro {diametro_mm} mm es: {awg}")
    else:
        print(f"El diámetro {diametro_mm} mm no está dentro del rango válido (0.015 - 11.684 mm)\n")

    repetir = input("Nuevo cálculo (s/n): ").lower() == 's'

#Fabrica de refacciones.

while True:
    print("1. Ejecutar software")
    print("2. Cerrar software")
    
    opcion = int(input("\nSeleccione una alternativa válida: "))
    if opcion == 1:
        precio_unitario_pieza = int(input("Introduzca el precio de la pieza: "))
        cantidad_piezas = int(input("Introduzca la cantidad de piezas a comprar: "))
        monto_total = precio_unitario_pieza * cantidad_piezas

        if monto_total > 500000:
            inversion_empresa = monto_total * 0.55
            prestamo_bancario = monto_total * 0.3
            credito_fabricante = monto_total * 0.15
        
        elif monto_total < 500000:
            inversion_empresa = monto_total * 0.7
            prestamo_bancario = monto_total * 0
            credito_fabricante = monto_total * 0.3
        
        else:
            print("\nVerifique la información suministrada.")
        
        interes_fabricante = credito_fabricante * 0.2
        total_credito_fabricante = interes_fabricante + credito_fabricante
        print(f"\nCantidad de piezas a comprar: {cantidad_piezas}")
        print(f"Precio unitario de pieza a comprar: {precio_unitario_pieza}")
        print(f"Monto total de la compra: {monto_total}")
        print(f"Inversión de la empresa en la compra: {inversion_empresa}")
        print(f"Préstamo al banco: {prestamo_bancario}")
        print(f"Crédito al fabricante (incluye intereses): {total_credito_fabricante}\n")


    elif opcion == 2:
        print("\nCerrando el programa...")
        break

    else:
        print("Verifique la información suministrada.\n")
        
        

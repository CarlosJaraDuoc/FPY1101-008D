import os
import time
clean = "cls"
os.system(clean)
sushi = 0
sushiP = 0
sushiO = 0
sushiV = 0
sushiA = 0
valorP = 0
valorO = 0
valorV = 0
valorA = 0
total = 0
descuento = 0
respuesta = 1
while True:
    volver = ""
    try:
        time.sleep(1)
        os.system(clean)
        print("Bienvenido al delivery de Sushis")
        print("Seleccione el tipo de Sushi: ")
        print("1. Pikachu Roll $4500 ")
        print("2. Otaku Roll $5000 ")
        print("3. Pulpo Venenoso Roll $5200 ")
        print("4. Anguila Eléctrica Roll $4800 ")
        print("5. Proceder a pago")
        tipo = int(input())
        if tipo == 1:
            sushiP += 1
            sushi += 1
            valorP = 4500
            continue
        elif tipo == 2:
            sushiO += 1
            sushi += 1
            valorO = 5000
            continue
        elif tipo == 3:
            sushiV += 1
            sushi += 1
            valorV = 5200
            continue
        elif tipo == 4:
            sushiA += 1
            sushi += 1
            valorA = 4800
            continue
        elif tipo == 5:
            print()
        else:
            print("Ingrese un valor dentro del rango (1-5)")
            time.sleep(1)
            continue
    except ValueError:
        print("Ingrese un número válido")
        time.sleep(1)
        continue
    os.system(clean)
    time.sleep(1)
    print("¿Posee código de descuento?")
    print("1. Si")
    print("2. No")
    codigo = int(input())
    total = sushiP * valorP + sushiO * valorO + sushiV * valorV + sushiA * valorA
    while codigo == 1:
        try:
            os.system(clean)
            time.sleep(1)
            nomDescuento = input("Ingrese el código de descuento: ")
            if nomDescuento == "soyotaku":
                descuento = total * 0.10
                print ("Ha obtenido un 10\%de descuento")
                break
            else:
                print("código no válido")
                print("¿Desea reingresar el código?")
                print ("V = Sí")
                print ("X = Volver al menú")
                volver = input("")
                if volver == "V":
                    continue
                else:
                    break
        except ValueError:
            print("No ha ingresado un valor correcto")
    else:
        os.system(clean)
        time.sleep(1)
    if volver == "X":
        continue
    os.system(clean)
    time.sleep(1)
    print ("******************************")
    print(f"TOTAL PRODUCTOS:{sushi}")
    print ("******************************")
    print(f"Pikachu Roll : {sushiP}")
    print(f"Otaku Roll : {sushiO}")
    print(f"Pulpo Venenoso Roll : {sushiV}")
    print(f"Anguila Eléctrica Roll : {sushiA}")
    print ("******************************")
    print(f"Subtotal por pagar: ${total}")
    print("Descuento por código: $",int(descuento))
    total -= descuento
    print("TOTAL: $",int(total))
    print("¿Desea realizar otro pedido?")
    print("1. Si")
    print("2. No")
    try:
        respuesta = int(input())
        if respuesta == 2:
            break
        elif respuesta == 1:
            os.system(clean)
            time.sleep(1)
            sushi = 0
            sushiP = 0
            sushiO = 0
            sushiV = 0
            sushiA = 0
            valorP = 0
            valorO = 0
            valorV = 0
            valorA = 0
            total = 0
            descuento = 0
            respuesta = 1
            continue
        else:
            print("Ingrese un número dentro del rango (1 - 2)")
    except ValueError:
        print("Ingrese un número válido")
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): 
    return "Error: No se puede dividir entre cero" if b == 0 else a / b

def calculadora():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
            
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor, ingresa números válidos.")
                continue
                
            if opcion == '1': print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == '2': print(f"Resultado: {restar(num1, num2)}")
            elif opcion == '3': print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == '4': print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Iniciar la calculadora
calculadora()
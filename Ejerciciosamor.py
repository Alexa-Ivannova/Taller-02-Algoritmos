# Validación de rango numérico Dada la variable predefinida numero, determina si su valor está entre 1 y 10 (ambos inclusive). Si no lo está, indica que el número es inválido.

# numero = int(input("Ingresa un número: "))

# if numero == 1 or numero <= 10:
#     print("número valido")
# else:
#     print("número invalido")


# Verificación de credenciales Con las variables user y pwd ya asignadas, comprueba si coinciden exactamente con las constantes USUARIO_OK y CLAVE_OK. Dependiendo del resultado, indica si el acceso está concedido o denegado.

# user = "pepita"
# pwd = 123456789

# USUARIO_OK = str(input("Ingrese usuario: "))
# CLAVE_OK = int(input("Ingrese clave númerica: "))

# if user == USUARIO_OK and pwd == CLAVE_OK:
#     print("Acceso correcto")
# else:
#     print("El usuario o la constraseña son incorrectos")


# Simulación de botón y LED Usando la variable boton_val (0 = no presionado, 1 = presionado) y la variable booleana led_estado, implementa la lógica que encienda o apague el LED virtual según el estado del botón.

# boton_val = int(input("Indique si el estado del botón, si esta presionado marque 1 y si no esta presionado marque 0: "))
# led_estad = 1
# led = "encendido"

# if boton_val == 0 or boton_val <= led_estad:
#     if boton_val == led_estad:
#         print(led)
#     else:
#         led= "apagado"
#         print(led)
# else:
#     print("El valor indicado es incorrecto")

    # Detección de umbral en sensor analógico Con la lectura simulada valor_sensor y el valor umbral UMBRAL, decide si el sensor supera el umbral. En función de ello, actualiza led_estado y reporta si se detectó un valor alto o si permanece dentro de rango.

valor_sensor = int(input("Ingrese el valor del sensor: "))
UMBRAL = 10
led_estado = ""

if valor_sensor <= UMBRAL:
    led_estado = "El valor permanece dentro del rango"
    print(led_estado)
else:
    led_estado = "Se ha detectado un valor alto"
    print(led_estado)
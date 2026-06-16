"""Tu Misión
Escribe un script en Python que haga lo siguiente:

Contabilizar: Crea un diccionario llamado reporte_cargas 
donde las llaves sean los nombres de los empleados y los 
valores sean la suma total de puntos que cada uno acumuló.
Identificar al "MVP": Encuentra quién fue la persona que 
más carga de trabajo realizó (el total de puntos más alto) 
y cuánto fue.
Calcular el Promedio: Calcula el promedio de carga de todo 
el equipo.
Alerta de Sobrecarga: Imprime un mensaje para cualquier 
empleado que haya superado los 10 puntos, diciendo: 
"Alerta: [Nombre] está sobrecargado con [Puntos] puntos".

Reglas del Reto
Debes usar un bucle for para procesar la lista registros.
Debes usar el método .split(':') para separar el nombre del 
puntaje (recuerda convertir el puntaje a int o float).
Debes usar el patrón counts.get(name, 0) o un if/else para 
ir sumando los puntos en el diccionario."""
registros = [
    "Ana:3", "Juan:5", "Ana:2", "Maria:4", "Juan:2",
    "Maria:4", "Ana:5", "Maria:2", "Juan:4"]
#lectura de cargas y diccionario reporte_cargas

reporte_carga=dict()
for registro in registros:
    nombre, puntos_str = registro.split(":")
    puntos=int(puntos_str)
    reporte_carga[nombre]=reporte_carga.get(nombre,0)+ puntos
print(reporte_carga)

#mvp
a=0
MVP= mvpnm, mvppt
for reporte in reporte_cargas:
    if a < reporte_cargas[reporte]:
        MVP= reporte, reporte_cargas[reporte]
        
#promedio

total_cargas=sum(reporte_cargas.values())
empleados=len(reporte_cargas)
promedio= total_cargas / empleados

#imprimir
print("El promedio de cargas por empleado es ",promedio," puntos")
print("El MVP es", MVP)

#alerta de sobrecarga
for empleado, puntos in reporte_cargas.items():
    if puntos > 10:
        print(f"Alerta: {empleado} está sobrecargado con {puntos} puntos")

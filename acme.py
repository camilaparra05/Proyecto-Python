from Interfaz.menu2 import menu
from Interfaz import funciones
from inicio.Inicio import inicio_sesion

user = input("Ingresar su usuario: ")
password = input("Ingresar su contraseña: ")
inicio_sesion(user, password)
 

arch = funciones.cargar_archivo()
    
while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            funciones.registrar_grupo(arch)
        elif opcion == "2":
            funciones.registrar_modulo(arch)
        elif opcion == "3":
            funciones.registrar_estudiante(arch)
        elif opcion == "4":
            funciones.registrar_docente(arch)
        elif opcion == "5":
            pass
            # codigo_estudiante, codigo_modulo = registrar_asistencia(arch)
            # asistencia(arch, codigo_estudiante, codigo_modulo)
        elif opcion == "6":
            funciones.consultar_estudiantes_por_grupo()
        elif opcion == "7":
            funciones.consultar_estudiantes_por_modulo()
        elif opcion == "8":
            funciones.consultar_docentes_por_modulo()
        elif opcion == "9":
            funciones.consultar_estudiantes_por_docente()
        elif opcion == "10":
            funciones.generar_informe_asistencia()
        elif opcion == "11":
            print("Saliendo del sistema...")
            funciones.guardar_informacion(arch)
            break
        else:
            print("Opción no válida. Intente nuevamente.")


 

menu()
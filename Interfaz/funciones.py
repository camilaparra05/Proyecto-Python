import json
import os
from datetime import datetime

Archivo_data = os.path.join(os.path.dirname(__file__), 'funciones.json')

def cargar_archivo():
    try:
        with open(Archivo_data, "r") as fd:
            arch = json.load(fd)
            return arch
    except FileNotFoundError:
        return {
            "GRUPOS": [],
            "ESTUDIANTES": [],
            "MODULOS": [],
            "DOCENTES": [],
            "ASISTENCIAS": [],
        }
    except json.JSONDecodeError:
        return {
            "GRUPOS": [],
            "ESTUDIANTES": [],
            "MODULOS": [],
            "DOCENTES": [],
            "ASISTENCIAS": [],
        }

def guardar_informacion(arch):
    with open(Archivo_data, "w") as fd:
        json.dump(arch, fd,)

def registrar_grupo(arch):
    codigo = input("Ingrese el codigo del grupo:  ")
    nombre = input("Ingrese el nombre del grupo:  ")
    sigla = input("Ingrese la sigla del grupo:  ")
    grupo = {'codigo': codigo, "nombre": nombre, "sigla": sigla}
    arch["GRUPOS"].append(grupo)
    guardar_informacion(arch)
    

def registrar_modulo(arch):
    codigoM = input("Ingrese el codigo del modulo:  ")
    nombreM = input("Ingrese el nombre del modulo:  ")
    duracionM = input("Ingrese la duracion en semanas:  ")
    modulo = {'codigoM': codigoM, "nombreM": nombreM, "duracionM": duracionM}
    arch["MODULOS"].append(modulo)
    guardar_informacion(arch)

def registrar_estudiante(arch):
    codigo = input("Ingrese el codigo del estudiante:  ")
    nombre = input("Ingrese el nombre del estudiante:  ")
    edad = input("Ingrese la edad del estudiante:  ")
    sexo = input("Ingrese el sexo del estudiante:  ")
    estudiante = {'codigo': codigo, "nombre": nombre, "edad": edad, "sexo": sexo}
    arch["ESTUDIANTES"].append(estudiante)
    guardar_informacion(arch)

def registrar_docente(arch):
    nombre = input("Ingrese el nombre del docente:  ")
    cedula = input("Ingrese la cedula:  ")
    docente = {'nombre': nombre, "cedula": cedula}
    arch["DOCENTES"].append(docente)
    guardar_informacion(arch)

def registrar_asistencia(arch):
    codigo_estudiante = input("Ingrese el codigo del estudiante:  ")
    codigo_modulo = input("Ingrese el codigo del modulo:  ")
    asistencia={"codigo_estudiante": codigo_estudiante, "codigo_modulo":  codigo_modulo}
    arch["ASISTENCIA"].append(asistencia)
    return codigo_estudiante, codigo_modulo

def consultar_estudiantes_por_grupo():
    codigo_grupo = input("Ingrese el código del grupo: ")
    return codigo_grupo

def consultar_estudiantes_por_modulo():
    codigo_modulo = input("Ingrese el código del módulo: ")
    return codigo_modulo

def consultar_docentes_por_modulo():
    codigo_modulo = input("Ingrese el código del módulo: ")
    return codigo_modulo

def consultar_estudiantes_por_docente():
    cedula_docente = input("Ingrese la cédula del docente: ")
    codigo_modulo = input("Ingrese el código del módulo: ")
    return cedula_docente, codigo_modulo


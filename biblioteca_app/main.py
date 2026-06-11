# ==========================================================
# ARCHIVO PRINCIPAL (main.py)
# ----------------------------------------------------------
# Este archivo representa el punto de inicio del programa.
#
# Su función es:
# 1. Importar las clases necesarias.
# 2. Crear objetos Libro y Usuario.
# 3. Crear una instancia de Biblioteca.
# 4. Registrar los libros y usuarios.
# 5. Mostrar la información almacenada.
#
# Este ejemplo permite observar cómo interactúan varias
# clases dentro de un programa orientado a objetos.
# ==========================================================


# ----------------------------------------------------------
# IMPORTACIÓN DE CLASES
# ----------------------------------------------------------
# Se importan las clases definidas en otros módulos del
# proyecto para poder utilizarlas en este archivo.
# ----------------------------------------------------------

from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca


# ==========================================================
# CREACIÓN DE OBJETOS LIBRO
# ==========================================================
# A partir de la clase Libro se crean dos objetos diferentes.
#
# Aunque ambos pertenecen a la misma clase, cada objeto posee
# sus propios valores para título, autor e ISBN.
# ==========================================================

libro1 = Libro(
    "Python para Principiantes",
    "Juan Pérez",
    "ISBN001"
)

libro2 = Libro(
    "Programación Orientada a Objetos",
    "María Gómez",
    "ISBN002"
)


# ==========================================================
# CREACIÓN DE OBJETO USUARIO
# ==========================================================
# Se crea un objeto de la clase Usuario con información
# específica de una persona registrada en la biblioteca.
# ==========================================================

usuario1 = Usuario(
    "Carlos López",
    "carlos@correo.com"
)


# ==========================================================
# CREACIÓN DE LA BIBLIOTECA
# ==========================================================
# Se instancia un objeto Biblioteca.
#
# Este objeto actuará como administrador central de los
# libros y usuarios registrados en el sistema.
# ==========================================================

biblioteca = Biblioteca()


# ==========================================================
# REGISTRO DE LIBROS
# ==========================================================
# Los libros creados previamente son agregados a la
# colección interna de la biblioteca.
# ==========================================================

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)


# ==========================================================
# REGISTRO DE USUARIOS
# ==========================================================
# Se registra el usuario dentro de la biblioteca utilizando
# el método correspondiente.
# ==========================================================

biblioteca.agregar_usuario(usuario1)


# ==========================================================
# VISUALIZACIÓN DE INFORMACIÓN
# ==========================================================
# Finalmente se muestran en pantalla todos los libros y
# usuarios almacenados en la biblioteca.
#
# Los métodos mostrar_libros() y mostrar_usuarios()
# recorren las listas internas e imprimen cada objeto.
# ==========================================================

print("=== LIBROS REGISTRADOS ===")
biblioteca.mostrar_libros()

print("\n=== USUARIOS REGISTRADOS ===")
biblioteca.mostrar_usuarios()
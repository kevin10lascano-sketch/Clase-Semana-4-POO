# ==========================================================
# CLASE: Libro
# ----------------------------------------------------------
# Esta clase representa un libro dentro de un sistema de
# biblioteca digital.
#
# Cada objeto creado a partir de esta clase almacenará la
# información correspondiente a un libro específico.
#
# Atributos:
# - titulo : Nombre del libro.
# - autor  : Nombre del autor del libro.
# - isbn   : Código único de identificación del libro.
#
# Ejemplo de creación:
#
# libro1 = Libro(
#     "Cien años de soledad",
#     "Gabriel García Márquez",
#     "9780307474728"
# )
# ==========================================================

class Libro:

    def __init__(self, titulo, autor, isbn):
        """
        Constructor de la clase Libro.

        Este método se ejecuta automáticamente cuando se crea
        un nuevo objeto Libro.

        Parámetros:
            titulo (str): Título del libro.
            autor (str): Nombre del autor.
            isbn (str): Código ISBN del libro.

        Los valores recibidos se almacenan dentro del objeto
        utilizando atributos de instancia.
        """

        # Almacena el título del libro.
        self.titulo = titulo

        # Almacena el nombre del autor.
        self.autor = autor

        # Almacena el código ISBN.
        self.isbn = isbn

    def mostrar_informacion(self):
        """
        Devuelve una cadena de texto con la información
        principal del libro.

        Retorna:
            str: Texto con el título y el autor.

        Ejemplo de salida:
            Título: El Principito | Autor: Antoine de Saint-Exupéry
        """
        return f"Título: {self.titulo} | Autor: {self.autor}"

    def __str__(self):
        """
        Método especial utilizado por Python para definir
        cómo se mostrará el objeto cuando se imprima con
        la función print().

        Retorna:
            str: Representación amigable del libro.

        Ejemplo:
            print(libro)

        Salida:
            El Principito - Antoine de Saint-Exupéry
        """
        return f"{self.titulo} - {self.autor}"
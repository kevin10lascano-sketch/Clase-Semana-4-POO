# ==========================================================
# CLASE: Biblioteca
# ----------------------------------------------------------
# Esta clase representa una biblioteca digital encargada de
# administrar colecciones de libros y usuarios.
#
# Su función principal es almacenar, organizar y mostrar
# la información de los libros y usuarios registrados en
# el sistema.
#
# La biblioteca utiliza listas para guardar múltiples
# objetos creados a partir de las clases Libro y Usuario.
#
# Atributos:
# - libros   : Lista que almacena los objetos Libro.
# - usuarios : Lista que almacena los objetos Usuario.
#
# Ejemplo de creación:
#
# biblioteca = Biblioteca()
# ==========================================================

class Biblioteca:

    def __init__(self):
        """
        Constructor de la clase Biblioteca.

        Este método se ejecuta automáticamente al crear un
        nuevo objeto Biblioteca.

        Inicializa dos listas vacías que permitirán almacenar
        libros y usuarios durante la ejecución del programa.
        """

        # Lista donde se almacenarán los objetos Libro.
        self.libros = []

        # Lista donde se almacenarán los objetos Usuario.
        self.usuarios = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la colección de la biblioteca.

        Parámetros:
            libro (Libro): Objeto de tipo Libro que será
                           almacenado en la biblioteca.

        Funcionamiento:
            Utiliza el método append() para insertar el
            objeto al final de la lista de libros.
        """

        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.

        Parámetros:
            usuario (Usuario): Objeto de tipo Usuario que
                               será agregado al sistema.

        Funcionamiento:
            Utiliza el método append() para almacenar el
            usuario en la lista correspondiente.
        """

        self.usuarios.append(usuario)

    def mostrar_libros(self):
        """
        Muestra todos los libros registrados en la biblioteca.

        Funcionamiento:
            Recorre la lista de libros utilizando un ciclo
            for y muestra cada objeto mediante print().

        Nota:
            Cuando se imprime un objeto Libro, Python ejecuta
            automáticamente el método especial __str__()
            definido en dicha clase.
        """

        for libro in self.libros:
            print(libro)

    def mostrar_usuarios(self):
        """
        Muestra todos los usuarios registrados en la biblioteca.

        Funcionamiento:
            Recorre la lista de usuarios utilizando un ciclo
            for y muestra cada objeto mediante print().

        Nota:
            Cuando se imprime un objeto Usuario, Python ejecuta
            automáticamente el método especial __str__()
            definido en dicha clase.
        """

        for usuario in self.usuarios:
            print(usuario)
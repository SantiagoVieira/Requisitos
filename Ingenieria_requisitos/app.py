class Administrador:
    def __init__(self, coordinadores, docentes, usuario, contraseña):
        self.coordinadores = coordinadores
        self.docentes = docentes
        self.usuario = usuario
        self.contraseña = contraseña
        self.docentes_programas = {}
        self.lista_docentes = []
        self.investigacion = ['Investigacion 1', 'Investigacion 2', 'Investigacion 3']
        self.asignaciones_investigacion = {}

    def autenticacion_coordinador(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == self.usuario and contraseña == self.contraseña:
            print("Autenticación exitosa.")
        else:
            print("Credenciales inválidas.")

    def autenticacion_docente(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == self.usuario and contraseña == self.contraseña:
            print("Autenticación exitosa.")
        else:
            print("Credenciales inválidas.")

    def agregar_docente_programa(self, docente, programa):
        if programa not in self.docentes_programas:
            self.docentes_programas[programa] = []
        self.docentes_programas[programa].append(docente)

    def crear_lista_docentes(self, docente):
        self.lista_docentes.append(docente)


class Coordinador(Administrador):
    def __init__(self, nombre, usuario, contraseña):
        super().__init__(coordinadores=[], docentes=[], usuario=usuario, contraseña=contraseña)
        self.nombre = nombre

    def clasificar_docente_programa(self, programa):
        if programa in self.docentes_programas:
            return [docente for docente in self.docentes_programas[programa]]
        else:
            return []

    def clasificar_docente_gdi(self):
        for investigacion in self.investigacion:
            docente = Docente('usuario', 'contraseña', 'Nombre del docente')
            self.asignaciones_investigacion[investigacion] = docente

class Docente(Administrador):
    def __init__(self, usuario, contraseña, nombre):
        super().__init__(coordinadores=[], docentes=[], usuario=usuario, contraseña=contraseña)
        self.nombre = nombre

    def get(self):
        pass

class Informacion:
    def __init__(self, producto):
        self.producto = producto

    def get_informacion(self):
        pass

from app import Administrador
from app import Coordinador
from app import Docente
##Prueba autenticacion coordinador
coordinador = Coordinador('Juan Perez', 'usuario', 'contraseña')
coordinador.autenticacion_coordinador()

# Prueba autenticacion docente
#docente = Docente('1', '2', '3')
#docente.autenticacion_docente()

# Prueba agregar docente programa
##coordinador = Coordinador("Juan", "juan123", "contraseña123")
##docente = Docente("docente1", "1234", "Pedro")
##coordinador.agregar_docente_programa(docente, "Ingeniería de Sistemas")
##print(coordinador.docentes_programas["Ingeniería de Sistemas"])

# Prueba crear lista Docentes
#admin = Administrador([], [], "admin", "1234")

#docente1 = Docente("docente1", "1234", "Pedro")
#docente2 = Docente("docente2", "1234", "Juan")
#docente3 = Docente("docente3", "1234", "María")

#admin.crear_lista_docentes(docente1)
#admin.crear_lista_docentes(docente2)
#admin.crear_lista_docentes(docente3)
#print("Lista de docentes:")
#for docente in admin.lista_docentes:
#    print(docente.nombre)

# Clasificar dorcente programa
#coordinador = Coordinador("Juan", "juan123", "contraseña123")
#docente = Docente("docente1", "1234", "Pedro")
#coordinador.agregar_docente_programa(docente, "Ingeniería de Sistemas")
#programa = "Ingeniería de Sistemas"
#docentes_programa = coordinador.clasificar_docente_programa(programa)
#for docente in docentes_programa:
#    print(docente.nombre)

# Clasificar docente grupo de investigacion
# Crear una instancia de Coordinador

#coordinador1 = Coordinador('Juan', 'usuario', 'contraseña')
#docente1 = Docente('usuario1', 'contraseña1', 'Pedro')
#docente2 = Docente('usuario2', 'contraseña2', 'Ana')
#docente1.nombre = 'Pedro Pérez'
#docente2.nombre = 'Ana González'
#coordinador1.agregar_docente_programa(docente1, 'programa1')
#coordinador1.agregar_docente_programa(docente2, 'programa2')
#coordinador1.crear_lista_docentes(docente1)
#coordinador1.crear_lista_docentes(docente2)
#coordinador1.clasificar_docente_gdi()
#print(docente1.nombre)

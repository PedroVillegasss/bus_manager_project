# Proyecto Bus Manager
El siguiente código fuente fue desarrollado para la asignatura de Paradigmas de Programación de quinto semestre.
## Autores
* Rodrigo Orellana
* Benjamín Valenzuela
* Pedro Villegas
# Enunciado
## Introducción
Durante las próximas tres semanas deberán desarrollar un proyecto grupal (3 integrantes) donde implementen los conceptos vistos en clase de POO. Este trabajo consiste en la creación de un software para organizar salidas a paseos en una escuela. 

Para esto, deben programar una solución que reciba información de múltiples archivos de texto con datos relevantes a los cursos que irán de paseo, los profesores y profesoras a cargo, los buses en los que se moverán, etc. 

Existe una lista limitada de acciones que se pueden realizar en este programa, las cuales se detallarán más adelante. A pesar de esto, es de extrema importancia que este software no falle, ya que cualquier error o equivocación puede significar dejar a algún estudiante atrás, contar con menos buses de los necesarios o incluso la cancelación del paseo en su totalidad. 

Este puede ser usado por profesores, alumnos y conductores de bus para organizar el transporte y asegurarse de que se cumplan los protocolos apropiados. 

En esta ocasión se les dará mayor libertad para que desarrollen la solución que mejor se adapte a los requerimientos del proyecto, siempre teniendo en cuenta que su programa debe emplear el paradigma de orientación a objetos, siguiendo los principios y buenas practicas aprendidas en las cátedras.

## Descripción del Proyecto
A continuación se explicarán los requerimientos que la entrega debe cumplir para que el software sea de utilidad para los usuarios finales de este. Una vez que terminen de leer este enunciado y todas las características y funcionalidades queden claras, su primer trabajo es modelar las clases a utilizar para reflejar las diferentes entidades que se presentan.

Siempre deben tener en cuenta la importancia de encapsular sus cualidades y responsabilidades, y tener claras las relaciones que puedan existir entre las diferentes clases durante la ejecución del programa.

### Requerimientos
Los usuarios de este programa son todos aquellos que deben subirse al bus el día del paseo, es decir, los alumnos, los profesores y el conductor. Pueden existir uno o más buses, y cada conductor sabe que bus es el que debe manejar. Cada bus tiene capacidad para llevar a un curso entero, por lo que cada curso tiene su bus asignado.

Los profesores tienen la responsabilidad de asegurarse de que todos los estudiantes estén presentes y en el bus correcto, por lo que un alumno no es capaz de subir al bus cuando quiera, sino que debe ser el profesor quien le indique que puede subirse. Si el bus al que se esta subiendo un alumno no es el que corresponde a su curso, el programa debe levantar una alerta.

Curiosamente, los conductores son muy territoriales, por lo que para evitar malos entendidos el programa debe levantar una alerta si un conductor intenta subir a un bus que no le corresponde. A modo de evitar dejar a alguien abajo, el profesor no puede subirse al bus hasta que todos los alumnos del curso hayan abordado. Si intenta hacerlo, el programa debe alertar y recordar esta condición al usuario. Además, por razones obvias, un bus vació no debe poder salir.

Todos los usuarios tienen un nombre, apellido y rut, siendo este ultimo inmutable, es decir, no se puede cambiar posterior a la creación del usuario. Además, los conductores tienen el bus que se les asignó entre sus atributos de instanciación.

### Ingesta de datos
El repositorio que deben clonar para empezar a trabajar viene precargado con archivos dentro de una carpeta data/, en la que se pueden encontrar múltiples archivos de texto en los que se almacena información que deben utilizar para poblar el programa al comenzar la ejecución. Estos solo pueden ser accedidos al comenzar la ejecución del programa con la finalidad mencionada, y, de ser necesario, pueden ser re-visitados únicamente por un profesor para pasar lista (piensen en estos archivos como el libro de clases del profesor).

El formato de estos archivos es:
* busses.txt: <licence_plate>
* classroom.txt: <name>,<teacher_rut>,<licence_plate>,[<student_rut>,...]
* drivers.txt: <first_name>,<last_name>,<rut>,<licence_plate>
* students.txt: <first_name>,<last_name>,<rut>
* teachers.txt: <first_name>,<last_name>,<rut>

El formato y distribución con la que se presentan estos archivos no corresponden a una imposición o sugerencia de clases que se deban crear. Sirven solo para entregar un punto de partida rico en datos para la ejecución del programa.

### Ejecución
En la carpeta raíz del repositorio debe haber un archivo input.txt, en el que cada linea corresponde a una acción a realizar. Posterior a la ingesta de datos, el programa debe leer este archivo y llevar a cabo cada una de estas acciones. Debe ser lo suficientemente riguroso de no interrumpir la ejecución de esta seguidilla de acciones, manejando con gracia acciones que contradigan las reglas introducidas en este enunciado.

Cada acción puede seguir alguno de los siguientes formatos:
* <rut> GETS IN THE BUS <licence_plate>
* <rut> LETS <rut> IN THE BUS <licence_plate>
* <licence_plate> DRIVES OFF

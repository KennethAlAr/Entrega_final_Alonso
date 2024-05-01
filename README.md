# Entrega Final
### Alumno: Kenneth Alonso Arce

# Roll for Initiative
### La web "Roll for Initiative" es una web para crear sistemas y salas de juego para juegos de rol de mesa:

## Instrucciones

1. Abrir el enlace [Roll for Initiative](http://localhost:8000).

2. Si no estamos logueados, en la parte superior aparecen los siguientes botones:
    - En la parte izquierda el botón de "Roll for Inititative" que sirve como botón "home" y nos lleva a la página principal.
    - En la parte derecha el botón de "login" para loguearse con una cuenta existente.
    - El botón "Crear Usuario" para crearse una cuenta nueva.
    - En la parte inferior derecha el botón "Acerca de mí" con un poco de información sobre mí.

3. Si estamos logueados, veremos en la parte superior los siguientes botones:
    - En la parte izquierda el botón de "Roll for Inititative" que sirve como botón "home" y nos lleva a la página principal.
    - El dropdown "Sistema" con las opciones para ver todos los sistemas de juego, crear un sistema de juego nuevo o buscar un sistema de juego.
    - El dropdown "Juegos" con las opciones para ver todos los juegos creados, crear un juego nuevo o buscar un juego específico.
    - El dropdown "Reservas" para ver todas las reservas que tiene el usuario logueado o para crear una nueva reserva.
    - En la parte derecha el botón "logout" para desconectar la cuenta logueada.
    - El nombre del usuario que sirve como botón para editar los datos del usuario.
    - El avatar del usuario o, en caso de que no tenga avatar, el botón "Añadir Avatar".
    - En la parte inferior derecha el botón "Acerca de mí" con un poco de información sobre mí.


## Sistemas:
### Todos los sistemas:
1. Hace una visualización de todos los sistemas de juego que se han creado con sus detalles.
2. Se puede hacer CRUD en todos ellos.
    - El botón "Ver" nos enseña el detalle del sistema elegido, además tenemos un botón de "Volver" para volver a la página anterior.
    - El botón "Editar" nos deja editar los detalles del sistema, en esta url aparece el mismo formulario que se utiliza para crear un sistema pero con los datos originales del sistema que se está editando.
    - El botón "Eliminar" nos deja eliminar el sistema, en este caso nos lleva a una nueva url de confirmación de eliminación.
3. En esta url tenemos además un botón de "Buscar Sistema" y otro de "Crear Sistema".
### Crear Sistema:
1. Se puede crear un sistema eligiendo un nombre, un tipo de dado, una base de juego y una descripción.
### Buscar sistema:
1. Se puede hacer una búsqueda con diversos filtros:
    - Por nombre o parte de nombre.
    - Por tipo de dado.
    - Por base del sistema.
2. Cuando hacemos la búsqueda nos lleva a una nueva url que es igual a la que se utiliza en "Todos los Sistemas" con la distinción que esta lista añade un botón de "Todos los Sistemas" para volver a la lista general donde aparecen todos los sistemas.

## Juegos:
### Todos los juegos:
1. Hace una visualización de todos los juegos creados con sus respectivos detalles.
2. Se puede hacer CRUD en todos ellos.
    - El botón "Ver" nos enseña el detalle del juego elegido asi como todos los jugadores que se han unido junto a sus detalles y su imagen de avatar, además tenemos un botón de "Volver" para volver a la página anterior. En la lista de jugadores tenemos el botón "Ver" para poder ver los detalles de los jugadores que han reservado espacio en la partida, también con su botón de "Volver". Adicionalmente, si el juego no está disponible el mensaje "No disponible" aparece en rojo.
    - El botón "Editar" nos deja editar los detalles del juego, en esta url aparece el mismo formulario que se utiliza para crear un juego pero con los datos originales del juego que se está editando.
    - El botón "Eliminar" nos deja eliminar el juego, en este caso nos lleva a una nueva url de confirmación de eliminación.
### Crear Juego:
1. Se puede crear un juego eligiendo un nombre, su disponibilidad, el número de jugadores, el sistema de juego, la descripción y la fecha y hora de inicio asi como la hora de final.
### Buscar juego:
1. Se puede hacer una búsqueda con diversos filtros:
    - Por nombre o parte de nombre.
    - Mostrando solo los juegos disponibles.
    - Por un número de jugadores mínimos.
    - Por sistema de juego.
    - Por fecha de partida.
2. Cuando hacemos la búsqueda nos lleva a una nueva url que es igual a la que se utiliza en "Todos los Juegos" con la distinción que esta lista añade un botón de "Todos los Juegos" para volver a la lista general donde aparecen todos los juegos.

## Reservas:
### Todas tus reservas:
1. Muestra una lista de todas las reservas que ha hecho el usuario conectado.
2. Se puede hacer CRUD en todas ellas.
    - El botón "Ver" nos enseña el detalle de la reserva, además tenemos un botón de "Volver" para volver a la página anterior.
    - El botón "Editar" nos deja editar los detalles de la reserva, en esta url aparece el mismo formulario que se utiliza para crear una reserva pero con los datos originales de la reserva que se está editando.
    - El botón "Eliminar" nos deja eliminar la reserva, en este caso nos lleva a una nueva url de confirmación de eliminación.
3. En cada reserva aparece un botón adicional de "Juego" para ver los detalles del juego en el que se ha hecho la reserva. Este botón nos lleva a la url de detalle de juego, igual que el botón "Ver" de la lista de todos los juegos.
### Crear reserva:
1. Se puede crear una reserva eligiendo el juego, la raza, la clase, si tenemos experiencia o no y la descripción. En este caso el jugador de la reserva es por defecto el usuario logueado.

## Lógica de usuarios:
### Crear usuario:
1. Nos deja crear un usuario nuevo eligiendo nombre y contraseña.
### Login:
1. Nos deja conectarnos con una cuenta existente si tenemos su "username" y su "password".
### Editar usuario:
1. Si estamos logueados, en la barra superior, a la derecha, aparece el nombre del usuario que a la vez hace de botón para poder editar los datos del usuario.
2. Se puede editar el nombre de usuario, su primer y segundo apellido y su correo electrónico.
### Añadir Avatar / Editar Avatar:
1. Si estamos logueados, en la barra superior, a la derecha del nombre de usuario aparece el botón "Añadir Avatar".
2. Se puede seleccionar un archivo que sirva como avatar para el usuario.
3. En caso de ya tener un avatar, en vez del botón "Añadir Avatar" aparecerá el avatar del usuario al lado derecho de su nombre.
4. El avatar hace las veces de botón para editar el avatar. En este caso nos envía al mismo formulario que el botón de "Añadir Avatar", con la distinción que, en este caso, antes de añadir el nuevo avatar, borra el anterior.

## Lógica de administración:
1. Podemos administrar la página de Roll for Initiative en la página del [Administrador](http://localhost:8000/admin/).
2.  - User: admin 
    - Password: admin1234
3. El administración tiene poderes para hacer CRUD en los usuarios, los avatares, los juegos, las reservas y los sistemas.
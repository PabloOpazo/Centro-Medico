## Proyecto Centro-Medico

## Configuracion de ambiente de trabajo:

## Repositorio https://github.com/PabloOpazo/Centro-Medico.git

Crea una máquina virtual e instala las bibliotecas disponibles en el archivo requirementes.txt:
Ingresa a la carpeta creada y activa un entorno virtual:
```
$ cd centro-medico
$ python -m venv venv
```
Luego debes activarlo con el siguiente comando:

```
$ source ./venv/bin/activate
```
Después de activarlo, instala las bibliotecas necesarias para ejecutar el proyecto:
```
 (venv)$ pip install -r requirements.txt
```
Para tener el primer acceso y configurar la aplicación, ejecuta el comando 'migrate' para generar la base de datos predeterminada de Django (SQLite). Luego, crea el superusuario:
```
(venv)$ ./manage.py migrate
(venv)$ ./manage.py createsuperuser
Apellido/Usuario: admin
E-mail: admin@mail.com
Password: 
Password (again):
```


Para iniciar el servidor debes ingresar:
```
(venv)$ ./manage.py runserver
```


Para verificar si todo está funcionando como se espera, accede a la siguiente dirección:
[http://localhost:8000/](http://localhost:8000/)

Vista administrador
[http://localhost:8000/admin](http://localhost:8000/admin)


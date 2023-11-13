## Repositorio https://github.com/PabloOpazo/Centro-Medico.git
 pip install -r requirements.txt
```
Para tener el primer acceso y configurar la aplicación, ejecuta el comando 'migrate' para generar la base de datos predeterminada de Django (SQLite). Luego, crea el superusuario:
```
python manage.py migrate
python manage.py createsuperuser
Apellido/Usuario: admin
E-mail: admin@mail.com
Password: 
Password (again):
```


Para iniciar el servidor debes ingresar:
```
python manage.py runserver
```


Para verificar si todo está funcionando como se espera, accede a la siguiente dirección:
[http://localhost:8000/](http://localhost:8000/)

Vista administrador
[http://localhost:8000/admin](http://localhost:8000/admin)


Viendo como funciona Flask
-
Crear un ambiente nuevo y activarlo:

	virtualenv taller
	source taller/bin/activate


Installar Flask
	
	pip install Flask

Correr ejemplo
	
	python ejemplo1/hello.py

Entrar a ver la aplicación en [http://localhost:5000](http://localhost:5000)

Para el segundo ejemplo correrlo con

	python ejemplo2/hello2.py

y entrar a [http://localhost:5000](http://localhost:5000) para verla.


Ejemplo de aplicación web en Flask
-
Activar el ambiente si no lo está

	source taller/bin/activate

Correr la primera parte de la aplicación

	python ejemplo2/main.py

Correr las siguientes partes de la misma manera y ver sus diferencias

	python ejemplo2/main2.py
	python ejemplo2/main3.py
	python ejemplo2/main4.py


Aplicación de ejemplo en Heroku
-
Tener activado el ambiente, recuerden que si no lo está lo activan con 

	source taller/bin/activate

Ir a la carpeta de la aplicación

	cd helloHeroku

Iniciar repositorio git y hacer commit:

	git init
	git add .
	git commit -m 'first commit'

Loguearse y crear la aplicación en Heroku:

	heroku login
	heroku create

Hacer push a Heroku:

	git push heroku master

Listo :D 
Ya está arriba la aplicación.

Aplicación en Heroku con base de datos
-

Desactivar ambiente de taller
	
	deactivate

Ir a la carpeta, crear un nuevo ambiente y activarlo

	cd microblog
	virtualenv microblogEnv
	source microblogEnv/bin/activate

Instalar las librerías necesarias con pip desde el archivo de requerimientos

	pip install -r requirements.txt

Al igual que la aplicación anterior, iniciamos un repositorio git, añadimos las cosas y hacemos commit.

	git init
	git add .
	git commit -m 'first commit'

Luego, creamos la aplicación en heroku

	heroku create

Ya que la aplicación necesita una base de datos creamos una Postgresql en heroku

	heroku addons:add heroku-postgresql:dev

Ver información de la base de datos llamada DATABASE:
	
	heroku pg:credentials DATABASE

Modificamos la variable DATABASE en el archivo microblog/\_\_init\_\_.py

Debemos inicializar la base de datos, eso lo hacemos abriendo la terminal de python y ejecutando los siguientes comandos

	python
	\>\>\> from microblog.database import init_db
	\>\>\> init_db()


Subimos todo a heroku con 

	git push heroku master


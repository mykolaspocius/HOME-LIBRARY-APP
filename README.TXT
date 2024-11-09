            Este archivo descirbe el estado de la aplicacion en el checkpoint 

%%%%%%%%%%%%%%%%%%%%%%% ENTORNO DESARROLLO %%%%%%%%%%%%%%%%%%%%%%%%%%
- Para asegurarse que se puede activar entorno virtual en windows en la consola en modo administrador ejecutar lo siguiente:
    Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope LocalMachine
- Crear entorno virtual:
    python -m venv .venv  
- Para activar entorno virtual con nombre .venv en windows:
    .venv\Scripts\activate  
- Para ir actualizando requirements.txt segun se van instalando dependencias en el entorno
    pip freeze > requirements.txt
%%%%%%%%%%%%%%%%%%%%%%% Setup entorno FLASK  %%%%%%%%%%%%%%%%%%%%%%%%
- Para definir la variables de entorno de inicio para FLASK, crear archivo .flaskenv. Alli se definen FLASK_APP y FLASK_DEBUG.
- Para poder usar estos archivos de variables de entorno hay que instalar el paquete python-dotenv
    pip install python-dotenv
- Para facilitar imports dentro de app definir archivo __init__.py dentro de app. Esto convierte a app en un python package, lo que va a permitir importar cosas
    usando notacion import app.lo_que_sea. 
- Para algunas variables necesarias para configurar extensiones usar objeto Config dentro de config.py.

%%%%%%%%%%%%%%%%%%%%%%% Aplicacion %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
- Se definen dos rutas en el BluePrint main para la pagina principal y el login de los usuarios
- Se define otro BluePrint para Books con una ruta /Books/
- Se añade la inicialización de los BluePrints en __init__.py de app
- Se crean templates para visualizar las paginas definidas en las rutas creadas
- Se añade la extención Flask-wtf para crear formularios
- Se añade la ruta de registro usuarios a main
- Se crean los formularios para Login y Registro
- Creados los modelos para manejar usuarios y permisos
- Creada la base de datos usando migrate y sqlalchemy
- Registrar algunos app.cli comandos para poblar la base de datos con valores de permisos, roles y usuario admin
- Añadir .env para guardar las credenciales de admin
- Creado el código en rutas de main para login y registro de usuarios en la base de datos
- Añadida extension Flask-Login
- Configurado el login y logout de los usuarios usando la anterior extensión
- Añadida la protección sobre ruta /books para que solo se pueda ver si el usuario está identificado. Se ha usado redirect en /login



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
- Usar una ruta basica '/' definida directamente en __init__.py para probar si funciona el servidor



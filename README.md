Twitter-Home-Control
===

Código Python para que desde Twitter controlemos las acciones de nuestro
computador en el hogar.

En esta implementación utilizamos un Arduino y la  librería PyFirmata
(https://github.com/tino/pyFirmata) por lo que es requerido que el arduino
tenga cargado el firmware Firmata (en IDE de Arduino utilizar
Files/Examples/Firmata/StandardFirmata).
Esta librería no esta disponible en los repositorios de Debian y tampoco la
puedo instalar via PIP por lo cual tuve que bajarla directo desde el sitio y
dejarla como subdirectorio (no la incluyo aquí)

Para Twitter, utilizamos la librería Twython (tweepy tiene problemas en mi Debian/Testing).

La implementación requiere que el usuario cree una cuenta Twitter y luego la App
obteniendo las credenciales. Éstas deben ser puesta en un archivo llamado "Keys" en
el mismo directorio que la aplicación, con el siguiente formato:

* CONSUMER_KEY=xxxx
* CONSUMER_SECRET=xxxx
* ACCESS_TOKEN_KEY=xxxx
* ACCESS_TOKEN_SECRET=xxx

Para efectos de las pruebas se puso un LED en el Pin 13 y se aceptan los
comandos:

* Encender led de prueba
* Apagar led de prueba
* Animar led de prueba

También se utiliza el módulo eSpeak para indicar de manera verbal los comandos recibidos

##Historia
* 2015-05-31 Primera implementación funcional. Manipula un led a través de mensajes
directos desde Twitter

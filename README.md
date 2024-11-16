Network Device Scanner with Nmap
Descripción
Este proyecto utiliza Nmap para escanear la red local y detectar los dispositivos conectados. La herramienta genera un log detallado de los dispositivos nuevos que se unen a la red y actualiza un archivo JSON con la información de todos los dispositivos detectados. El objetivo es tener un registro constante y actualizado de los dispositivos en la red, lo cual puede ser útil para monitoreo, auditoría o gestión de redes.

Funcionalidades
Escaneo de dispositivos en la red local: Utiliza Nmap para identificar todos los dispositivos activos en la red, obteniendo sus direcciones IP y otros detalles relevantes.
Generación de logs: Crea un archivo de log donde se registra información sobre los dispositivos nuevos que se unen a la red, permitiendo un seguimiento histórico.
Actualización de JSON: Actualiza un archivo JSON con los dispositivos detectados, manteniendo un registro persistente y accesible de todos los dispositivos que han sido identificados en la red.
Detección en tiempo real: El escaneo de la red se puede realizar en intervalos regulares, asegurando que el registro se mantenga actualizado.
Tecnologías y Herramientas
Python 3.x: Lenguaje de programación utilizado para automatizar el escaneo y el manejo de archivos.
Nmap: Herramienta de código abierto para escanear redes y dispositivos.
JSON: Formato de almacenamiento para mantener un registro de los dispositivos.
Logs: Generación de logs en archivos de texto para un seguimiento histórico.
Requisitos
Python 3.x: Asegúrate de tener Python 3 instalado.
Nmap: Instala Nmap en tu sistema para que el script funcione correctamente.
Dependencias: Instalar las librerías necesarias (si aplica).
bash
Copiar código
pip install nmap
Uso
Configura el archivo JSON y el log: Define el archivo JSON donde se almacenarán los dispositivos detectados.
Ejecuta el escaneo: El script escaneará la red local en intervalos regulares y actualizará los registros.
Revisa los logs y el JSON: El archivo de log contendrá detalles de nuevos dispositivos detectados y el archivo JSON tendrá un registro completo de todos los dispositivos en la red.
Contribuciones
¡Las contribuciones son bienvenidas! Si tienes sugerencias, mejoras o reportes de errores, por favor abre un issue o crea un pull request.

Notas:
Si deseas personalizar el rango de IP o el intervalo de escaneo, puedes modificar la configuración en el archivo de parámetros del proyecto.
Ten en cuenta que la herramienta debe ejecutarse con privilegios suficientes para utilizar Nmap en la red local.

# Instrucciones para la entrega de Talleres y Laboratorios
Este material está desarrollado para que los estudiantes puedan subir de forma correcta sus ejercicios de clase y recibir retroalimentación. Para revisar este material de forma efectiva, es necesario haber visto el vídeo introductorio a GitHub subido a Bloque Neón.
## ÍNDICE

1. Instrucciones para hacer visible su repositorio
2. Instrucciones para subir archivos correctamente
3. Actualizar su repositorio para recibir retroalimentación

# 1. Instrucciones para hacer visible su repositorio:
Cree un repositorio en Github con el nombre "MIIA_estudiante_X". La "X" la reemplazará con su número asignado en el siguiente link: [Excel](https://docs.google.com/spreadsheets/d/1QRWAh6s2AYoAv1bwY1lfE0UxGwtN0PQT/edit?usp=sharing&ouid=106193266347732142982&rtpof=true&sd=true).
En este link deberá escribir en la respectiva columna su usuario en GitHub para poder acceder a su trabajo.
### Recuerde:
- Su repositorio debe de ser público.
- Su repositorio debe de contener solo información del curso.
- Añada semanalmente sus talleres y laboratorios con su solución al repo.

Se creará un algoritmo que descargue sus archivos automáticamente. Si su repositorio no está bien creado (i.e. no es visible), el algoritmo no accederá a él y por ende no podrá recibir retroalimentación ni nota para sus cursos.

# 2. Instrucciones para subir archivos correctamente:
Los talleres y laboratorios del curso se recopilarán con un algoritmo que lea sus envíos y publicaciones durante cada fecha de entrega. Es por esto que usted debe de ser cuidadoso con los nombres que le ponga a cada acrividad.
Para cada actividad usaremos un nombre especifico que permita identificar su trabajo.
### Pasos:
- Cree dos carpetas en su repo. Una con el nombre "Talleres" y otra con el nombre "Laboratorios".
- Cada taller o laboratorio debe de ser nombrado de esta manera: "Taller_Y_X" y "Lab_Y_X". Donde la "Y" es el número del taller y la "X" es el número asignado previamente por el curso.
- Estos talleres deben de estar guardados en su carpeta respectiva de forma organizada
- Actualice su repositorio en la nube para que sea evaluado.

Para este último punto, recuerde esta secuencia de comandos en una consola de git lanzada en su repositorio:
```sh
git add .
git commit -m "Entrega"
git push
```
> Una consola de git viene en una instalación local del programa Git para el manejo de repositorios. Entender estos comandos le facilitará el trabajo durante el curso y el resto de su vida como programador.

# 3. Actualizar su repositorio para recibir retroalimentación:
Una vez las calificaciones de los laboratorios se realice, usted podrá acceder a la retroalimentación de su trabajo actualizando su repo de forma local. El siguiente comando sirve para actualizar su versión local:
```sh
git pull
```
Para que pueda subir su retroalimentación, deberá aceptar la integración (pull-request) que le estaré enviando con su archivo comentado. 

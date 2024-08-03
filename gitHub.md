# Primeros pasos en Git

## ¿Que es GIT?
Es un sistema de control de versiones CVS, utilizado para guardar el historial de cambios del codigo fuente .

## ¿Qué es un Repositorio?
Es un proyecto que contiene multiples archivos. Existen dos tipos de repos.:
1. **Repositorios remotos**: se alojan en Linea (la nube), los principales servicios de alojamiento en Git son GitHub (propiedad de Microsoft), Gitlab (prop. de GitLab), y BitBucket.
2. **Repositorios locales**: se alojan Fuera de linea (auto-instalado en tu servidor).

## Los tres Estados de Git
Un archivo puede tener los siguientes estados:
* **modified** (modificado): significa que se modificó el archivo pero no se ha confirmado en nuestra base de datos local.
* **staged** (preparado): significa que has marcado un archivo modificado en su versión actual para que vaya en tu próxima confirmación.
* **committed** (confirmado): significa que los datos se encuentran asegurados en nuestra base de datos local.

Esto nos lleva a conocer las tres secciones principales de un proyecto de Git:

**Git directory** (directorio de Git): donde se almacenan los metadatos - *Información sobre el repositorio, como configuraciones, ramas, etiquetas, etc*- y la base datos de objetos para tu proyecto -- *Todos los objetos de datos, como commits, árboles y blobs (archivos de contenido), están almacenados aquí. Estos objetos son la esencia del historial de tu proyecto* --


**working directory** (directorio de trabajo): es una copia de una versión del proyecto. Estos archivos se sacan de la base de datos comprimida en el directorio de Git, y se colocan en disco para que los puedas usar o modificar. Esta es la parte visible del repositorio, donde realizas tus tareas diarias de desarrollo, como editar código, agregar nuevos archivos, o eliminar archivos existentes.

**staging area** (área de preparación) : generalmente contenido en tu directorio de Git, que almacena información acerca de lo que va a ir en tu próxima confirmación.

<!-- ![Flujo de trabajo de git](/images/areas.png) -->

<img src="/images/areas.png" alt="500" width="500"/>

### Flujo de trabajo basico en GIT

El flujo de trabajo básico en Git es algo así:

1. Modificas una serie de archivos en tu directorio de trabajo.
2. Preparas los archivos, añadiéndolos a tu área de preparación.
3. Confirmas los cambios, lo que toma los archivos tal y como están en el área de preparación y almacena esa copia instantánea de manera permanente en tu directorio de Git.

## Instalación de Git

**Windows**:

Descargamos git en https://git-scm.com/downloads
. Utilizaremos la terminal Git Bash (se descarga cuando instalamos git)

Abrimos Git Bash:
* **Verificamos instalación**: escribimos en la terminal <font color="red">**`git --version`**</font>
* **Configuramos git**: escribimos lo siguiente en la terminal
```Bash
git config --global user.name nombreDeUsuarioejemplo
git config --global user.email tuemail@gmail.com
```
( La opcion --global es para que la config se efectue de manera global y no por proyecto. y en user.name configuramos git con nuestro nombre el que queramos )

* **Configurar editor de texto**: con esto señalamos que VSCode es nuestro editor de texto por defecto. Wait sirve para q espere a que cerremos el editor. 
```Bash
git config --global core.editor "code --wait"
``` 

* **Configuración finales de linea en archivos de texto**: Los finales de línea pueden variar entre sistemas operativos: Windows utiliza "CRLF" (carriage return + line feed) mientras que Linux y macOS utilizan "LF" (line feed).
La configuración core.autocrlf en Git ayuda a manejar estas diferencias al clonar repositorios y hacer commits, para evitar problemas de compatibilidad y asegurarse de que los archivos se vean correctos en diferentes sistemas operativos. 

``` bash
git config --global core.autocrlf true           #Para Windows
git config --global core.autocrlf input          #Para Linux/Mac
```      

Si quisieramos ver nuestro archivo de config global escribimos: `git config --global -e`     //esto nos llevara a VSCode y nos mostrara la config.

DATO: `git config -h` (muestras opciones para la config)

## Comandos básicos en la terminal

1) **`ls`** : muestra todas las carpetas/directorios que tenemos
2) **`pwd`** : nos dice en que carpeta/directorio nos encontramos
3) **`cd nombreDeDirectorio`** : nos mueve a la carpeta seleccionada. Tambien podemos abrir una carpeta dentro de otra **`cd Desktop/carpeta1`**
4) **`cd ..`** : salir de la carpeta
5) **`mkdir nombreDirectorio`** : esta funcion crea una carpeta con el nombre que deseamos.
6) **`touch archivoNuevo`** : Nos permite crear un archivo nuevo con el nombre que deseemos.
7) **`code .`** : esto abre mi editor de texto (q por defecto es VSCode) dentro de la carpeta/directorio donde estoy
8) **`cat nameArchivo`** : me muestra el contenido de un archivo.


## Flujo de trabajo con Git

Comandos basicos de GIT.

**`git init`** : INICIALIZA un repositorio dentro de la carpeta. Por ejemplo escribo: git init (luego presiono enter y me va a aparecer -> Initialized empty Git repository in C:/Users/Usuario/Desktop/Carpeta1/.git/   <-- .git me indica que este directorio esta oculto, no se mostrara lo que hay en .git si escribo ls. Pero si lo hara con "ls -a" >)

**`git add nombreDeArchivo`** : cuando ejecutamos este comando, lo que haremos sera seleccionar los archivos que queramos pasar a la etapa Stage. En esta Etapa basicamente se considera los cambios/actualizaciones del archivo que queramos subir al repositorio (pero no se suben al repositorio).

**`git commit -m "mensaje entre comillas"`** : sube el archivo en la etapa commit (es la etapa despues de stage, es decir confirma que quiero guardar este cambio para luego pasarlo al repo).

**`git status`** : nos muestra el estado actual de nuestro repositorio (como los archivos que no se subieron o a subir)

**`git push`**  : sube lo commiteado al repositorio remoto.


NOTA: para subir mas de un archivo escribimos por ejemplo: `git add archivo1 archivo2`
En caso de modificar un archivo como archivo2 (es decir hicimos cambios del codigo desde VScode), tendremos que actualizar estos cambios a mi etapa stage => vuelvo a escribir: `git add archivo2`


### Eliminar en git

**Eliminar un Archivo** : Para eliminar un archivo podriamos utilizar el sig. comando:

```bash
rm archivo2             #eliminar archivo
git status              #verifico su estado y me aparece "deleted:  archivo2"
git add archivo2        #lo paso a la etapa Stage
git commit -m "eliminar archivo 2" #esto elimina el archivo2 de todas las etapas (stage y commit)
```
Luego **`git push`** para subir los cambios al repositorio remoto.

**otra forma** mas corta es: 
```bash
git rm archivo2
git commit -m "eliminar archivo 2"
```

Si quiero restaurar un archivo a eliminar que pase a la etapa Stage (justo antes de comitear) utilizo:
 
``` bash
git restored --stage archivo2
```

En caso de que quiera descartar los cambios y que lo devuelva a mi lista ls escribo:  `git restore archivo2`


**Eliminar una carpeta**
```bash
git rm -r miCarpeta
git commit -m "elimino miCarpeta"
```
Luego **`git push`** para subir los cambios al repositorio remoto.


## CONECTANDO CON GITHUB:

1. Creamos una cuenta en GITHUB
2. Luego creamos un repositorio dentro de github.


En Github tenemos dos formas de subir nuestro repositorio local al remoto, es decir dos formas de hacer push. Para ello es necesario que tengamos commiteado los archivos que queramos subir al repositorio remoto.

### Formas de hacer PUSH 

#### Mediante una clave Token

1. Primero debemos crearnos una clave Token. Para ello entramos a nuestro GitHub y:
    - Desde el icono de nuestra cuenta seleccionamos la opcion settings.
    - Luego bajamos y presionamos "<> Developer settings" 
    - pincho en "Personal access tokens" 
    - luego en "Personal access tokens (classic)" -> "Generate new Token" -> "Generate new Token (classic)" 
    - en "note" escribimos el nombre que quiera ponerle a mi token y en "Select scopes" selecciono la opcion "repo" 
    - Por ultimo bajo y pincho en "Generate Token" y Listo utilizaremos esta clave más adelante.

NOTA: este token dura 30dias o mas depende de la opcion que elijamos a la hora de crearla

2. Agregamos un nuevo repositorio remoto con el siguiente comando:

```Bash
git remote add origin https://github.com/ejemplo  #este link lo encontramos en  [<> Code]
```
Aqui se define una nueva conexión a un repositorio remoto y la etiqueta con el nombre "origin" (origin es de ejemplo).
Se usa cuando no hay un remoto llamado "origin" configurado previamente.

3. Siguiente a eso, si es la primera vez que haces push escribimos:

```bash
git push -u origin main      #main es la rama por defecto creada en nuestro repo. remoto
```
Donde -u (o --set-upstream) establece una relación de seguimiento entre la rama local main y la rama remota main. Si ya has utilizado este comando con hacer `git push` es suficiente.


Presiono Enter, y nos aparece:
```bash
Username for 'https://github.com': NombreDeUsuarioDeGit    #luego ENTER
Password for 'https://ejemplo@gmail.com': contraseñaToken  #copiamos el Token que genreamos en el paso 1) 
```

Luego Enter y Listo! , el codigo se subio al repo. remoto.

#### Mediante Claves SSH

Ideal para trabajar en computadoras fijas (aquellas a las que más frecuentas). Describire los pasos que podemos seguir en Linux, para mas información sobre generar una nuvea clave ssh en Mac o Windows lo podemos encontrar [aqui](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

1. Crear una clave ssh localmente, abrimos una terminal y escribimos lo siguiente reemplazando el correo por tu correo de github:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
2.  


## RAMAS EN GIT o BRANCHES
Comandos basicos sobre ramas de git.

**`git branch`** : me dice en que rama me encuentro, y cuales hay.

**`git checkout -b nuevaRama`** : crea una nueva rama

**`git checkout nombreDeRama`** : Cambia a la rama que yo quiero utilizar.

**`git log --oneline`** : me da el historial de los cambios en mi rama

**`git merge nombreOtraRama`** :sirve para pasar los cambios de otra rama a mi rama principal (debo situarme ahi)

**`git branch -d nombreRamaAEliminar`** : elimina de forma local una rama (para ello debemos situarnos en otra rama)

**`git push origin --delete nombreRamaAEliminar`** : sube los cambios al repo.remoto     


## Funciones utiles entre repos locales y remotos

**`git remote -v`** : indica las conexiones remotas que tiene nuestro proyecto local.

**`git remote set-url origin urlDemiRepoRemota`** : Para cambiar la URL de tu repositorio remoto en Git tan solo escribimos el siguiente código agregando la nueva dirección. Esto se lo utiliza cuando la url de nuestro repo remoto cambia o queremos cambiar su destinario.


NOTA: git pull --rebase urlDemiRepoRemoto
En lugar de utilizar git merge para integrar la rama remota en la local, usa git rebase. Me ayudo a actualizar los cambios de mi rama remota a la local y viceversa.

`rm -rf .git` : eliminar un repositorio de Git creado con ‘git init’ en un directorio (elimina un repo local)

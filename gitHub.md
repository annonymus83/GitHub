# Primeros pasos en Git

## ¿Que es GIT?
Es un sistema de control de versiones CVS, utilizado para guardar el historial de cambios del codigo fuente .

## ¿Qué es un Repositorio?
Es un proyecto que contiene multiples archivos. Existen dos tipos d repos.:
1. **Repositorios remotos**: el repo. se aloja en Linea (la nube), los principales servicios de alojamiento en GiT son GitHub (propiedad de Microsoft), Gitlab (prop. de GitLab), y BitBucket.
2. **Repositorios locales**: el repo. se aloja Fuera de linea (auto-instalado en tu servidor).

## Los tres Estados de Git
Un archivo puede tener los siguientes estados:
* **modified** (modificado): significa que se modificó el archivo pero no se ha confirmado en nuestra base de datos local.
* **staged** (preparado): significa que has marcado un archivo modificado en su versión actual para que vaya en tu próxima confirmación.
* **committed** (confirmado): significa que los datos se encuentran asegurados en nuestra base de datos local.

Esto nos lleva a conocer las tres secciones principales de un proyecto de Git: 
El directorio de Git (**Git directory**), el directorio de trabajo (**working directory**), y el área de preparación (**staging area**).

![Flujo de trabajo de git](/images/areas.png)

<img src="/images/areas.png" alt="200" width="200"/>

## Instalación de Git

**Windows**:

Descargamos git en https://git-scm.com/downloads
. Utilizaremos la terminal Git Bash (se descarga cuando instalamos git)

Abrimos Git Bash:
* **Verificamos instalación**: escribimos en la terminal `git --version` 
* **Configuramos git**: escribimos lo siguiente en la terminal
```Bash
git config --global user.name nombreDeUsuarioejemplo
git config --global user.email tuemail@gmail.com
```
( La opcion --global es para que la config se efectue de manera global y no por proyecto. y en user.name configuramos git con nuestro nombre el que queramos )

* **Configuar editor de texto**: con esto señalamos que VSCode es nuestro editor de texto por defecto. Wait sirve para q espere a que cerremos el editor. 
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

1) `ls` : muestra todas las carpetas/directorios que tenemos
2) `pwd` : nos dice en q carpeta/directorio nos encontramos
3) `cd nombreDeDirectorio` : nos mueve a la carpeta seleccionada. Tambien podemos abrir una carpeta dentro de otra `cd Desktop/carpeta1`
4) `cd ..` : salir de la carpeta
5) `mkdir nombreDirectorio` : esta funcion crea una carpeta con el nombre que deseamos.
6) `touch archivoNuevo` : Nos permite crear un archivo nuevo con el nombre que deseemos.
7) `code .` : esto abre mi editor de texto (q por defecto es VSCode) dentro de la carpeta/directorio donde estoy


## Flujo de trabajo con Git

`git init` : INICIALIZA un repositorio dentro de la carpeta. Por ejemplo escribo: git init (luego presiono enter y me va a aparecer -> Initialized empty Git repository in C:/Users/Usuario/Desktop/Carpeta1/.git/   <-- .git me indica que este directorio esta oculto, no se mostrara lo que hay en .git si escribo ls. Pero si lo hara con "ls -a" >)

`git add nombreDeArchivo` : cuando ejecutamos este comando, lo que haremos sera seleccionar los archivos que queramos pasar a la etapa Stage. En esta Etapa basicamente se considera los cambios/actualizaciones del archivo que queramos subir al repositorio (pero no se suben al repositorio).

`git commit -m "mensaje entre comillas"` : sube el archivo en la etapa commit (es la etapa despues de stage, es decir confirma que quiero guardar este cambio para luego pasarlo al repo).


`git status` : nos muestra el estado actual de nuestro repositorio (como los archivos que no se subieron o a subir)

NOTA: para subir mas de un archivo escribimos por ejemplo: *git add archivo1 archivo2*    //respetando los espacios
En caso de modificar un archivo como archivo2 (es decir hicimos cambios del codigo desde VScode), tendremos que **actualizar** estos cambios a mi etapa stage => vuelvo a escribir: *git add archivo2*


`rm nombreDeArchivo` : rm es un comando que sirve para eliminar un archivo
ejemplo: rm archivo2

```bash
git status  #verifico su estado y me aparece "deleted:  archivo2"
git add archivo2  #lo paso a la etapa Stage
git commit -m "eliminar archivo 2" #esto elimina el archivo2 de todas las etapas (stage y commit)

```

**otra forma** mas corta es: 
```bash
git rm archivo2
git commit -m "eliminar archivo 2"
```

Si quiero restaurar un archivo a eliminar que pase a la etapa Stage (justo antes de comitear) utilizo:
 
`git restored --stage nombreArchivo`

ejemplo: git restored --staged archivo2
En caso de que quiera descartar los cambios y que lo devuelva a mi lista ls escribo:
      git restore archivo2

7. `git push`  : sube lo commiteado al repositorio remoto.


## ***CONECTANDO CON GITHUB***:
1. Creamos una cuenta 
2. Luego creamos un repositorio

ABRIMOS **Git Bash** :
3. Y escribimos lo siguiente (esto lo hacemos despues de haber "commiteado los archivos")

`git remote add origin https://github.com/ejemplo`    

//esta url lo encontramos en la opcion <>Code (que se haya dentro del repositorio que cree). 

4. Siguiente a eso:

`git push -u origin main`

//main es una rama que por defecto se crea en nuestro repo.
Presiono Enter, y nos aparece:

Username for 'https://github.com': NombreDeUsuarioDeGit  //luego ENTER

Password for 'https://ejemplo@gmail.com': contraseñaToken  //esta contraseñaToken lo conseguimos desde nuestra cuenta GITHUB 1)Desde el icono de nuestra cuenta seleccionamos la opcion settings .2)Luego bajamos y presionamos "<> Developer settings" 3) pincho en "Personal access tokens" 4) luego en "Personal access tokens (classic)" -> "Generate new Token" -> "Generate new Token (classic)" 5) en "note" escribimos el nombre que quiera ponerle a mi token y en "Select scopes" selecciono la opcion "repo" 6) Por ultimo bajo y pincho en <Generate Token> 
7) copio el token y lo reemplazo en "constraseñaToken" (de la terminal)

NOTA: este token dura 30dias o mas depende de la opcion q elijamos a la hora de crearla

5. Enter y Listo! , el codigo se subio a la repo.


**RAMAS EN GIT o BRANCHES**
Notar que en nuestra terminal nuestra rama se llama por defecto "master" entonces en mi caso el paso 4. de ***CONECTANDO CON GITHUB*** no me funciono. (Esto pasa porque por defecto de github nuestra rama del repo se llama "main")

`git branch`   :me dice en que rama me encuentro, y cuales hay.

`git checkout -b nameDeRamaNueva`  : crea una nueva rama

`git checkout nombreDeRama`    :Cambia a la rama que yo quiero utilizar.

`git log --oneline`    :me da el historial de los cambios en mi rama

`cat nameArchivo`    :me muestra el contenido de un archivo.

`git merge nombreOtraRama`   :sirve para pasar los cambios de otra rama a mi rama principal (debo situarme ahi)

`git branch -d nombreRamaAEliminar`   :elimina de forma local una rama (para llo debemos situarno en otra rama)

`git push origin --delete nombreRamaAEliminar`  :sube los cambios al repo.remoto     


**REPOSITORIOS REMOTOS Y LOCALES**

REMOTO : lo que se sube a gitHub ejemplo

LOCAL : lo que se crea dentro de los comandos en git

`git remote -v`  -> indica las conexiones remotas que tiene nuestro proyecto local

`git remote set-url origin urlDemiRepoRemota`   -> Para cambiar la URL de tu repositorio remoto en Git tan solo    
                                  escribimos el siguiente código agregando la nueva dirección


NOTA: git pull --rebase urlDemiRepoRemoto
En lugar de utilizar git merge para integrar la rama remota en la local, usa git rebase. Me ayudo a actualizar los cambios de mi rama remota a la local y viceversa.

**¿Cómo eliminar un repositorio de Git creado con ‘git init’ en un directorio?**
`rm -rf .git`

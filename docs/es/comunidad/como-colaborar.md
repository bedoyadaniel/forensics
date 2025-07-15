---
title: Comunidad - ¿Cómo colaborar con este repositorio?
summary: Paso a paso para contribuciones en github
keywords: forense, comunidad, contribucion
authors: Daniel Bedoya Arroyo
lang: es
tags: [comunidad, issue, pull request, commit, github intro]
last_updated: 2025-07-14
some_url:
---


# ¿Cómo colaborar con este repositorio?

El repositorio se encuentra actualmente en GitHub, por lo que existen **dos maneras principales** de colaborar con este repositorio:

* [***Issues***](https://github.com/Socialtic/forensics/issues): Los *issues* o **problemas son reportes o solicitudes relacionadas con el contenido** del repositorio.  Ejemplos de *issues* son reportes de errores de ortografía, correcciones a enlaces, mejoras en la redacción, entre otros. Para reportar un problema no es necesario tener familiaridad con github, markdown o la estructura de los contenidos. Los *issues* reportados recibirán respuesta por parte del equipo gestor del repositorio. 

* [***Pull request***](https://github.com/Socialtic/forensics/pulls): Los *pull request* **son solicitudes de integración donde se solicita aplicar cambios** al repositorio, de forma frecuente para mejorar, corregir o expandir el contenido del repositorio. **Los *pull requests* son revisados por el equipo responsable del proyecto**, y de considerarse apropiados se aprobarán e incluirán en la versión pública del repositorio. 

## Propuestas de mejora o correcciones a través de issues

Si encuentras algún error, o tienes una propuesta de mejora **[puedes iniciar un *issue* o problema en el repositorio siguiendo este enlace](https://github.com/Socialtic/forensics/issues/new)**. A través del *issue* será posible sugerir, discutir e implementar cambios y mejoras al contenido. No importa si el error es sencillo, como por ejemplo una falta ortográfica: **nos encanta recibir reportes de mejora al contenido**. 

A la hora de levantar un issue, te solicitamos utilizar el formato descrito en el documento [*issue template*](https://github.com/Socialtic/forensics/blob/main/.github/ISSUE_TEMPLATE/official_template.md), que se cargará de forma automática al intentar abrir un nuevo *issue* en el repositorio: 

![Tab de issues del repositorio forensics, para generar un nuevo issue utilizar el botón de new issue que se encuentra en la parte superior derecha de la interfaz web de GitHub.](/comunidad/assets/img/community-new-issue.jpg "imagen 1"){ loading=lazy }
/// caption
**imagen 1.** Tab de issues del repositorio forensics, para generar un nuevo issue utilizar el botón de new issue que se encuentra en la parte superior derecha de la interfaz web de GitHub.
///

Al dar *click* en el botón, se presentará la opción para seleccionar un formato. Seleccionar la opción de *issue template.*  

![Pop-up para seleccionar una plantilla, dentro del tab de *issues* del repositorio forensics. Se despliega al hacer click en el botón de nuevo *issue.* ](/comunidad/assets/img/community-new-issue-pop-up.jpg "imagen 2")
/// caption
**imagen 2.** Pop-up para seleccionar una plantilla, dentro del tab de *issues* del repositorio forensics. Se despliega al hacer click en el botón de nuevo issue.
///


Al utilizar la opción de un formato predefinido como el *issue template* se abrirá una interfaz desde donde se puede editar el texto del tema a reportar utilizando el formato recomendado. Recomendamos **utilizar el *template* pre-cargado y eliminar** cualquier sección que no sea relevante. 

![Ejemplo de reporte de un *issue* a través de la interfaz gráfico de GitHub en el repositorio forensics.](/comunidad/assets/img/community-new-template.jpg "imagen 3") 
/// caption
**imagen 3.** Ejemplo de reporte de un *issue* a través de la interfaz gráfico de GitHub en el repositorio forensics.
///


## Solicitudes de integración a través de *pull request*

Para **proponer una integración de cambios al repositorio** puedes seguir los siguientes pasos: 

1. Utilizando **tu propia cuenta de Github (o una cuenta organizacional si es la preferencia),** haz [una bifurcación](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) o *fork* del repositorio  

```
!!! tip "Recomendación"
   Puedes hacerlo desde el navegador web en [github.com](http://github.com), utilizando el **botón “Fork”** en la parte superior derecha del [repositorio principal](https://github.com/Socialtic/forensics), tal y como se muestra en la imagen 4.
```

![Interfaz de GitHub para el repositorio forensics, donde se resalta la opción para bifurcar el repositorio](/comunidad/assets/img/community-fork-tab.jpg "imagen 4")
/// caption
**imagen 4.** Interfaz de GitHub para el repositorio forensics, donde se resalta la opción para bifurcar el repositorio.
///


2. Desde el *fork* del repositorio, crea una nueva rama o *branch* donde podrás hacer los cambios pertinentes.

```
!!! tip "Recomendación"
   - Usa **nombres descriptivos** para tus ramas, como “fix-guia-acquisition”, “add-tutorial-analyzing-mvt-bugreport  
   - Puedes hacerlo en github dando click a la sección de *“branches”* como se muestra en la imagen 5.   
```  

![Interfaz de GitHub para el fork del repositorio forensics, donde se resalta la sección para consultar las ramas o branches.](/comunidad/assets/img/community-fork-branch-tab.jpg "imagen 5")  
/// caption
**imagen 5.** Interfaz de GitHub para el fork del repositorio forensics, donde se resalta la sección para consultar las ramas o branches.
///

Desde la sección de *branches*, puedes hacer una nueva rama o *branch* **dentro de tu copia o *fork* del repositorio**, tal y como se muestra en la imagen 6. 

![Interfaz de GitHub para el *fork* del repositorio forensics en la sección de branches, donde se resalta la opción para crear una nueva rama.](/comunidad/assets/img/community-fork-new-branch.jpg "imagen 6")  
/// caption
**imagen 6** Interfaz de GitHub para el *fork* del repositorio forensics en la sección de branches, donde se resalta la opción para crear una nueva rama.
///

3. **Realiza tus cambios y haz *commits*** claros, especificando los cambios o ajustes realizados. La imaen 7 muestra un ejemplo de un *commit*.

```
!!! tip "Recomendación"
   - Sigue las recomendaciones oficiales de [Git Guides para hacer *commits*](https://github.com/git-guides/git-commit)  
   - Cuando hagas cambios en algún documento a través de la interfaz web, GitHub confirmará la rama o *branch* a la cual se le deben aplicar los cambios. Utiliza la rama que creaste. 
```

![Interfaz de GitHub para el repositorio forensics, donde se muestra el formulario a completar cuando se realiza un cambio o commit.](/comunidad/assets/img/community-fork-commit.jpg "imagen 7")
/// caption
**imagen 7.** Interfaz de GitHub para el repositorio forensics, donde se muestra el formulario a completar cuando se realiza un cambio o commit.
///


4. Abre un pull request   

```
!!! tip "Recomendación"
   - Sigue el formato establecido descrito en la [plantilla de  pull request](https://docs.google.com/document/d/1elOOTVjq389TSSrClmDtlTEiYsCHXQCadvZfFzHmfs4/edit?tab=t.0#heading=h.j3djtr277ooi), y envía tu solicitud de integración.   
   - Puedes enviar la solicitud utilizando la interfaz web de Github, y dando click en la opción que se presenta para hacer una solicitud de integración luego de hacer cambios en una rama, tal y como se muestra en la **imagen 8.** 
```


![Interfaz de GitHub para un fork del repositorio forensics, donde se muestra la opción para comparar y enviar una solicitud de integración al repositorio principal.](/comunidad/assets/img/community-fork-compare-pull-request.jpg "imagen 8")
/// caption
**imagen 8.** Interfaz de GitHub para un fork del repositorio forensics, donde se muestra la opción para comparar y enviar una solicitud de integración al repositorio principal.
///

La imagen 9 muestra los detalles de una solicitud de integración, utilizando el formato pre-establecido. 


![Interfaz de GitHub para un fork del repositorio forensics, donde se muestra el detalle de una solicitud de integración o pull request. ](/comunidad/assets/img/community-pull-request-template.jpg "imagen 9")
/// caption
**imagen 9.** Interfaz de GitHub para un fork del repositorio forensics, donde se muestra el detalle de una solicitud de integración o pull request. 
///

Una vez que tu solicitud de integración sea revisada y aceptada, se ve verá como la que se muestra en la imagen 10. Esto también significa que tus cambios fueron aplicados directamente al repositorio. 

![Interfaz de GitHub para el repositorio forensics, donde se muestra la revisión e integración de un pull request.](/comunidad/assets/img/community-pull-request-example.jpg "imagen 10. ")
/// caption
**imagen 10.** Interfaz de GitHub para el repositorio forensics, donde se muestra la revisión e integración de un pull request.
///

## Recursos adicionales

Agradecemos también **recursos adicionales** que puedan fortalecer la práctica forense en la sociedad civil, **aún cuando no sigan** el marco de referencia [Diátaxis](https://diataxis.fr/). Dependiendo del contenido, se puede publicar en su forma original en los recursos de comunidad o colaborar la adaptación al marco de referencia. 

Para este tipo de colaboraciones, puede escribirnos a: [**seguridad@socialtic.org**](mailto:seguridad@socialtic.org)

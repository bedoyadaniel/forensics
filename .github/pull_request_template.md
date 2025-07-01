# Pull-request template

Esta plantilla tiene la finalidad de fomentar el uso del formato establecido a los contribuidores del proyecto **Forensics** parapoder dar seguimientos a la lógica de cambios y el flujo de trabajo colaborativo.

**Agradecemos las contribuciones** hechas a este proyecto y es por eso que se plantea un formato de pull-request para continuar el orden del flujo de trabajo. Este formato incluye siguiente:

* Descripción del cambio
* Tipo de cambio
* Método de prueba
* Checklist
* Información adicional (opcional)

## Tipo de cambio

Se debe indicar el tipo de contribución que se está realizando. **Para este repositorio, la mayoría de los cambios serán cambios en la documentación**. Las opciones disponibles son:

* **Fix**: Corrección de un error o contenido incorrecto
* **Feature**: Nuevo contenido o funcionalidad (tutorial, guia, referencia, explainer)
* **Refactor**: Reestructuración o mejora interna sin cambios funcionales
* **Documentación**: Mejora o corrección de la documentación existente
* **Seguridad**: Mejora relacionada con el tratamiento de la información o protección de datos
* **Otro**: Especificar el tipo de cambio si no encaja en las anteriores categorías

## Descripción del cambio

En esta sección debe describirse con claridad qué se modificó en el proyecto. Si el cambio es complejo, puede incluir un resumen técnico, enlaces a issues relacionados o capturas de pantalla relevantes.

## Método de prueba

Aquí se explica **cómo fue validado el cambio propuesto**. Debe indicarse si se realizaron pruebas unitarias, manuales o automatizadas. También se especifica el entorno en el que se llevaron a cabo las pruebas.

Datos del entorno de prueba:

* Herramientas usadas
  * e.j androidqf, mvt-adb, mvt-bugreport, etc.
  * Versiones de las herramientas utilizadas
* Sistema operativo
* Idioma y ruta del documento que se usó de referencia.

**Dependiendo del cambio, no será necesario detallar métodos de prueba,** en particular si el ajuste responde a cambios en la sintaxis y organización del contenido.

## Checklist

Antes de enviar el pull request, marca con una X lo que aplica de la siguiente Checklist:

- [ ] El contenido respeta la estructura y estilo definidos por el proyecto
- [ ] El formato es claro, consistente y accesible para personas con conocimientos técnicos básicos
- [ ] La contribución se integra correctamente dentro del marco Diátaxis
- [ ] Se respetan los lineamientos de estilo del idioma
- [ ] No se incluye información sensible, privada o irrelevante para el objetivo de los contenidos.

## Información adicional (opcional)

Si existe información relevante que deba ser compartida, como **riesgos detectados, requerimientos especiales o dependencias externas**, debe incluirse en esta sección.

**Nota:** Esta plantilla tiene como objetivo mantener un proceso ordenado, seguro y trazable para todas las contribuciones que se realicen al proyecto Forensics. Forma parte de las políticas de control y colaboración del equipo de seguridad digital y está alineada con los principios de control de cambios y trazabilidad de versiones.

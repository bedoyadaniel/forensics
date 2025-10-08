---
title: Comunidad - Traducciones y localizaciones
summary: Consideraciones sobre traducciones y localizaciones
keywords: forense, comunidad, contribucion, traducción, traducir
lang: es
tags: [comunidad, intro, traducir]
last_updated: 2025-07-14
some_url:
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---
# Traducciones y localizaciones

!!! warning "Tradução em Português ainda não disponível"
    Este recurso **ainda não foi traduzido para o português**. Estamos exibindo a versão em espanhol, e você também pode consultar a versão em inglês. Se você quiser, pode contribuir com a tradução deste recurso — ficaríamos muito felizes com sua colaboração! Para isso, consulte nossos [recursos da comunidade](comunidad/como-colaborar.md).

Desde SocialTIC comprendemos la importancia de mantener **recursos accesibles**, de **fácil lectura** y que puedan generar un impacto en **poblaciones con diferentes capacidades técnicas y en múltiples regiones del mundo**. Debido a nuestra experticia y ubicación geográfica, nuestros recursos frecuentemente estarán **disponibles primero en idioma español,**  y de forma posterior se destinarán los recursos necesarios para la **traducción al idioma inglés**.  Si tienes interés en **colaborar con la traducción de recursos del español al inglés**, o viceversa, por favor escríbenos a [**seguridad@socialtic.org**](mailto:seguridad@socialtic.org). 

Si tienes interés en traducir los contenidos del repositorio a un **nuevo idioma**, te solicitamos **informarnos a través de un nuevo *issue* o directamente a través de seguridad@socialtic.org**. Si bien concordamos en la importancia de localizar recursos, existen algunas consideraciones importantes antes de iniciar una traducción: 

* Capacidad y sostenibilidad: La traducción y localización de contenidos es un **trabajo arduo,** y desde **SocialTIC agradecemos cualquier esfuerzo** que impulse el análisis forense consensuado en poblaciones vulnerables, especialmente de la mayoría global. Sin embargo, antes de iniciar una traducción, recomendamos **evaluar la sostenibilidad del esfuerzo**  en el mediano-largo plazo.  
* Revisión de los contenidos: En nuestra experiencia, es ideal que además de la traducción inicial, **una segunda persona realice una revisión secundaria**. Si tienes problemas para identificar una segunda contraparte para revisar una traducción, puedes informarnos para apoyar en la coordinación.   
* Actualización y mantenimiento: Nuestra visión es que el **repositorio estará en constante crecimiento y actualización**. Esperamos que los **primeros años sean los más intensos** en la producción de contenidos de triaje y adquisición, para luego enfocarse en contenidos más especializados.   
* Reglas de estilo: Sugerimos generar unas reglas de estilo breves que consideren por ejemplo el **uso de anglicismos, lenguaje inclusivo, entre otros**.    
* Licencia de uso:  Este repositorio extiende [la licencia de MVT](https://docs.mvt.re/en/latest/license/) para fomentar el análisis forense consensuado. 

### Organización de los contenidos

El repositorio se encuentra **estructurado para aceptar traducciones a nuevos idiomas**. En general, los contenidos en todos los idiomas **se estructuran de la siguiente manera**: 

```
docs/
en/
explainers/
how-tos/
references/
tutorials/
community/
index.md
es/
explainers/
how-tos/
references/
tutoriales/
comunidad/
index.md

```

Adicionalmente, **cada nuevo contenido tendrá su propia carpeta correspondiente**, donde se aloja el archivo en formato markdown con los contenidos. Por ejemplo, el contenido *Explainer:* *Introducción a la forense digital consentida para la defensa de los derechos humanos* se organiza de la siguiente forma en el idioma inglés y español: 

```
es/
explainers/
01-explainer-introduccion-forense-digital/
01-explainer-introduccion-forense-digital.md
en/
	explainers/
		01-explainer-introduction-digital-forensics/
			01-explainer-introduction-digital-forensics.md
	
```

Antes de comenzar una traducción, recomendamos explorar las carpetas de contenidos, y consultar ante cualquier duda. Se recomienda además revisar los **lineamientos de estilo para la nomenclatura de archivos incluídos como parte de las mejores prácticas** de contribución del repositorio.     

Para realizar contribuciones directamente al repositorio en relación a traducciones, se recomienda seguir las instrucciones en la sección de *pull requests* o solicitudes de integración. 

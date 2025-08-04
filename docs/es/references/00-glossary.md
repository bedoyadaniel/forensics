---
title: Glosario 
summary: Glosario 
keywords: glosario
authors: Daniel Bedoya Arroyo
lang: es
tags: [glossary, glosario, reference]
last_updated: 2025-08-04
some_url:
---


# Glosario

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](https://diataxis.fr/).

Este recurso en particular es un glosario de términos que incluye **conceptos, abreviaciones y otros términos** que se consideran de importancia para la comprensión de los contenidos. 

## Términos

### Adquisición

Se refiere a una etapa de investigación forense, la persona analista forense debe determinar la mejor forma de recolectar la evidencia forense. **Qué priorizar y cómo realizar la extracción dependerá de diversos factores**, entre ellos el tipo de incidente, el tipo de atención (en sitio o remota), la [volatilidad de la evidencia](https://www.sciencedirect.com/topics/computer-science/volatile-evidence) y el esfuerzo requerido para la extracción. Consideraciones adicionales para la extracción incluyen lo siguiente:


### Análisis de riesgos

Los riesgos particulares que una organización o individuo enfrenta, **dependen del contexto y de su trabajo particular**. Al proceso de identificar vulnerabilidades, riesgos y amenazas en un momento determinado se le conoce como análisis de riesgos. 

### AndroidQF

[AndroidQF](https://github.com/mvt-project/androidqf) es una herramienta de software libre y de código abierto **enfocada en la extracción forense de dispositivos Android**. Actualmente mantenida por el [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/es/). 

Su enfoque está pensado especialmente para periodistas, activistas, defensores de derechos humanos y los **laboratorios técnicos que acompañan casos de vigilancia digital y amenazas de software espía.**

### Artefacto forense

Un artefacto forense se refiere a la evidencia o los datos recuperados durante el análisis forense digital, lo incluye arhivos, registros de procesos, logs, metadatos, etc. 

### Cadena de custodia

Al proceso de documentar con claridad quién y de qué forma se manipula  la evidencia se le conoce como **cadena de custodia**. La evidencia forense puede ser manipulada o destruída durante el proceso forense, por lo que la persona analista debe ser capaz de demostrar la [integridad de la evidencia](https://www.ibm.com/es-es/topics/data-integrity).  En caso de que esta demostración no sea posible o suficientemente robusta, es posible que las evidencia **no sea admisible en procesos judiciales**, o sea refutada y desestimada por otros especialistas.

### Consentimiento informado

El [consentimiento](https://es.wikipedia.org/wiki/Consentimiento) es un principio que hace referencia a la exteriorización de la voluntad entre dos o más personas para aceptar derechos y obligaciones. En el contexto de análisis forense digital en beneficio de personas de la sociedad civil, el consentimiento informado se refiere al **acuerdo y aprobación de acciones para facilitar la recolección, análisis, presentación y preservación de evidencia digital**. 

Un aspecto clave en cualquier acuerdo de consentimiento es la capacidad de quién acepta el acuerdo de tomar una **decisión informada** sobre el curso de la investigación, e incluso poder rechazar la asistencia. En la práctica forense, esto significa brindar toda la información necesaria para que quién solicita el análisis comprenda las acciones, riesgos, derechos y obligaciones que conlleva el proceso de investigación. Es importante que la **persona analista se comunique de forma clara y transparente**, y respete la voluntad de quién solicita el apoyo. 

### Copia bit a bit

Copia bit a bit, DD o duplicación de disco se refiere al proceso de crear una réplica exacta de un medio electrónico. Permiten proteger la evidencia original, de forma tal que se proteja su integridad y se preserve en apego a mejores prácticas. 

### CVE

Es un programa de reporte, clasificación y publicación de vulnerabilidades de seguridad. Se establecen registros CVE únicos para cada vulnerabilidad, como por ejemplo ```CVE-2014-0160```

### DFIR (Digital Forensics and Incident Response)

Si la respuesta a un incidente y el análisis forense se realizan por separado, las acciones que se tomen podrían interferir y dificultar tanto la respuesta como el análisis. Por ejemplo, **al responder** a un incidente sin tomar en cuenta las necesidades de preservación de evidencia, **se podrían alterar o destruir pruebas** y artefactos necesarios para el análisis forense. De la misma manera, si únicamente nos enfocamos en el análisis forense, se podría **retrasar la contención de la amenaza** e incrementar las consecuencias y el tiempo de resolución de un incidente.

Por lo tanto, **resulta ventajoso [combinar ambos procesos](https://www.paloaltonetworks.es/cyberpedia/digital-forensics-and-incident-response)**, de manera que durante la respuesta a un incidente se consideren mejores prácticas para la recolección y preservación de evidencia, y se utilicen hallazgos producto del análisis forense para contener y erradicar amenazas, y, ultimadamente, se prevengan futuros incidentes.

### Exploit

[Exploit](https://es.wikipedia.org/wiki/Exploit) es una palabra inglesa que significa explotar o aprovechar, y que en el ámbito de la informática es un fragmento de software, fragmento de datos o secuencia de comandos o acciones, utilizada con el fin de aprovechar una vulnerabilidad de seguridad de un sistema de información para conseguir un comportamiento no deseado del mismo.
​

### Forense digital

La forense digital es el proceso utilizado para la recolección, preservación, análisis y presentación de evidencia digital derivada de medios y dispositivos electrónicos, utilizando **técnicas de investigación y métodos científicos** que sean fiables, acertados y repetibles, de forma tal que los resultados puedan ser utilizados en **procedimientos judiciales**.[1](https://csrc.nist.gov/glossary/term/digital_forensics)

La forense digital se utiliza para descubrir y examinar datos de dispositivos electrónicos con el objetivo de **identificar, recuperar, documentar e interpretar la información** digital y su conexión con [ataques digitales](https://protege.la/ataques/). La utilización de procedimientos estándar, en apego a mejores prácticas, **permite generar evidencia útil** que impulse acciones de **rendición de cuentas**, que pueda reducir la impunidad con la que se ejecutan ataques digitales.


### Google Takeout

Es una función para cuentas en línea de Google que permite extraer información de diferentes aplicaciones, registros de acceso, logs de seguridad, correo electrónico, entre otros. El proceso tarda algunos días en completarse. 

 [Sige este enlace para acceder a la función e inicar un takeout request.](https://takeout.google.com/?pli=1).  


### Guerra legal (lawfare)

Guerra legal o lawfare se refiere al uso del sistema o instituciones legales para dañar, desacreditar o afectar individuos o organizaciones. Por ejemplo, en relación al caso en las cortes de Estados Unidos entre NSO y WhatsApp, el Citizen Lab enfrentó una serie de recursos y solicitudes legales que buscaban desmantelar su trabajo y acceder a información sensible, incluída la lista de víctimas. En otro ejemplo, en 2018 la empresa Candiense Sandvine amenazó al Citizen Lab con una demanda por difamación a raíz de su publicación concerniente al uso de equipos Sandvine para la implantación de spyware.  

### Hash

[Hash](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) son  funciones de criptográficas, que permiten producir un único valor para un conjunto de datos dados. Ejemplos incluyen MD5, SHA1. 

### Identificación

Se refiere a una etapa de investigación forense, donde la persona analista determina **cuáles dispositivos, cuentas o sistemas podrían contener información relevante para la investigación**. Ejemplos de dispositivos incluyen teléfonos móviles, computadoras, cuentas en línea, medios de almacenamiento, entre otros. Idealmente, para determinar la evidencia a recolectar, la persona analista debe tener contacto con la persona impactada, para entender qué sucedió, qué acciones se han tomado hasta el momento y qué evidencia podría estar disponible.

### Indicador de compromiso (IOC)

[Un indicador de compromiso o IDC](https://es.wikipedia.org/wiki/Indicador_de_compromiso) (en inglés: indicator of compromise, IoC) es toda aquella información relevante que describe cualquier incidente de ciberseguridad, actividad y/o artefacto malicioso, mediante el análisis de sus patrones de comportamiento.[1]​ La intención de un indicador de compromiso es esquematizar la información que se recibe o se extrae durante el análisis de un incidente, de tal manera que pueda reutilizarse por otros investigadores o afectados, para descubrir la misma evidencia en sus sistemas y llegar a determinar si han sido o no comprometidos ya sea desde el punto de vista de monitorización frente a amenazas o por análisis forense.[2]​ Por ejemplo, se identifican ficheros creados, entradas de registro modificadas, procesos o servicios nuevos. La idea subyacente es que, si se analiza un sistema y se encuentran los detalles recogidos en un indicador de compromiso concreto, se está ante una infección provocada por el programa malicioso (malware) al que hace referencia dicho indicador de compromiso.[3]​ Los indicadores de compromiso permiten realizar un intercambio sencillo y práctico de información con el fin de detectar intrusos a partir de análisis forenses, respuestas a incidentes o análisis de malware.

### Log (bitácora)

Los logs, también conocidos como registros o bitácoras, son archivos que documentan actividades que ocurren dentro de un sistema informático, red o aplicación. Estos registros pueden contener información sobre accesos de usuarios, cambios en el sistema, errores, y otras actividades relevantes para una investigación forense. 

En este recurso detallamos consideraciones importantes sobre [investigaciones forenses basadas en logs en dispositivos Android](../explainers/03-explainer-forense-logs-android/03-explainer-forense-logs-android.html). 

### Malware

[De acuerdo a wikipedia](https://es.wikipedia.org/wiki/Malware), un malware, traducido del inglés como programa malicioso, programa maligno, programa malintencionado o código maligno, es cualquier tipo de software que realiza acciones dañinas en un sistema informático de forma intencionada (al contrario software defectuoso) y sin el conocimiento del usuario (al contrario que el software potencialmente no deseado. 

### MVT

MVT es una herramienta para facilitar el análisis forense consentido de dispositivos que pertenezcan a personas que podrían ser objetivo de ataques de spyware avanzados, y en específico personas parte de la sociedad civil y de comunidades en riesgo.

Se indica en su [sitio web](https://forensics.socialtic.org/comunidad/licencia.html):

_Mobile Verification Toolkit (MVT) is a tool to facilitate the consensual forensic analysis of Android and iOS devices, for the purpose of identifying traces of compromise._

_It has been developed and released by the Amnesty International Security Lab in July 2021 in the context of the Pegasus Project along with a technical forensic methodology. It continues to be maintained by Amnesty International and other contributors._

_In this documentation you will find instructions on how to install and run the mvt-ios and mvt-android commands, and guidance on how to interpret the extracted results._

### Notificación de amenaza (Threat notification)

### n-day

### Persona experta (perito/a)

### Phishing

### Proveedor de servicios de Internet (ISP)

### Respuesta a incidentes de seguridad

La [respuesta a incidentes](https://www.ibm.com/es-es/topics/incident-response) se centra en **detectar y responder a eventos de seguridad**. A través de procedimientos de respuesta, se pretende minimizar el impacto y contener las consecuencias de los incidentes. Para una respuesta efectiva, es importante identificar la causa raíz de las intrusiones, de forma tal que se pueda erradicar la amenaza y se logre una recuperación oportuna.

### Software espía (spyware)

### Stalkerware

### TTP

### Triaje

### Volatilidad

### Vulnerabilidad

### Zero click

### Zero day

---
title: Diccionario de archivos generados por la herramienta androidqf 
summary: dictionary of androidqf resulting files 
keywords: android, androidqf, reference
lang: es
tags: [explainer, intro]
last_updated: 2025-06-16
some_url:
created: 2025-06-16
comments: true
name: jose

---


# Diccionario de archivos generados por la herramienta androidqf 

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis/).

Este recurso en particular se enmarca dentro de la categoría de [referencias](https://diataxis.fr/reference), y contiene información sobre los archivos generados por [androidqf](../../references/00-glossary/index.md#androidqf) al realizar una extracción forense de un dispositivo Android, esto con el objetivo de que una persona analista **conozca los archivos generados, cómo utilizarlos, donde buscar información específica y en qué formato la encontrará.**

Este recurso se actualizó por última vez el 16 de Junio del 2025 y para la recopilación de la información se tomó como base la [versión 1.7.1](https://github.com/mvt-project/androidqf/tree/v1.7.1).

[Androidqf](https://github.com/mvt-project/androidqf) es una herramienta de extracción forense que pertenece al [MVT Project](https://github.com/mvt-project/). Es mantenida actualmente por el [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/es/).

Su nombre viene de la frase en inglés *Android Quick Forensics*. Se caracteriza por ser una **herramienta portable**, es decir se puede ejecutar en Windows, GNU/Linux y Mac OS mediante un binario precompilado, lo que simplifica la [adquisición de información forense](../../explainers/01-explainer-introduction-digital-forensics/index.md#cómo-se-aplica-la-forense-digital-en-la-práctica-de-defensa-de-derechos-humanos) de dispositivos Android. 

La información generada por androidqf se puede agrupar en 5 categorías principales:

* Detalles de la adquisición  
* Configuración del dispositivo  
* Información sobre registros y eventos del sistema  
* Procesos y aplicaciones  
* Archivos respaldados

## Adquisición y extracción

### acquisition.json

La información de este archivo se genera mediante el módulo [acquisition.go](https://github.com/mvt-project/androidqf/blob/main/acquisition/acquisition.go)*.*

**¿Qué contiene este archivo?**

Este archivo se encuentra en formato *json* y registra información relacionada con el proceso de adquisición de datos del dispositivo. Contiene la siguiente información: 

* Identificador único o UUID de la extracción (se utiliza cómo nombre de la carpeta donde se almacena la información.  
* Versión de androidqf.  
* Ubicación donde se almacena la extracción.  
* Fecha y hora de inicio y finalización de la adquisición.  
* Información del binario *collector* utilizado.  
* Información del binario *adb* utilizado.  
* Ubicación del almacenamiento de *sdcard*.  
* Arquitectura del CPU del dispositivo.

**¿Por qué es importante?**

Esta información permite conocer información básica de la extracción y obtener identificadores únicos del sistema que facilitan el [proceso de custodia de la extracción  forense](../../explainers/01-explainer-introduction-digital-forensics/index.md#cadena-de-custodia). 

**Ejemplo:**

```
{
 "uuid": "0f615832-ed22-411e-9317-b429d28ecf9a",
 "androidqf_version": "v1.7.0-1-gf7642bf",
 "storage_path": "/home/user/0f615832-ed22-411e-9317-b429d28ecf9a",
 "started": "2025-01-01T18:36:37.443498116Z",
 "completed": "2025-01-01T18:50:04.947856405Z",
 "collector": {
  "ExePath": "/data/local/tmp/collector",
  "Installed": false,
  "Adb": {
   "ExePath": "/usr/bin/adb",
  },
  "Architecture": "arm64-v8a"
 },
 "tmp_dir": "/data/local/tmp/",
 "sdcard": "/sdcard/",
 "cpu": "arm64-v8a"
}
```

### command.log

La información de este archivo se genera mediante el módulo [logger.go](https://github.com/mvt-project/androidqf/blob/main/log/logger.go). Este módulo presenta los logs del proceso de captura y adquisición de la información. 

**Información contenida**

Este archivo se encuentra en texto plano con una extensión *.log* y contiene un registro de los comandos ejecutados durante la adquisición de datos. Documenta cada comando usado (*DEBUG*) y su salida en pantalla (*INFO*), mensajes de alertas (*WARNING*) y mensajes de errores (*ERROR*) durante la ejecución. Utiliza el siguiente formato: 

* Fecha y hora del comando o mensaje  
* Tipo de mensaje  
* Contenido del mensaje

**¿Por qué es importante?**

Permite generar un registro de las acciones realizadas por la aplicación durante la adquisición de información. A través de este registro, es posible  verificar la completitud de la extracción, asegurando que todos los pasos fueron realizados; o en caso de existir alertas o errores, permite identificarlos. 

**Ejemplo del contenido del archivo**

```
2025-01-01T14:22:39-06:00 [INFO] Started new acquisition in /home/user/1c3c6742-f225-479f-a836-4a6a86a056b7
2025-01-01T14:22:39-06:00 [INFO] Would you like to take a backup of the device?
2025-01-01T14:22:41-06:00 [INFO] Generating a backup with argument com.android.providers.telephony. Please check the device to authorize the backup...

2025-01-01T14:22:52-06:00 [INFO] Backup completed!
2025-01-01T14:22:52-06:00 [INFO] Collecting information on installed apps. This might take a while...
2025-01-01T14:22:52-06:00 [INFO] Collecting device properties...
2025-01-01T14:22:52-06:00 [INFO] Collecting device diagnostic information. This might take a while...
2025-01-01T14:24:11-06:00 [INFO] Collecting list of running processes...
2025-01-01T14:24:11-06:00 [DEBUG] Deploying collector binary 'collector_arm64' for architecture 'arm64-v8a'.
2025-01-01T14:24:11-06:00 [INFO] Collecting list of services...
2025-01-01T14:24:12-06:00 [INFO] Generating a bugreport for the device...
2025-01-01T14:26:22-06:00 [DEBUG] Bugreport completed!
2025-01-01T14:26:22-06:00 [INFO] Collecting list of files... This might take a while...
2025-01-01T14:26:22-06:00 [DEBUG] Using collector to collect list of files
2025-01-01T14:39:20-06:00 [INFO] Collecting device settings...
2025-01-01T14:39:20-06:00 [INFO] Collecting SELinux status...
```

### hashes.csv

La información de este archivo se genera mediante la función [*HashFiles*](https://github.com/mvt-project/androidqf/blob/main/acquisition/acquisition.go#L134) del módulo [acquisition.go](https://github.com/mvt-project/androidqf/blob/main/acquisition/acquisition.go)*.*

**Información contenida**

Este archivo se encuentra en formato [csv](https://en.wikipedia.org/wiki/Comma-separated_values) y almacena los hashes [SHA-256](https://es.wikipedia.org/wiki/SHA-2) para cada archivo generado durante la extracción o copiado desde el dispositivo. Sigue la estructura: 

* Ubicación y nombre del archivo  
* Valor hash utilizando *sha256*

**¿Por qué es importante?**

Los hashes permiten garantizar la integridad de la información y asegurar que no hayan sido modificados después de la adquisición, favoreciendo también procedimientos de cadena de custodia.

**Ejemplo del contenido del archivo**

```
2ab44150-35d3-4b40-a820-c9152fe93a13\apks\gov.dhs.cbp.cbpone_gov.dhs.cbp.cbpone-NYwrqdamzef6AVKRRGXzgA.apk,2d553aada9039d4def18a09b84c317a70d9fdde87524a043db5f0eeb1862e89a
2ab44150-35d3-4b40-a820-c9152fe93a13\backup.ab,48202a8cb422d7eeb12ff8ad13fac3a67b37600c63eae8089d9674465da32990
2ab44150-35d3-4b40-a820-c9152fe93a13\bugreport.zip,ec82812dba70891b78d7130dc16e3474918e4a0e02bb15ec00e1015679f720ee
2ab44150-35d3-4b40-a820-c9152fe93a13\command.log,c0ae883bebee7503b0ca94a54cdbb43628602046c68b770c760f730a55d6dc8c
2ab44150-35d3-4b40-a820-c9152fe93a13\dumpsys.txt,e54a613502ca362584766c0f75e17ca366d7ecdc4aa6869c50424dff83acbc15
2ab44150-35d3-4b40-a820-c9152fe93a13\env.txt,387301687084cca0e124a9c365e930b4e5e6303b3e6f9dc64e2146f168b79c1a
2ab44150-35d3-4b40-a820-c9152fe93a13\files.json,832f8121a69f131c9f434e1ca68d7b1e2deda40de72ff8396ea386a6a8cf69d3
2ab44150-35d3-4b40-a820-c9152fe93a13\getprop.txt,b8dbad7e900aeeb3c60e48dd988c44905741a7e5b124055a09c2c417aa1556b3
2ab44150-35d3-4b40-a820-c9152fe93a13\hashes.csv,cea94f56c720436d217b44ee746e2a6d69ddd226325a94bf3a3adeb32be4658a
2ab44150-35d3-4b40-a820-c9152fe93a13\logcat.txt,6c080ba0357c6e82818e5a89135ff06aa9386f811daf898fc1797e1b9e6299d3
2ab44150-35d3-4b40-a820-c9152fe93a13\logs\data\anr\anr_2024-12-20-00-11-38-831,e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
2ab44150-35d3-4b40-a820-c9152fe93a13\logs\sdcard\log\thermal_log-shm,e9eed4a2f55edd11e022b7b089d69a5de929d2bd484041a64e957861a5ab055b
2ab44150-35d3-4b40-a820-c9152fe93a13\packages.json,69d560bfbbb75e074a49d107811c350461badac885b3925ed816d716f1f1144a
2ab44150-35d3-4b40-a820-c9152fe93a13\processes.txt,9e933447e79e4743722691af88e9a4bdcc11029a92b84b0ebd9d54e0bfcf2694
2ab44150-35d3-4b40-a820-c9152fe93a13\root_binaries.json,4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
2ab44150-35d3-4b40-a820-c9152fe93a13\selinux.txt,1ca5672ae970bdc4f5b584898245b3d884e11deb6867e9563bdfbc8b82e8f62e
2ab44150-35d3-4b40-a820-c9152fe93a13\services.txt,b3ae6ad626b3a5ba8fc3b68771d42baf9795e03cc7b4b1ccbe361d9625e0f1fe
2ab44150-35d3-4b40-a820-c9152fe93a13\settings_global.txt,410f788450907331183ee36979e93fc7dc0b1805e574d1ac1d5fbc9869897c53
2ab44150-35d3-4b40-a820-c9152fe93a13\settings_secure.txt,be67f431c457edfb88d733594aba662310dbe3863c62da21cbf7dad5bcc0f136
2ab44150-35d3-4b40-a820-c9152fe93a13\settings_system.txt,b0e7452110867ca3f5c15ea52b9b9a198433a836f97d6fd8b95fcd39fd30c714
```

## Información y configuración del dispositivo 

### getprop.txt 

La información de este archivo se genera mediante el módulo [getprop.go](https://github.com/mvt-project/androidqf/blob/main/modules/getprop.go)*.*

**Información contenida**

Este archivo se encuentra en formato *TXT* y contiene la salida del comando de `adb getprop`, el cual detalla las **propiedades del sistema**.

Las propiedades del sistema son pares clave-valor de cadenas que se almacenan en el diccionario global [*build.prop*](https://xdaforums.com/t/guide-build-prop-wiki.2056266/) o en archivos de descripción *.sysprop*, y proporcionan una forma conveniente de compartir configuraciones dentro del sistema. 

La información se puede encontrar utilizando el siguiente formato:

```
[{prefix}.]{group}[.{subgroup}]*.{name}[.{type}]
```

Algunas propiedades aparecen con el prefijo *ro*, lo que indica que son propiedades de solo lectura, o que fueron asignadas luego del reinicio del dispositivo. Las propiedades con el prefijo *persist* se refieren a configuraciones resistentes al reinicio. Algunas propiedades no tendrán prefijo, por lo que inician directamente con el grupo al que pertenecen. 

Los grupos más comunes son:

* *bluetooth*, relacionado con Bluetooth  
* *boot*, sysprops de cmdline del kernel  
* *build*, sysprops que identifican una compilación  
* *telephony*, relacionado con la telefonía  
* *audio*, relacionado con el audio  
* *graphics*, relacionado con los gráficos  
* *vold*, relacionado con vold que gestiona el montaje de volúmenes físicos de almacenamiento externo

Para mayor detalle se puede revisar la [lista de propiedades ya definidas en el código fuente de Android](https://android.googlesource.com/platform/system/sepolicy/+/refs/heads/main/private/property_contexts).

**¿Por qué es importante?**

Las propiedades brindan información importante sobre el hardware y el software del dispositivo, las cuales pueden ser alteradas por software malicioso para ocultar su presencia o para modificar el comportamiento del dispositivo de forma inadvertida.

**Ejemplo del contenido del archivo**

```
[property_name]: [value]
[aaudio.hw_burst_min_usec]: [2000]
[aaudio.mmap_exclusive_policy]: [2]
[aaudio.mmap_policy]: [2]
[apex.all.ready]: [true]
[bluetooth.device.class_of_device]: [90,2,12]
[ro.boot.product.model]: [SM-A715F]
[ro.boot.serialno]: [R58N84XXXXX]
[ro.bootimage.build.date]: [Thu Feb 29 13:55:21 +07 2024]
[ro.bootimage.build.date.utc]: [1709189721]
[ro.bootimage.build.fingerprint]: [samsung/a71naxx/a71:11/RP1A.200720.012/A715FXXSBDXB1:user/release-keys]
[ro.build.selinux]: [1]
[ro.build.selinux.enforce]: [1]
[ro.build.version.security_patch]: [2024-02-01]
[ro.gfx.driver.1]: [com.qualcomm.qti.gpudrivers.sm6150.api30]
[ro.hardware]: [qcom]
[ro.hardware.chipname]: [SM7150]
[ro.product.system.model]: [SM-A715F]
[ro.vendor.product.cpu.abilist]: [arm64-v8a,armeabi-v7a,armeabi]
[ro.vendor.product.cpu.abilist32]: [armeabi-v7a,armeabi]
[ro.vendor.product.cpu.abilist64]: [arm64-v8a]
```

**Aprende más**

* [Descripción general de la configuración | Propiedades del sistema | Android Open Source Project](https://source.android.com/docs/core/architecture/configuration?hl=es-419#system-properties)   
* [Cómo implementar propiedades del sistema como APIs | Android Open Source Project](https://source.android.com/docs/core/architecture/configuration/sysprops-apis?hl=es-419)  
* [Agrega propiedades del sistema | Android Open Source Project](https://source.android.com/docs/core/architecture/configuration/add-system-properties?hl=es-419)  
* [Compatibilidad de políticas | Android Open Source Project](https://source.android.com/docs/security/features/selinux/compatibility?hl=es-419#system-property-and-ownership) 

### selinux.txt 

La información de este archivo se genera mediante el módulo [selinux.go](https://github.com/mvt-project/androidqf/blob/main/modules/selinux.go)*.*

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando de `adb shell getenforce` e indica la política de seguridad *SELinux* aplicada en el dispositivo, indicando el modo en el que se encuentra (*enforcing*, *permissive*, o *disabled*).

**¿Por qué es importante?**

[*SELinux*](https://en.wikipedia.org/wiki/Security-Enhanced_Linux) es una capa de seguridad clave en Android. Cambios en su configuración pueden ser un indicativo de compromisos en la seguridad del dispositivo.

**Ejemplo del contenido del archivo**

```
Enforcing
```

**Aprende más**

* [Conceptos de SELinux | Android Open Source Project](https://source.android.com/docs/security/features/selinux/concepts?hl=es-419)  
* [SELinux Project](https://github.com/selinuxproject)  
* [¿Qué es SElinux? SELinux (Security Enhanced Linux) le permite configurar el nivel de seguridad para sus sistemas Linux](https://www.redhat.com/es/topics/linux/what-is-selinux) 

### settings\_global.txt 

La información de este archivo se genera mediante el módulo [settings.go](https://github.com/mvt-project/androidqf/blob/main/modules/settings.go)*.*

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando `adb shell cmd settings list global` , el cual muestra preferencias que siempre se aplican de forma idéntica a todos los usuarios definidos ([well-defined user](https://source.android.com/docs/devices/admin/multi-user#user_types)). Las aplicaciones pueden leerlas, pero no pueden escribirlas, se trata de preferencias que el usuario debe modificar explícitamente a través de la interfaz de usuario del sistema o API especializadas para esos valores.

Estas configuraciones incluyen opciones de desarrollador, arranque, y estado de la conexión de bluetooth, wifi y telefonía. Para ver la [lista completa de preferencias globales](https://developer.android.com/reference/android/provider/Settings.Global) se puede revisar la documentación correspondiente de Android.

**¿Por qué es importante?**

Permite identificar configuraciones anómalas que podrían comprometer la seguridad, privacidad  o funcionalidad del dispositivo. Configuraciones predeterminadas inusuales pueden señalar intentos de modificar el comportamiento del sistema, intencionados o accidentales.

**Ejemplo del contenido del archivo**

```
Phenotype_boot_count=68
adb_enabled=1
airplane_mode_on=0
bluetooth_on=1
boot_count=71
bug_report=0
default_device_name=Galaxy A14 5G
package_verifier_user_consent=1
phone_play_store_availability=0
require_password_to_decrypt=1
spam_call_enable=1
subscription_mode=0
turnOff_5g_network_mode_set=0
wifi_networks_available_notification_on=0
wifi_on=1
wifi_scan_always_enabled=1
zram_enabled=1
```

**Aprende más**

* [Settings | Android Developers](https://developer.android.com/reference/android/provider/Settings?hl=es-419)   
* [Settings.Global | Android Developers](https://developer.android.com/reference/android/provider/Settings.Global?hl=es-419)

### settings\_secure.txt 

La información de este archivo se genera mediante el módulo [settings.go](https://github.com/mvt-project/androidqf/blob/main/modules/settings.go)*.*

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando `adb shell cmd settings list secure`  Muestra preferencias de seguridad del sistema que las aplicaciones pueden leer pero no escribir. Son preferencias que el usuario debe modificar explícitamente a través de la interfaz de usuario de una aplicación del sistema. Las aplicaciones normales no pueden modificar la base de datos de configuraciones de seguridad.

Estas configuraciones incluyen opciones de desarrollador, accesibilidad, ubicación, entrada de datos, bloqueo de pantalla, control parental, text-to-speech, y conexión de bluetooth, wifi y telefonía.

Para ver la [lista completa de preferencias de seguridad](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419) se puede revisar la documentación correspondiente de Android.

**¿Por qué es importante?**

Permite identificar configuraciones anómalas que podrían comprometer la seguridad, privacidad  o funcionalidad del dispositivo. Configuraciones predeterminadas inusuales pueden señalar intentos de modificar el comportamiento del sistema, intencionados o accidentales.

**Ejemplo del contenido del archivo**

```
accessibility_allow_diagonal_scrolling=1
accessibility_button_mode=1
accessibility_button_target_component=com.android.settings/com.samsung.android.settings.accessibility.shortcut.AmplifyShortcut
accessibility_display_magnification_enabled=0
accessibility_enabled=0
android_id=af4de9XXXXXXXXXX
autofill_service=null
assistant=com.google.android.googlequicksearchbox/com.google.android.voiceinteraction.GsaVoiceInteractionService
aware_enabled=0
backup_auto_restore=1
backup_encryption_opt_in_displayed=1
bluetooth_settings_foreground=0
clipboard_show_access_notifications=0
default_input_method=com.samsung.android.honeyboard/.service.HoneyBoardService
fingerprint_screen_lock=1
location_mode=3
location_time_zone_detection_enabled=1
lockscreen.disabled=0
wifi_saved_state=0
```

**Aprende más**

* [Settings | Android Developers](https://developer.android.com/reference/android/provider/Settings?hl=es-419)   
* [Settings.Secure | Android Developers](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419) 

### settings\_system.txt 

La información de este archivo se genera mediante el módulo [settings.go](https://github.com/mvt-project/androidqf/blob/main/modules/settings.go)*.*

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando `adb shell cmd settings list system` , el cual muestra diversas preferencias generales del dispositivo. Estas preferencias afectan la experiencia del usuario y el funcionamiento básico del dispositivo.

Estas configuraciones incluyen opciones de sensores como el acelerómetro o giroscopio, zona horaria, pantalla, alarmas, sonido, vibración, actualizaciones, y conexión de bluetooth, wifi y telefonía.

Para ver la [lista completa de preferencias de sistema](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419) se puede revisar la documentación correspondiente de Android.

**¿Por qué es importante?**

Permite identificar configuraciones anómalas que podrían comprometer la seguridad, privacidad  o funcionalidad del dispositivo. Configuraciones predeterminadas inusuales pueden señalar intentos de modificar el comportamiento del sistema, intencionados o accidentales.

**Ejemplo del contenido del archivo**

```
FOTA_CLIENT_POLLING_TIME=1710699386219
FOTA_CLIENT_REGISTRATION=1
FOTA_CLIENT_TEST=0
SEM_VIBRATION_FORCE_TOUCH_INTENSITY=4
SEM_VIBRATION_NOTIFICATION_INTENSITY=5
SOFTWARE_UPDATE_LAST_CHECKED_DATE=1728477705778
SOFTWARE_UPDATE_WIFI_ONLY2=1
alarm_alert_set=1
anykey_mode=0
aod_mode=0
automatic_unlock=1
block_unwanted_call=1
block_unwanted_call_type=1
lockscreen_sounds_enabled=1
lockscreen_wallpaper=1
login_state=0
mic_mode_enable=0
mic_mode_wificall=0
samsung_errorlog_agree=1
tty_mode=0
unknown_mode=0
volume_alarm=11
volume_alarm_ble_headset=11
volume_alarm_earpiece=11
volume_alarm_speaker=11
volume_assistant=7
wifi_call_enable1=0
wifi_call_preferred1=2
wifi_call_when_roaming1=0
wireless_fast_charging=0
```

**Aprende más**

* [Settings | Android Developers](https://developer.android.com/reference/android/provider/Settings?hl=es-419)   
* [Settings.System | Android Developers](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419) 

### env.txt 

La información de este archivo se genera mediante el módulo [env.go](https://github.com/mvt-project/androidqf/blob/main/modules/env.go)*.*

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando `adb shell env` el cual muestra la configuración de las variables de entorno de la terminal (shell) [*mkshrc*](http://mirbsd.de/mksh) la cual es utilizada por Android.

Por defecto las variables de *mkshrc* en Android se encuentran en el archivo *mkshrc* o *profile* que puede estar en alguno de los siguientes directorios.

```
/system/etc
/system/etc/profile
$HOME/
/data/local
```

Mientras que [el binario de *mkshrc* se puede encontrar en alguno de los siguientes directorios](https://android.googlesource.com/platform/bionic/+/refs/heads/master/libc/include/paths.h#50).

```
/product/bin
/apex/com.android.runtime/bin
/apex/com.android.art/bin
/system_ext/bin
/system/bin
/system/xbin
/odm/bin
/vendor/bin
/vendor/xbin
```

Las variables contenidas pueden indicar:

* Ubicaciones de particiones  
* Valores de entorno de ejecución de la máquina virtual de Android  
* Configuraciones de la terminal

**¿Por qué es importante?**

Las variables de entorno pueden indicar cambios en las configuraciones de la terminal, del intérprete de comandos, del entorno de ejecución de la máquina virtual de Android o de los puntos de montaje de algunas particiones y carpetas. Esto podría ser un indicador de un comportamiento sospechoso.

**Ejemplo del contenido del archivo**

```
_=/system/bin/env
ANDROID_DATA=/data
ANDROID_ART_ROOT=/apex/com.android.art
LOGNAME=shell
STANDALONE_SYSTEMSERVER_JARS=/apex/com.android.btservices/javalib/service-bluetooth.jar:/apex/com.android.devicelock/javalib/service-devicelock.jar:/apex/com.android.os.statsd/javalib/service-statsd.jar:/apex/com.android.scheduling/javalib/service-scheduling.jar:/apex/com.android.tethering/javalib/service-connectivity.jar:/apex/com.android.uwb/javalib/service-uwb.jar:/apex/com.android.wifi/javalib/service-wifi.jar:/apex/com.samsung.android.lifeguard/javalib/service-lifeguard.jar
HOME=/
ANDROID_TZDATA_ROOT=/apex/com.android.tzdata
ANDROID_ROOT=/system
TERM=xterm-256color
SHELL=/bin/sh
ANDROID_BOOTLOGO=1
ANDROID_ASSETS=/system/app
ANDROID_SOCKET_adbd=21
HOSTNAME=a14x
DOWNLOAD_CACHE=/data/cache
SECONDARY_STORAGE=/storage/sdcard:/storage/usb1:/storage/usb2
ANDROID_STORAGE=/storage
USER=shell
TMPDIR=/data/local/tmp
PATH=/product/bin:/apex/com.android.runtime/bin:/apex/com.android.art/bin:/system_ext/bin:/system/bin:/system/xbin:/odm/bin:/vendor/bin:/vendor/xbin
SYSTEMSERVERCLASSPATH=/system/framework/com.android.location.provider.jar:/system/framework/knoxanalyticssdk.jar:/system/framework/mcfsdk.jar:/system/framework/uibc_java.jar:/system/framework/services.jar:/system/framework/semwifi-service.jar:/system/framework/ssrm.jar:/apex/com.android.adservices/javalib/service-adservices.jar:/apex/com.android.adservices/javalib/service-sdksandbox.jar:/apex/com.android.appsearch/javalib/service-appsearch.jar:/apex/com.android.art/javalib/service-art.jar:/apex/com.android.configinfrastructure/javalib/service-configinfrastructure.jar:/apex/com.android.healthfitness/javalib/service-healthfitness.jar:/apex/com.android.media/javalib/service-media-s.jar:/apex/com.android.ondevicepersonalization/javalib/service-ondevicepersonalization.jar:/apex/com.android.permission/javalib/service-permission.jar:/apex/com.android.rkpd/javalib/service-rkp.jar:/apex/com.samsung.android.shell/javalib/service-samsung-shell.jar
ASEC_MOUNTPOINT=/mnt/asec
ANDROID_I18N_ROOT=/apex/com.android.i18n
EXTERNAL_STORAGE=/sdcard
```

**Aprende más**

* [Shell (informática) \- Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Shell_\(inform%C3%A1tica\))  
* [Can I update the adb shell's environment variables? \- Android Enthusiasts Stack Exchange](https://android.stackexchange.com/questions/53389/can-i-update-the-adb-shells-environment-variables/64926#64926)   
* [Update mksh to latest version \- Android Enthusiasts Stack Exchange](https://android.stackexchange.com/questions/217617/update-mksh-to-latest-version/217627#217627) 

## Registros y eventos del sistema 

### logcat.txt y logcat\_old.txt 

La información de estos archivos se genera mediante el módulo [logcat.go](https://github.com/mvt-project/androidqf/blob/main/modules/logcat.go) .

**Información contenida**

Estos archivos se encuentran en texto plano con extensión .*txt* y contienen la salida de los comandos `adb shell logcat -d -b all` y `adb shell logcat -L -b all` respectivamente, los cuales muestran el registro de mensajes del sistema. Algunos ejemplos de la información contenida son:

* Mensajes de error y advertencia (FATAL EXCEPTION).  
* Mensajes de aplicaciones, procesos y servicios del sistema operativos.  
* Logs de depuración y eventos informativos.

El archivo contienen la  siguiente estructura:

* Inicio del registro (contiene divisiones de registros).  
* Marca de tiempo (timestamp).  
* Identificador del proceso y del hilo (PID) y (TID).  
- Nivel de prioridad:
    - E: Error 
    - W: Advertencia
    - I: Información
    - D: Depuración
    - F: Fatal
    - V: Verbose
* Etiqueta que indica el componente o proceso del sistema.  
* Descripción y detalles de los mensajes o de los errores.

**¿Por qué es importante?**

Esta información puede ser utilizada para analizar el comportamiento y ejecución de eventos en el sistema y de las aplicaciones del dispositivo para identificar anomalías o patrones que puedan indicar presencia de malware. En términos forenses son de los archivos más relevantes por su contenido.

**Ejemplo del contenido del archivo**

```
--------- beginning of crash  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: FATAL EXCEPTION: main  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: Process: example.android.app, PID: 12345  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: java.lang.RuntimeException: Unable to instantiate receiver example.android.app.MyBroadCastReceiver  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: at android.app.ActivityThread.handleReceiver(ActivityThread.java:4861)  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: at android.os.Handler.dispatchMessage(Handler.java:106)  
2025-01-01 00:00:00.000 30144 30860 I ActivityManager: Process example.android.app has died.  
```

**Aprende más**

* [Herramienta de linea de comandos Logcat](https://developer.android.com/tools/logcat?hl=es-419)

### dumpsys.txt 

La información de este archivo se genera mediante el módulo [dumpsys.go](https://github.com/mvt-project/androidqf/blob/main/modules/dumpsys.go) .

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando `adb shell dumpsys` el cual muestra información detallada sobre los servi`cios en ejecución, incluyendo procesos y aplicaciones.

El archivo está dividido en secciones específicas para cada servicio siguiendo un orden:

* Lista de servicios activos  
* Detalles de cada servicios  
* Logs detalladas 

Para conocer el listado de servicios que se pueden encontrar en un *dumpsys* de un dispositivo se puede ejecutar el comando `adb shell service list`

**¿Por qué es importante?**

El archivo brinda una perspectiva completa del estado del sistema en el dispositivo, clave para poder conocer la actividad realizada por servicios, aplicaciones y procesos en el dispositivo. En términos forenses es uno de los archivos más relevantes por su contenido.

**Ejemplo del contenido del archivo**

```
Currently running services:
  accessibility
  account
  adb
  alarm
  android.frameworks.cameraservice.service.ICameraService/default
  android.hardware.biometrics.face.IFace/default
  android.hardware.vibrator.IVibratorManager/default
  android.os.UpdateEngineService
  android.security.authorization
  anrmanager
  anti_root_dialog
  app_binding
  appops
  audio
  auth
  battery
  batteryproperties
  batterystats
  bluetooth_manager
  bugreport
  cpuinfo
  critical.log
  dataloader_manager
  dbinfo
  input
  logcat
  meminfo
  netstats
  ostats_pullerd
  ostats_tpd
  ostatsd
  package
  permission
  phone
  power
  processinfo
  procstats
  settings
  stats
  statsbootstrap
  usb
  wifi
  window

-------------------------------------------------------------------------------
DUMP OF SERVICE AtlasService:
--------- 0.001s was the duration of dumpsys AtlasService, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE DockObserver:
Current Dock Observer Service state:
  reported state: 0
  previous state: 0
  actual state: 0
--------- 0.007s was the duration of dumpsys DockObserver, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE ISubsysRadio:
--------- 0.005s was the duration of dumpsys ISubsysRadio, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE MMListService:
--------- 0.001s was the duration of dumpsys MMListService, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE OPLUSExService:
--------- 0.001s was the duration of dumpsys OPLUSExService, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE OplusLocationManager:
--------- 0.001s was the duration of dumpsys OplusLocationManager, ending at: 2025-05-08 18:>
-------------------------------------------------------------------------------
DUMP OF SERVICE appops:
Current AppOps Service state:
  Settings:
	top_state_settle_time=+5s0ms
	fg_service_state_settle_time=+5s0ms
	bg_state_settle_time=+1s0ms

  Op mode watchers:
	Op COARSE_LOCATION:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
  	#1: ModeCallback{21558a8 watchinguid=-1 flags=0x1 op=MONITOR_LOCATION from uid=u0a124 pid=3315}
  	#2: ModeCallback{c7241f6 watchinguid=-1 flags=0x1 op=COARSE_LOCATION from uid=1000 pid=1807}
  	#3: ModeCallback{f993e3b watchinguid=-1 flags=0x1 op=FINE_LOCATION from uid=u0a124 pid=3315}
	Op FINE_LOCATION:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
  	#1: ModeCallback{e5bfc6d watchinguid=-1 flags=0x1 op=FINE_LOCATION from uid=1000 pid=1807}
  	#2: ModeCallback{f993e3b watchinguid=-1 flags=0x1 op=FINE_LOCATION from uid=u0a124 pid=3315}
	Op READ_CONTACTS:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op WRIT E_CONTACTS:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op READ_CALL_LOG:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op WRITE_CALL_LOG:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op READ_CALENDAR:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op WRITE_CALENDAR:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op POST_NOTIFICATION:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}


```

**Aprende más**

* [dumpsys en Android](https://developer.android.com/tools/dumpsys?hl=es-419)

### bugreport.zip 

La información de este archivo se genera mediante el módulo [bugreport.go](https://github.com/mvt-project/androidqf/blob/main/modules/bugreport.go) .

**Información contenida**

Este es un archivo comprimido en formato *zip* y contiene la salida del comando `adb shell bugreport` el cual es un informe completo sobre el estado actual del dispositivo que incluye datos del sistema, logs y configuraciones.

Este archivo comprimido puede ser analizado por la MVT mediante el comando `mvt-android check-bugreport bugreport.zip` 

Los archivos y carpetas contenidas en el comprimido incluye los siguiente:

* **dumpstate-yyyy-mm-dd-hh-mm-ss.txt:** Archivo que proporciona un resumen de las características principales del dispositivo móvil y el estado actual del sistema.  
* **dumpstate_board.txt:** Archivo que proporciona logs de inicio del sistema con datos detallados sobre los eventos y servicios que se ejecutan durante el arranque del dispositivo.  
* **dumpstate_log.txt:** Archivo que presenta los logs del proceso de generación de informe. Contiene posibles errores o advertencias durante la recopilación de datos.  
* **main_entry.txt:** Este archivo sirve como un índice del contenido de los componentes recopilados en el bugreport.  
* **version.txt:** Muestra la versión del formato de generación de los registros del bugreport.  
* `fs/cache/recovery/`  
    * **last_data_partition_info:** Esta información proporciona las características del almacenamiento del dispositivo, el tamaño total, tamaño de sector y el número de bloques presentes. Así mismo, informa la capacidad de almacenamiento utilizada y la disponibilidad.  
    * **last_dataresizing:** Esta información registra el inicio y configuración de varios sensores del dispositivo. También muestra mensajes de instancias creadas para sensores específicos (como auto rotation, smart alert, etc).  
    * **last_postrecovery:** Esta información describe actividades relacionadas con la comunicación entre componentes de software seguros.  
* `fs/data/anr/`  
    * **arn_yyyy-mm-dd-hh-mm-ss:** Proporciona un diagnóstico detallado de aplicaciones que no responden. ARN se origina de *App Not Responding*.
* `fs/data/log/bt/`  
    * **btsnooz_hci.log:** Registro generado por dispositivos Android que contiene información sobre la actividad de la interfaz HCI (*Host Controller Interface*) de Bluetooth.  
    * **btsnooz_hci.log.last:** Contiene un registro más detallado y extenso del historial de eventos de HCI Bluetooth.  
* `fs/misc/recovery`  
    * **ro.buil.fingerprint:** El archivo contiene el identificador único de la versión de software que está ejecutando el dispositivo.  
    * **ro.build.fingerprint.1:** El archivo contiene una variante del identificador de compilación en el dispositivo.  
* `fs/data/tombstones/`  
    * **tombstone_xx:** Estos archivos son registros de fallos (*crash dumps*) que el sistema genera automáticamente cuando un proceso de usuario o del sistema se bloquea inesperadamente.  
* `fs/proc/`  
    * **mountinfo:** Este archivo proporciona información detallada sobre los puntos de montaje en un sistema operativo basado en Linux. Básicamente, permite entender cómo están configurados los sistemas de archivos y las particiones montadas.  


**¿Por qué es importante?**

Este comprimido es una fuente de información con mucho valor para el análisis forense para poder identificar el estado general del dispositivo y dar seguimiento a irregularidades o fallas de software o hardware que se presenten en contextos de explotación de vulnerabilidades.

**Aprende más**

* [Cómo capturar y leer informes de errores](https://developer.android.com/studio/debug/bug-report?hl=es-419)

### logs/

La información de esta carpeta se genera mediante el módulo [logs.go](https://github.com/mvt-project/androidqf/blob/main/modules/logs.go). 

**Información contenida**  
Contiene archivos de registro recolectados directamente desde el dispositivo, utilizando el comando `adb pull` en varias carpetas. 

El módulo accede a rutas específicas del sistema para extraer archivos que documentan el comportamiento, errores y eventos del sistema operativo, las cuales son:

* /data/anr/  
* /data/log/  
* /sdcard/log/

Los archivos y carpetas contenidas en este directorio son los siguiente:

* `anr/anr_yyyy-mm-dd-hh-mm-ss`  
    * **anr_yyyy-mm-dd-hh-mm-ss**: Archivo que proporciona un diagnóstico detallado del estado del sistema y de la actividad de un proceso específico.  

* `log/acore/0_dump_all.zip`  
    * **0_dump_all.zip**: Archivo que contiene un volcado del estado del sistema asociado al proceso acore.  

* `log/batterystats/newbatterystats240905095247`  
    * **newbatterystats240905095247**: Archivo que contiene métricas sobre el uso energético del dispositivo.  

* `log/dropbox.txt`  
    * **dropbox.txt**: Archivo que contiene registros de eventos del sistema gestionados por DropBoxManager.  

* `log/dumpstate_debug_history.lst`  
    * **dumpstate_debug_history.lst**: Archivo que contiene el historial de ejecuciones del proceso de recolección de logs del sistema.  

* `log/dumpstate_lastkmsg_20240423_152746_0_MP.log.gz`  
    * **dumpstate_lastkmsg_20240423_152746_0_MP.log.gz**: Archivo que contiene el último mensaje del kernel tras un reinicio inesperado.  

* `log/dumpstate_latest_lastkmsg.log.gz`  
    * **dumpstate_latest_lastkmsg.log.gz**: Archivo que contiene el log persistente más reciente del kernel después de un reinicio.  

* `log/dumpstate-stats.txt`  
    * **dumpstate-stats.txt**: Archivo que contiene estadísticas generadas durante la recolección del estado del sistema.  

* `log/dumpstate_sys_error.zip`  
    * **dumpstate_sys_error.zip**: Archivo comprimido que contiene información sobre errores críticos del sistema.  

* `log/lom_log.txt`  
    * **lom_log.txt**: Archivo que contiene registros relacionados con almacenamiento o monitoreo del sistema.  

* `log/pm_debug_info.txt`  
    * **pm_debug_info.txt**: Archivo que contiene información de depuración del gestor de paquetes del sistema.  

* `log/power_off_reset_reason.txt`  
    * **power_off_reset_reason.txt**: Archivo que indica la causa del último apagado o reinicio del dispositivo.  

* `log/prev_dump.log`  
    * **prev_dump.log**: Archivo que contiene una captura previa del estado del sistema antes de un evento crítico.  

* `log/radio_PRECONFG_SET.log`  
    * **radio_PRECONFG_SET.log**: Archivo que documenta la configuración inicial del módulo de radio del dispositivo.  
 
* `log/shutdown_profile.1.txt`  
    * **shutdown_profile.1.txt**: Archivo que contiene el perfil de apagado registrado por el sistema.  

* `log/shutdown_profile_latest.txt`  
    * **shutdown_profile_latest.txt**: Archivo que contiene el perfil del apagado más reciente del sistema.  

* `log/err/`  
    * **mobiledata_dns.dat**: Archivo que contiene errores relacionados con resolución DNS en redes móviles.  
    * **mobiledata_tp2.dat**: Archivo que contiene errores en la transferencia de paquetes móviles.  
    * **mobiledata_tp.dat**: Archivo que contiene errores en la transferencia de paquetes móviles.  

* `log/ewlogd/ewlog0_20240920_144426188369.log`  
    * **ewlog0_20240920_144426188369.log**: Archivo que contiene registros de eventos del sistema generados por el servicio ewlogd.  

* `log/imscr/imscr.log.0`  
    * **imscr.log.0**: Archivo que contiene registros del componente IMS para servicios de comunicación.  

* `log/omc/`  
    * **cidmanager.log**: Archivo que contiene información del gestor de códigos de operador (CID).  
    * **csc_update_log.txt**: Archivo que contiene el registro de actualizaciones del paquete de personalización CSC.  
    * **home_fota_update_log.txt**: Archivo que contiene registros de actualizaciones FOTA en red doméstica.  
    * **prev_csc_log.txt**: Archivo que contiene un historial previo de configuración del operador.  

* `log/search/0_com.samsung.android.scs_index_encrypted.tar.gz`  
    * **0_com.samsung.android.scs_index_encrypted.tar.gz**: Archivo comprimido cifrado que contiene datos del índice de búsqueda del sistema.  

* `log/sfslog/sfslog.0.gz`  
    * **sfslog.0.gz**: Archivo comprimido que contiene registros del sistema de archivos seguro (Secure File System).  

* `log/smartswitch/1726696227738SmartSwitchSimpleLog.log`  
    * **1726696227738SmartSwitchSimpleLog.log**: Archivo que contiene registros del proceso de transferencia de datos mediante Smart Switch.  

* `log/update_engine_log/update_engine.20240603-222843`  
    * **update_engine.20240603-222843**: Archivo que contiene registros del motor de actualización de software del sistema.  

* `log/wfd/wfdDumpSource.log`  
    * **wfdDumpSource.log**: Archivo que contiene actividad registrada del componente Wifi direct (WFD).  

* `log/wifi/`  

* `system/proc/`  
    * **kmsg**: Archivo que contiene el log actual del kernel con actividad del sistema a bajo nivel.  
    * **last_kmsg**: Archivo que contiene el último log persistente del kernel tras un reinicio.  

* `sys/fs/pstore/`

## Procesos y aplicaciones 

### packages.json

La información de esta carpeta se genera mediante el módulo [packages.go](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/adb/packages.py).  
**Información contenida**

Este archivo se encuentra en formato *json* y contiene la salida del comando `adb shell pm list packages` , el cual muestra un listado de aplicaciones instaladas en el dispositivo.

El archivo contiene:

* name: Nombre del paquete de la aplicación.  
* files: Ruta del archivo APK correspondiente con sus respectivos hashes e información del certificado.  
* installer: Desde cual aplicación se instalo.  
* uid: El PID asociado en ejecución.  
* disabled: Indica si la aplicación esta deshabilitada.  
* system: Indica si el paquete pertenece al sistema.  
* third\_party: Indica si es una aplicación de terceros.

**¿Por qué es importante?**

El contenido de este archivo incluye información que permite identificar aplicaciones instaladas y cuál es su estado en el dispositivo. Esto ayuda a los analistas a evaluar si existen aplicaciones de riesgo o maliciosas, que permisos tienen y cuales pueden comprometer la seguridad.

**Estructura del archivo**

```
[
	{
    	"name": "com.whatsapp",
    	"files": [
        	{
            	"path": "/data/app/~~bqy7OQa_ZY_wDTFdG5YZRA==/com.whatsapp-3CExO11mXQz7SoP-3>
            	"local_name": "",
            	"md5": "a6014f075183b8872d115e04f546a19a",
            	"sha1": "7c52f9781c44c4902aecb4fc8a13584998e02376",
            	"sha256": "26721b2669943d57f9de57614a11077b7c3f3036396d48c3e54cbf0effd2268e",
            	"sha512": "21bea0ff94a748826041a1a8b3b9189090340086469ec62d31cf0d263c743fc2e>
            	"error": "",
            	"verified_certificate": true,
            	"certificate": {
                	"Md5": "556c6019249bbc0cab70495178d3a9d1",
                	"Sha1": "38a0f7d505fe18fec64fbf343ecaaaf310dbd799",
                	"Sha256": "3987d043d10aefaf5a8710b3671418fe57e0e19b653c9df82558feb5ffce5>
                	"ValidFrom": "2010-06-25T23:07:16Z",
                	"ValidTo": "2044-02-15T23:07:16Z",
                	"Issuer": "C=US, ST=California, L=Santa Clara, O=WhatsApp Inc., OU=Engin>
                	"Subject": "C=US, ST=California, L=Santa Clara, O=WhatsApp Inc., OU=Engi>
                	"SignatureAlgorithm": "DSA-SHA1",
                	"SerialNumber": 1277507236
            	},
            	"certificate_error": "",
            	"trusted_certificate": true
        	}
    	],
    	"installer": "com.facebook.system",
    	"uid": 10267,
    	"disabled": false,
    	"system": false,
    	"third_party": true
	}
]
```

### apks/ 

La información de esta carpeta se genera mediante el módulo [packages.go](https://github.com/mvt-project/androidqf/blob/main/modules/packages.go).

**Información contenida**

Este directorio almacena los archivos APK (paquetes de aplicaciones Android) extraídos del dispositivo. Estos son los archivos de instalación de las aplicaciones que estaban presentes en el sistema en el momento del análisis.

**¿Por qué es importante?**

El análisis de los APKs permite examinar las aplicaciones instaladas en el dispositivo, identificar posibles muestras de malware o aplicaciones maliciosas, así como validar las versiones instaladas y sus firmas.

### processes.txt  

La información de este archivo se genera mediante el módulo [processes.go](https://github.com/mvt-project/androidqf/blob/main/modules/processes.go). 

**Información contenida**

Este archivo se encuentra en formato *json* y contiene la salida del comando `adb shell ps -A` , el cual muestra información detallada sobre los procesos que se encuentran en ejecución. 

Este archivo presenta la información en una forma estructurada teniendo como orden identificadores, detalles de la ejecución, consumo de recursos y estado del proceso.

**¿Por qué es importante?**

Este archivo permite identificar procesos que son ejecutados de manera inusual o que son ejecutados por usuarios no autorizados como resultado de una escalada de privilegios. Así mismo, podemos asegurar que los procesos y sus jerarquías coinciden con las configuraciones establecidas o normales.

**Ejemplo del contenido del archivo**

```
[
	{
    	"pid": 1,
    	"uid": 0,
    	"ppid": 0,
    	"pgroup": 0,
    	"psid": 0,
    	"filename": "(init)",
    	"priority": 0,
    	"state": "S",
    	"user_time": 0,
    	"kernel_time": 0,
    	"path": "/system/bin/init",
    	"context": "u:r:init:s0",
    	"previous_context": "u:r:kernel:s0",
    	"command_line": ["/system/bin/init", "second_stage"],
    	"env": null,
    	"cwd": "/"
	},
	{
    	"pid": 2,
    	"uid": 0,
    	"ppid": 0,
    	"pgroup": 0,
    	"psid": 0,
    	"filename": "(kthreadd)",
    	"priority": 0,
    	"state": "S",
    	"user_time": 0,
    	"kernel_time": 0,
    	"path": "",
    	"context": "u:r:kernel:s0",
    	"previous_context": "u:r:kernel:s0",
    	"command_line": null,
    	"env": null,
    	"cwd": ""
	},
	{
    	"pid": 20430,
    	"uid": 0,
    	"ppid": 0,
    	"pgroup": 0,
    	"psid": 0,
    	"filename": "(com.whatsapp)",
    	"priority": 0,
    	"state": "",
    	"user_time": 0,
    	"kernel_time": 0,
    	"path": "",
    	"context": "u:r:untrusted_app:s0:c11,c257,c512,c768",
    	"previous_context": "u:r:init:s0",
    	"command_line": [
        	"com.whatsapp"
    	],
    	"env": null,
    	"cwd": ""
	},
]
```

**Aprende más**

* [Descripción general de los procesos y subprocesos](https://developer.android.com/guide/components/processes-and-threads?hl=es-419)

### services.txt 

La información de este archivo se genera mediante el módulo [services.go](https://github.com/mvt-project/androidqf/blob/main/modules/services.go)

**Información contenida**

Este archivo se encuentra en formato *txt* y contiene la salida del comando `adb shell service list` el cual muestra información detallada sobre los servicios en ejecución.

La estructura del archivo es el nombre del servicio y el proceso o paquete que está en ejecución para ese servicio.

**¿Por qué es importante?**

Este archivo permite identificar los servicios en ejecución o en sentido contrario identificar si un servicio no se encontraba en ejecución. Esto es útil para identificar que todos los servicios necesarios estén en ejecución para mantener la integridad de la seguridad del dispositivo.

**Ejemplo del contenido del archivo**

```
Found 368 services:
0	AtlasService: [android.atlas.service]
1	DockObserver: []
9	accessibility: [android.view.accessibility.IAccessibilityManager]
10	account: [android.accounts.IAccountManager]
11	activity: [android.app.IActivityManager]
13	adb: [android.debug.IAdbManager]
16	alarm: [android.app.IAlarmManager]
26	android.hardware.power.IPower/default: [android.hardware.power.IPower]
27	android.hardware.power.stats.IPowerStats/default: []
43	anrmanager: [android.app.IAnrManager]
44	anti_root_dialog: [com.oplus.exsystemservice.antirootdialog.IAntiRootDialog]
50	appops: [com.android.internal.app.IAppOpsService]
56	audio: [android.media.IAudioService]
61	battery: []
63	batterystats: [com.android.internal.app.IBatteryStats]
68	bugreport: [android.os.IDumpstate]
70	cacheinfo: []
72	clipboard: [android.content.IClipboard]
78	connectivity: [android.net.IConnectivityManager]
84	cpuinfo: []
85	critical.log: []
89	dbinfo: []
130	input: [android.hardware.input.IInputManager]
133	installd: []
146	location: [android.location.ILocationManager]
149	logcat: [android.os.logcat.ILogcatManagerService]
169	meminfo: []
181	netstats: [android.net.INetworkStatsService]
191	notification: [android.app.INotificationManager]
234	package: [android.content.pm.IPackageManager]
238	permission: [android.os.IPermissionController]
240	permissionmgr: [android.permission.IPermissionManager
242	phone: [com.android.internal.telephony.ITelephony]
247	power: [android.os.IPowerManager]
248	power_hal_mgr_service: [com.mediatek.powerhalmgr.IPowerHalMgr]
249	power_monitor: [com.oplus.os.IOplusPowerMonitor]
250	powerstats: []
252	processinfo: [android.os.IProcessInfoService]
253	procstats: [com.android.internal.app.procstats.IProcessStats]
255	recovery: [android.os.IRecoverySystem]
273	sensorservice: [android.gui.SensorServer]
274	serial: [android.hardware.ISerialManager]
276	settings: []
298	system_server_dumper: []
299	system_update: [android.os.ISystemUpdateManager]
301	telecom: [com.android.internal.telecom.ITelecomService]
302	telephony.registry: [com.android.internal.telephony.ITelephonyRegistry]
314	tracing.proxy: [android.tracing.ITracingServiceProxy]
322	usb: [android.hardware.usb.IUsbManager]
323	user: [android.os.IUserManager]
354	virtualdevice: [android.companion.virtual.IVirtualDeviceManager]
355	vodata: [com.mediatek.ims.internal.IVoDataService]
357	vold: []
358	vpn_management: [android.net.IVpnManager]
363	wifi: [android.net.wifi.IWifiManager]
367	window: [android.view.IWindowManager]
```

**Aprende más**

* [¿Cómo funcionan los servicios en android?](https://developer.android.com/develop/background-work/services?hl=es-419)

### root\_binaries.json 

La información de este archivo se genera mediante el módulo [root\_binaries.go](https://github.com/mvt-project/androidqf/blob/main/modules/root_binaries.go). 

Este módulo hace una búsqueda específica de proceso de rooting.

**Información contenida**

Este archivo se encuentra en formato *json* y contiene la salida del comando `adb shell which -a` aplicado a una lista de binarios para saber si están presentes en el sistema.

Los binarios a los que se aplica son utilizados para obtener acceso de root o elevar privilegios en el dispositivo.

La lista de binarios y archivos es:

* su  
* busybox  
* supersu  
* Superuser.apk  
* KingoUser.apk  
* SuperSu.apk  
* magisk  
* magiskhide  
* magiskinit  
* magiskpolicy

Si ninguno de estos archivos está presente en el dispositivo entonces el contenido del archivo será vacío.

**¿Por qué es importante?**

Este archivo detecta herramientas de rooting, lo cual puede representar un indicativo  de accesos no autorizados y escalada de privilegios que pueda exponer alguna vulnerabilidad.  Así mismo, permite al analista identificar binarios sospechosos que podrían haberse instalado sin el conocimiento del usuario y ayuda a determinar si el dispositivo ha sido manipulado.

**Ejemplo del contenido del archivo**

El archivo vacío tiene la siguiente estructura:

```
[]
```

Cuando el módulo identifica binarios relacionados con el rooting en las rutas estándar del sistema en el dispositivo, contendrá una lista de estas rutas a los binarios detectados:

```
[
	"/system/xbin/su",
	"/system/bin/su",
	"/data/local/xbin/su",
	"/data/local/bin/busybox",
	"/sbin/su",
	"/su/bin/magisk",
	"/system/bin/.ext/.su",
	"/data/local/tmp/Superuser.apk",
	"/data/local/tmp/magiskhide"
]


```

## Información de archivos en el dispositivo 

### backup.ab 

La información de este archivo se genera mediante el módulo [backup.go](https://github.com/mvt-project/androidqf/blob/main/modules/backup.go).

Este módulo está diseñado específicamente para realizar copias de seguridad de datos que están almacenados en dispositivos móviles con Android.

**Información contenida**

Este archivo se encuentra en formato binario y contiene datos relacionados con la copia de seguridad de aplicaciones y configuraciones del dispositivo. Los datos binarios presentes en este archivo se encuentran comprimidos e incluyen información confidencial del dispositivo.

Dependiendo de la opción seleccionada en androidqf el contenido del archivo puede ser solamente los SMS o puede ser una copia de datos de aquellas aplicaciones que tienen declarado en su manifiesto la posibilidad de realizar copias.

Este archivo comprimido puede ser analizado por la MVT mediante el comando `mvt-android check-backup backup.ab`

**¿Por qué es importante?**

En el caso forense este respaldo permite analizar los SMS en búsqueda de enlaces sospechosos o maliciosos.

**Ejemplo del contenido del archivo**

```
(Binary data containing app backups and settings)
414e 4452 4f49 4420 4241 434b 5550 0a35
0a30 0a6e 6f6e 650a 6170 7073 2f63 6f6d
2e61 6e64 726f 6964 2e63 7473 2e63 7473
7368 696d 2f5f 6d61 6e69 6665 7374 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 3030 3036
3030 2000 3031 3735 3000 0000 3031 3735
3000 0000 3030 3030 3030 3034 3537 3600
3000 0000 0000 0000 0000 0000 3031 3430
3134 0020 3000 0000 0000 0000 0000 0000
```

**Aprende más**

* [Extracción de archivos de respaldo | Android Backup Extractor](https://github.com/nelenkov/android-backup-extractor)  
* [Análisis de archivos de copias de seguridad en android](https://digitalforensicforest.com/2016/01/28/android-backup-file-ab-analysis/)  
* [Check an Android Backup (SMS messages) \- Mobile Verification Toolkit](https://docs.mvt.re/en/latest/android/backup/) 

### files.json 

La información de este archivo se genera mediante el módulo [files.go](https://github.com/mvt-project/androidqf/blob/main/modules/files.go)

**Información contenida**

Este archivo se encuentra en formato *json* y contiene el resultado de la busqueda de archivos mediante el comando *find.*

El comando completo de *find* es `adb shell find '/' -maxdepth 1 -printf '%T@ %m %s %u %g %p\n' 2\> /dev/null` y se aplica a las siguientes carpetas:

* /sdcard/  
* /system/  
* /system\_ext/  
* /vendor/  
* /cust/  
* /product/  
* /apex/  
* /data/local/tmp/  
* /data/media/0/  
* /data/misc/radio/  
* /data/vendor/secradio/  
* /data/log/  
* /tmp/  
* /data/data/

Cada archivo incluye metadatos como: la ruta completa del archivo, tamaño, marca de tiempo (indica última modificación del archivo y último acceso al archivo), permisos del archivo, identificador del propietario, mensajes de error y hashes sha1, sha256, sha512, md5 si es que están pre-calculados.

**¿Por qué es importante?**

Este archivo tiene relevancia para identificar archivos de interés en una investigación forense, incluyendo potenciales archivos utilizados por atacantes para comprometer un dispositivo y hacer los análisis oportunos que permitan dar seguimiento a actividad maliciosa. 

**Ejemplo del contenido del archivo**

```
{
"path": "/sdcard/Android/.Trash/com.sec.android.app.myfiles/.nomedia",
    	"size": 62,
    	"mode": "-rw-rw----",
    	"user_id": 10276,
    	"user_name": "",
    	"group_id": 1023,
    	"group_name": "",
    	"changed_time": 1722868692,
    	"modified_time": 1722868692,
    	"access_time": 1714937715,
    	"error": "",
    	"context": "u:object_r:fuse:s0",
    	"sha1": "",
    	"sha256": "",
    	"sha512": "",
    	"md5": ""
}
```

## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentar que se muestra a continuación** para dejarnos tus ideas o apreciaciones. Por favor asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/). La función de comentarios enlaza directamente a la sección de [_Discussions_ de Github](https://github.com/Socialtic/forensics/discussions), donde también **puedes participar en las discusiones de forma directa**, si lo prefieres.   



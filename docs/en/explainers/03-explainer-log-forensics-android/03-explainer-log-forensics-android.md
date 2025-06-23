---
title: Introduction to log-based forensics on Android devices
summary: Document with introduction to log-based forensics on Android devices
keywords: forense, logs, android, androidqf
authors: Daniel Bedoya Arroyo
lang: en
tags: [explainer, intro]
last_updated: 2025-06-23
some_url:
---


# Explainer: Introduction to log-based forensics on Android devices

## Introduction

This document is part of a **technical documentation repository** created to establish a baseline of proven, flexible and accessible knowledge to **boost consensual forensic analysis in support of civil society across the globe**. To organize the contents, we use the [technical documentation framework Diátaxis](https://diataxis.fr/). 

This particular resource fits within [the explanation category in Diátaxis](https://diataxis.fr/explanation/), and presents an **introduction to log-based forensics for Android devices**, including a definition of log-based forensics, a comparison with other types of forensic analysis and some use cases. This is an introductory material that does not require previous knowledge, and is complemented with [how-to guides](http://../../../how-tos/) and  [tutorials](http://../../../tutorials/) for forensic acquisition. 

We appreciate revisions and suggestions from … to improve this content. Errors and omissions remain the responsibility of the authors. 

## ¿What is log-based forensic analysis and why is it useful?

Log-based forensic analysis refers to a type of investigation that **uses different records of the system, including bugreports, memory traces, configuration files, process lists, among others, to identify possible traces and indicators of [digital attacks](https://socialtic.org/wp-content/uploads/2020/11/Tipologia_AtaquesDigitales-2020-1.pdf)**. 

To conduct a log-based research, analysts normally walk through the different [phases of a forensic investigation](https://forensics.socialtic.org/en/explainers/01-explainer-introduction-digital-forensics/01-explainer-introduction-digital-forensics/#what-are-the-usual-stages-of-a-forensic-investigation), starting with the **identification and collection** of potential evidence. As it is the case with any type of investigation, prior to collecting evidence it is important to [discuss and document an informed consent](https://forensics.socialtic.org/en/how-tos/01-how-to-obtain-informed-consent/01-how-to-obtain-informed-consent/), while also making conscious efforts to [minimize personal data](https://little-flying-robots.ghost.io/a-brief-ode-to-data-minimization/) alongside information protection and verification practices. We have published a [draft consent letter](https://forensics.socialtic.org/en/how-tos/01-how-to-obtain-informed-consent/template-letter-of-consent-for-forensic-analysis-pdf.pdf) that can be adjusted as needed.  

In the case of mobile devices, regarding investigations focusing on advanced threats, **most of the analysis conducted so far by civil society** (by organizations like Citizen Lab or Amnesty tech) **uses log-based forensics** to arrive at conclusions and extract findings. The possibility of collecting targeted information (for example, a bugreport), **including in remote support situations**, makes this a common and convenient method of analysis. 

Evidence collected is **usually analyzed after the fact**, normally in a forensic lab environment, ideally in accordance with best practices for [operational security](https://en.wikipedia.org/wiki/Operations_security) and [evidence preservation](https://forensics.socialtic.org/en/explainers/01-explainer-introduction-digital-forensics/01-explainer-introduction-digital-forensics/#chain-of-custody). Tools like [MVT](https://github.com/mvt-project/mvt) on AndroidQF can aid and simplify the acquisition and analysis of evidence. Generally speaking, when conducting a log-based forensic analysis, you are looking to find **coincidence with known [indicators of compromise (IOC)](https://www.cloudflare.com/es-es/learning/security/what-are-indicators-of-compromise/)** of previous attacks; or to **document anomalies that when compared with a baseline** depict suspicious behaviors that coincide with adversarial activity, and that have not been previously recorded or characterized. Due to this methodological approach, log-based forensic analysis can often result in **high-confidence findings**. 

It’s worth noting that **not having a match with known IOCs is not necessarily a confirmation of a “clean device”.** It might be possible that threat actors have taken measures to prevent forensic analysis, or that the attack is exploiting a zero-day vulnerability that has not been previously detected. One of the advantages of log-based analysis is that **you can store records**, in case new information is discovered at a later date, potentially resulting in useful additional intelligence. If you are planning to store records for future analysis, it is important to ensure you have the [necessary consent](https://forensics.socialtic.org/en/how-tos/01-how-to-obtain-informed-consent/01-how-to-obtain-informed-consent/#documenting-informed-consent), and that you have taken measures to eliminate any personal information that is not relevant from a forensic standpoint.  

The publication “[Detection and analysis of spyware: methodologies, limitations and opportunities](https://irl.works/blog/2025/03/19/spyware-detection-analysis.html)” **summarizes and presents different methodologies commonly used by civil society,** specifically for the detection of spyware. In addition to log-based forensics (covered as forensic analysis on the report), the text also mentions investigations based on **monitoring signals**, specially from agents running on systems and looking after suspicious patterns, processes or other signals; and also analysis and investigations that rely on network **traffic monitoring** to identify traces of suspicious activity in the network communications.   

In summary, some of the **advantages of log-based forensics** include: 

* Facilitates **remote attention and triage**  
* Collects **less private information**, when compared to full disk copies, and specially when information is minimized.  
* It can result in **high confidence results**, particularly if you can match with known indicators of compromise.    
* It is useful to **make comparisons when you have a known baseline** to compare against.  
* It is possible to **continue evaluating forensic artifacts** against new indicators of compromise that are published at a later date.

And some of the **challenges of log-based** forensics are:

* Even when you only do targeted extraction of artifacts, it is possible that the **collected information contains thousands or tens of thousands lines**, which means that manual review and analysis requires time and experience with the filtering and scanning of information.   
* Some **logs and records may not be available from the user profile**, or might require additional permissions (like for example, route access on android)  
* Most log files work with [**circular buffers**](https://es.m.wikipedia.org/wiki/Buffer_circular) that are overweight as they are filled up, therefore the older information is constantly being overwritten   
* Although some tools can facilitate the process, in general for the extraction of records and logs it is recommended to have a **basic understanding of the operating system**.


## ¿How do you initiate a log based analysis on an android device? 

To perform a log-based forensic analysis, you need to go through the typical stages of a forensic investigation, **starting with the capture of key system records** from the device under investigation. Once the information is collected, you will need to use a combination of tools and manual analysis to identify potential traces of malicious activity. Understanding **how the system behaves in normal circumstances is helpful, as is having access to indicators of compromise**—such as those published by  [Amnesty International](https://github.com/mvt-project/mvt-indicators) or [Citizen Lab](https://github.com/citizenlab/malware-indicators). However, it's important to note that these **indicators may become outdated** as attackers change their infrastructure, technology, or attack vectors, so they should be updated or complemented with manual analysis.

To extract the key records from an android device, it is possible to use some **tools that facilitate the backing and extraction of logs**, like for example, Google’s bug report or ADB shell, as well as other tools developed by third parties like androidQF.

## Types of logs and tools for extraction

In the case of mobile devices running android, due to the diversity of manufacturers and their particular preferences, as well as the ecosystem of developers and the multiple components, there are many different and record logs. In general, a mix of the [following standards](https://source.android.com/docs/core/tests/debug/understanding-logging) is used:

* [RFC 5424 (protocolo syslog)](https://datatracker.ietf.org/doc/html/rfc5424): Used for **kernel and UNIX-style** system services logging.   
* [android.util.log](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/util/Log.java) :Used for **logging Android system and application** events.   
* [java.util.logging.level:](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html) used in **Java-based applications**, which includes many third-party apps.

All these standards have similar constructions, but defer in the number of levels of logging available. For example, in **syslog there are 8 levels**, ranging from debugging to emergency logs; while **android.util has only 5 levels**, ranging from verbose up to error.  

Although understanding exactly the login levels and the construction of each different type of flag is beyond the scope of this resource, it is **important to take this ecosystem fragmentation into account**, since it will continue to be reflected in other aspects of the process, including when navigating the graphical interface. 

This diversity of the android ecosystem means that it is impossible to create a definitive list of all of the different logs available on android, but we can certainly list some of the **most commonly used to in forensic investigations**, focusing especially in those that can be accessed without root privileges:

* **main log:** main log records general messages from the applications and the system.   
* **kernel panic:** kernel panic log refers to logs that are created when the operating system detects an error from which it cannot recover, like for example, a memory violation or an issue with a system call. In the majority of cases, Linux uses the function [‘ramoops’](https://www.kernel.org/doc/html/v4.19/admin-guide/ramoops.html) to write the logs before the system stops.   
* **Crash reports and tombstones:**  crash logs are usually recorded when an application or process stops unexpectedly. tombstones on the other hand, referred to more detailed reports of failures and native android applications.    
* **radio logs**: radio X usually has information about the activity that happens between the cellular towers and the cell phone including information about mobile data, voice calling, SMS, among others.    
* **Security logs**: refers to system configurations of [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) or logs that are within the security buffer. Some security logs or events might not be accessible for unprivileged users.  

There are different tools that can be used to extract and package logs, application lists, process data, and other system records in a straightforward way; including some native tools and some developed by third parties:

* [**dumpsys**](https://developer.android.com/tools/dumpsys): A native Android command-line tool available via the Android Debug Bridge (ADB) shell. It **extracts detailed information about system services** such as battery usage, Wi-Fi status, memory, and more.  
* **dumpstate**: A native tool used to **gather error logs from a device**. It is invoked as part of the bugreport process.  
* [**logcat**](https://developer.android.com/tools/logcat): Another command-line tool available through ADB, it can **read from different log buffers**, including **main, system services, events, and crash**; each storing different types of diagnostic data.  
* [**bugreport**](https://developer.android.com/studio/debug/bug-report): A tool available via the graphical interface or ADB shell, **it generates a zipped diagnostic report** that includes logs from logcat, dumpstate, and dumpsys. The resulting ZIP file contains a structured folder with data on errors, memory usage, system calls, network activity, device info, and more.  
* [**androidqf**](https://github.com/mvt-project/androidqf): A **collection of scripts and tools designed to automate the extraction and packaging of forensic artifacts from Android devices using ADB**. It was initially developed by Claudio Guarnieri and is now maintained by Amnesty International's Security Lab.   
* [**Perfetto**](https://perfetto.dev/docs/)**:** An open-source system tracing tool **designed for performance profiling in Android and Linux**. While not traditionally used in forensic analysis, it can help in identifying abnormal system behaviors when configured appropriately.

## Additional considerations for log-based forensics

Before starting a log-based forensic analysis, it’s important to take into account the following aspects:

* **Minimization and protection of sensitive information:** Unlike other digital [forensics methods](https://forensics.socialtic.org/en/explainers/01-explainer-introduction-digital-forensics/01-explainer-introduction-digital-forensics/#how-can-digital-forensics-be-applied-in-the-defense-of-human-rights), civil society-led investigations typically aim to collect specific and targeted information, avoiding the capture of unnecessary personal data. If logs [contain sensitive content](https://forensics.socialtic.org/en/how-tos/01-how-to-obtain-informed-consent/01-how-to-obtain-informed-consent/#what-sensitive-information-is-commonly-collected-during-a-forensic-investigation)—such as messages—it is highly recommended to use automated procedures to retain only relevant forensic data. These procedures should be well-documented and reproducible to **ensure the integrity of the information.**  
       
* **Informed consent**: Before collecting logs or other records from a device, it is essential to obtain informed consent. [This resource provides guidance for generating a consent form](https://forensics.socialtic.org/en/how-tos/01-how-to-obtain-informed-consent/01-how-to-obtain-informed-consent/) and establishing good practices with the person requesting the analysis.

* **Roles and phases of log-based forensics:** Log-based forensic analysis follows [several stages](https://forensics.socialtic.org/en/explainers/01-explainer-introduction-digital-forensics/01-explainer-introduction-digital-forensics/#what-are-the-usual-stages-of-a-forensic-investigation), starting with identifying and collecting key information. **These steps can usually be carried out using practical guides and tools, even by those without advanced forensic expertise**. However, triage and deeper analysis do require additional knowledge—both in using forensic tools and conducting manual reviews.  
     
* **Managing expectations**: When reviewing a device, **you may find no traces of known threats**. While this is a positive signal, it doesn’t definitively mean the device hasn’t been compromised. Even after thorough manual analysis, various factors may limit the effectiveness of log-based forensics. If there are strong suspicions of compromise (for example, a threat notification from a platform), it is advisable to consider combining log-based methods with other forensic techniques mentioned earlier.  
    
* **Peer review and collaborative work**: In any type of forensic investigation—including log-based analysis—it is important to verify findings with trusted peers who can independently replicate your methodology. Peer review is strongly recommended before publishing results, especially if you’re presenting a new method or disclosing a previously unknown vulnerability.

## Conclusión

**Log-based forensics** relies on key device records—such as process information, error reports, or system logs—to identify known indicators of compromise or to highlight anomalies by comparing findings against an established baseline.

**On Android devices**, due to the diversity of manufacturers and technologies involved in development, there are a wide variety of standards and tools to become familiar with—including syslog, dumpstate, and ADB. Additionally, tools like AndroidQF are especially helpful for gathering forensic information from Android systems.

A large share of published reports by civil society organizations have relied on log-based forensics to support and document their findings. This is in part due to its ability to support remote investigations, its limited collection of personal information, and its capacity to produce high-confidence results.

If you would like to contribute to the development, translation, or dissemination of this resource, please contact us at [**seguridad@socialtic.org**.](mailto:seguridad@socialtic.org)seguridad@socialtic.org.


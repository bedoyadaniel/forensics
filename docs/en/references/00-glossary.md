---
title: Glossary
summary: Glossary
keywords: glossary
authors: Daniel Bedoya Arroyo
lang: en
tags: [glossary, reference]
last_updated: 2025-08-05
some_url:
created: 2025-08-05
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---

# Glossary

This document is part of a **technical documentation repository** whose main objective is to establish a baseline of proven, flexible and accessible knowledge to **boost consensual forensic analysis in support of civil society across the globe**. To organize the contents, we use the [technical documentation framework Diátaxis](https://diataxis.fr/). 

This particular resource is a glossary of terms that includes **concepts, abbreviations, and other terminology** considered important for a comprehensive understanding of the material. 

## Terms

### ADB

ADB stands for *Android Debug Bridge*. It is a **command-line tool** that **enables direct communication via USB with an Android device**, allowing the execution of various actions and commands.

In the context of **digital forensics**, especially in [log-based investigations](../explainers/03-explainer-forense-logs-android/03-explainer-forense-logs-android.html) using tools like AndroidQF, **ADB allows direct communication with the device**. It is useful when there is **physical access to the device** and when retrieving information through **native commands**, without relying on additional tools.

You can read more about [ADB on the Android Developers Website](https://developer.android.com/tools/adb?hl=es-419).  


### ADB-Generated Backup

One of the console commands in [ADB](#adb) allows for creating a full backup of the device, including applications and some configurations. This is usually done with the ```adb backup``` command or via tools like AndroidQF. When executed, the device will prompt for a password to encrypt the information.

### Acquisition

This refers to a stage in forensic investigation where the forensic analyst must determine the best method to collect digital evidence, and apply it to gather the relevant artifacts. 

### AndroidQF

[AndroidQF](https://github.com/mvt-project/androidqf) is a free and open-source software tool **focused on forensic extraction from Android devices**, currently maintained by the [Amnesty International Security Lab](https://securitylab.amnesty.org/.

It is especially designed for journalists, activists, human rights defenders, and **technical labs supporting cases of digital surveillance and spyware threats**.

### APK

According to Wikipedia, an [APK](https://en.wikipedia.org/wiki/Android_application_package) file (Android Application Package) is used by the Android operating system to distribute and install packaged application components for smartphones and tablets. It is a variant of the Java JAR format.

### Binary

Software binaries refer to files containing only precompiled binary code — i.e., instructions readable by machines and **ready to execute**. Examples include files with the ```.bin```, ```.exe``` or ```.app``` extensions.

### Bit-by-bit copy

A bit-by-bit copy, also known as a disk image or DD, is the process of creating an exact replica of an electronic medium. It helps preserve the integrity of the original evidence by avoiding direct manipulation and ensuring compliance with best practices.

### Bugreport

A native command-line tool on Android, available via the graphical interface or ADB shell. It generates a bug report containing diagnostic logs, including outputs from logcat, dumpsys, and dumpstate. It is packaged in a ```.zip``` file with a structured folder system containing error logs, memory usage, system calls, network and device information, among others.

### Chain of custody

The process of clearly documenting who accessed the evidence and how it was handled is known as the **chain of custody**. Forensic evidence can be manipulated or destroyed during investigation, so the analyst must demonstrate the [integrity of the evidence](#data-integrity). If this cannot be properly demonstrated, the evidence may **not be admissible in legal proceedings**, or may be challenged and dismissed by other experts.

### CVE

A program and reference method for reporting, classifying, and publishing security vulnerabilities. Each vulnerability is assigned a unique CVE ID, such as `CVE-2014-0160`.

Read the [wikipedia page here](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures). 


### Data integrity

Data integrity, along with confidentiality and availability, is one of the key principles of information security. It aims to ensure that data is **accurate and reliable**, and **has not been altered** — whether intentionally or accidentally — while at rest, in use, or in transit.

### Developer mode

[**Developer options**](https://developer.android.com/studio/debug/dev-options) refer to a **hidden menu** in the Android operating system that enables advanced features designed for **debugging apps or system-level changes**. It includes options like graphical driver settings, advanced network configurations, and **experimental features**.

### DFIR (Digital Forensics and Incident Response)

This acronym refers to Digital Forensics and Incident Response. It is the result of integrating the incident response and forensic analysis procedure into a single set of combined tasks that cover aspects of both processes. 

### Diataxis

[Diátaxis](https://diataxis.fr/start-here/) is a framework for writing and organizing technical documentation. Its core principle is grouping content into four categories: **Explanations**, **How-to Guides**, **Tutorials**, and **References**. Each content type addresses a specific user need and has a distinct purpose and style.

### Digital forensics

Digital forensics is the process used to collect, preserve, analyze, and present digital evidence obtained from electronic media and devices, using **reliable, accurate, and repeatable investigative techniques and scientific methods**, ensuring results can be used in **legal proceedings**. [1](https://csrc.nist.gov/glossary/term/digital_forensics)

It involves discovering and examining data on electronic devices to **identify, recover, document, and interpret information** and its relation to [digital attacks](https://protege.la/ataques/). Following standard procedures and best practices **helps produce actionable evidence**, which can support **accountability efforts** and reduce the impunity behind digital attacks.

### Exploit

An [exploit](https://en.wikipedia.org/wiki/Exploit_(computer_security)) is a piece of software, data, script, or sequence of actions used to **leverage a security vulnerability** in an information system to cause unintended behavior.

### Expert witness

According to [Wikipedia](https://en.wikipedia.org/wiki/Expert_witness), an expert witness is a person recognized as a reliable source in a particular field, whose ability to assess and decide competently gives them authority among peers or the public.

In forensic investigations, an expert is someone with certified knowledge (for example through industry certifications or proven equivalent experience) who can analyze, evaluate, and issue opinions on collected evidence.

### Forensic artifact

A forensic artifact refers to evidence or data recovered during digital forensic analysis. This includes files, process logs, system logs, metadata, and more.

### Google Takeout

A feature for Google online accounts that allows users to extract data from different apps, access logs, security logs, email, etc. The process takes several days to complete.

[Use this link to access the feature and start a takeout request.](https://takeout.google.com/?pli=1)


### Graphical User Interface




### Hash

A [hash](https://en.wikipedia.org/wiki/Hash_function) is a cryptographic function that produces a unique value for a given data set. Common examples include MD5 and SHA1.

### Identification

A stage in the forensic process where the analyst determines **which devices, accounts, or systems may contain relevant information**. Examples include phones, computers, online accounts, storage media, etc. Ideally, the analyst should speak with the affected person to understand what happened, what actions were taken, and what evidence may be available.

### Indicator of Compromise (IOC)

An [indicator of compromise (IOC)](https://en.wikipedia.org/wiki/Indicator_of_compromise) is any data that describes a cybersecurity incident, malicious activity, or artifact through behavioral patterns. The goal is to format information so that other researchers or affected parties can reuse it to identify similar evidence and determine whether they've been compromised. This may include created files, modified registry entries, or new processes/services. If these indicators are found in a system, it likely indicates infection by the corresponding malware. IOCs enable practical information sharing based on forensic analysis, incident response, or malware research.

### Informed consent

[Consent](https://en.wikipedia.org/wiki/Consent) refers to a voluntary agreement between two or more parties regarding rights and obligations. In the context of digital forensic analysis for civil society, informed consent means **the agreement and approval of actions to collect, analyze, present, and preserve digital evidence**.

A key aspect is that the person providing consent must be able to make an **informed decision** about the investigation and retain the right to reject assistance. In practice, this means providing enough information so that the requestor understands the actions, risks, rights, and responsibilities involved. The **forensic analyst must communicate clearly and transparently**, and respect the will of the person requesting support.

Read more on informed consent in our [how-to guide](../how-tos/01-how-to-obtain-informed-consent/01-how-to-obtain-informed-consent.md). 


### Internet Service Provider (ISP) 

Refers to the company that provides Internet service to the user. These companies usually provide the _last-mile connection_ and may interconnect with other operators or directly with international submarine cables. 

### Lawfare (legal warfare)

Lawfare refers to the **use of legal systems or institutions to harm, discredit, or undermine individuals or organizations**.

Read more in the related [explainer on risks and threats for forensic labs](../explainers/02-explainer-risks-threats/02-explainer-risks-threats.md). 

### Log

Logs (also called records or audit trails) are files that document events occurring within a computer system, network, or application. These may include user access, system changes, errors, and other activity relevant to forensic investigations.

This resource includes considerations for [log-based forensic investigations on Android devices](../explainers/03-explainer-log-forensics-android/03-explainer-log-forensics-android.md)


### Malware

Malware (short for malicious software) refers to any kind of software designed to **harm or compromise** a system. Unlike faulty or buggy software, malware **acts with malicious intent**, typically without the user's knowledge — unlike potentially unwanted software.

### MVT

MVT is a tool that facilitates consent-based forensic analysis of devices belonging to individuals at risk of **advanced spyware attacks**, especially civil society members and vulnerable communities.

As stated on its [official site](https://forensics.socialtic.org/comunidad/licencia.html):

_Mobile Verification Toolkit (MVT) is a tool to facilitate the consensual forensic analysis of Android and iOS devices, for the purpose of identifying traces of compromise._

_It was developed and released by the Amnesty International Security Lab in July 2021 as part of the Pegasus Project, along with a forensic methodology. It continues to be maintained by Amnesty International and other contributors._

_This documentation provides instructions on how to install and run mvt-ios and mvt-android commands, as well as guidance on interpreting the extracted results._


### n-day

n-day refers to a type of [vulnerability](#vulnerability) that is already known but not yet patched in all affected systems. In some cases, official patches or mitigations may exist but have not yet been applied


### Phishing

Phishing is a technique based on impersonating or falsifying information to prompt the user to take an action — such as clicking on a link, opening an infected file, connecting to a fake network or system, or entering information on fake websites. The objective is usually to steal information or infect a device or information system.

* e.g., suspicious emails or SMS messages prompting the user to click on links  
* e.g., suspicious emails or SMS messages requesting private, sensitive, or financial information  
* e.g., suspicious emails prompting the user to open attachments


### Portable tool

Refers to a software tool that **does not require installation** to run. It does not modify or add files to the system but includes all necessary components in its folder or executable.

A key advantage is that it **leaves fewer traces of execution** compared to installed programs.

### Risk analysis

The specific risks an organization or individual faces **depend on their particular context and work**. The process of identifying vulnerabilities, risks, and threats at a given time is known as risk analysis.


### Security Incident Response

The goal of Incident Response procedures is to minimize the impact and contain the consequences of incidents. Effective response requires identifying the root cause of intrusions in order to eradicate the threat and enable timely recovery.

### SocialTIC  

[SocialTIC](https://socialtic.org) is a civil society organization based in Mexico. Its mission is to **safely empower changemakers in Latin America**, strengthening their work in analysis, social communication, and advocacy through the strategic use of digital technologies and data.

### Spyware 

A type of malware that collects information from a computer or mobile device and transmits it to an external entity without the owner's knowledge or consent. These tools have various capabilities, but generally allow access to stored and in-transit data, as well as manipulation of the device’s sensors (camera, microphone, etc.).

### Stalkerware

Stalkerware refers to spyware used on a small scale, primarily in intimate or personal settings such as between partners, family members, or friends.

These tools are usually installed with physical access to the device and are designed to collect as much information as possible. The attacker often has access to a control panel where they can view all the gathered data.

Such tools are often marketed as family protection software to prevent device misuse or theft. However, their features and capabilities make them viable for home surveillance and spying.


### Threat intelligence

According to [Wikipedia](https://en.wikipedia.org/wiki/Cyber_threat_intelligence), Cyber Threat Intelligence (CTI) is the activity of collecting knowledge, skills, and experience to evaluate cyber and physical threats, as well as threat actors, with the aim of mitigating attacks or harmful events.

The concept emerged to address the growing range of threats and support security professionals in recognizing indicators of attacks, understanding attacker methods, and responding accurately.

Threat intelligence aims to understand adversaries and **reduce institutional risk** by analyzing threats and identifying key information that can help attribute attacks. The goal is to enable **smart, timely defensive actions** against attack scenarios and advanced threats.

### Threat notification

Threat notifications refer to messages sent by platforms and manufacturers to individuals who may have been targeted.

According to Apple, threat notifications inform and assist users of devices that may have been targeted by mercenary spyware. Notifications are sent via email and iMessage to the addresses and phone numbers linked to a person’s Apple ID. They also appear at the top of the page after signing in to account.apple.com.

### TTP 

Short for _Techniques, Tactics, and Procedures_, this term refers to the set of methods and behaviors used by threat actors. The most well-known TTP framework is [MITRE ATT&CK](https://attack.mitre.org/), which also includes a historical registry of [TTPs associated with specific threat actors](https://attack.mitre.org/groups/).

### Triage

Security incident triage refers to the initial assessment and classification of incidents based on factors such as severity, urgency, and potential impact. The main goal is to allocate resources and set priorities effectively, allowing incident response teams to focus on the most critical threats and reduce organizational risk. This process is akin to medical triage, where patients are categorized by severity to determine treatment order.

### Volatility

Volatility in digital evidence refers to the fact that some system data is destroyed or altered over time.

For example, some log files are overwritten after reaching a storage limit, which means this kind of evidence may not be available permanently.

### Vulnerability 

A vulnerability refers to a weakness or deficiency in processes, systems, practices, or habits that can enable threats or increase the impact and consequences of an incident.

### Zero Click 

Refers to an attack that **requires no user interaction for malware to be installed**. These attacks are typically highly sophisticated and expensive, often requiring the chaining of multiple vulnerabilities to succeed.

### Zero Day

A type of attack that exploits a [vulnerability](#vulnerability) that is not yet known — not even by the device manufacturer. As a result, there are no patches or fixes available.

See the [Wikipedia page for "Zero-day attack"](https://es.wikipedia.org/wiki/Ataque_de_d%C3%ADa_cero).

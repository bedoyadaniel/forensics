---
title: Explainer - Introduction to consensual digital forensics for the defense of Human Rights 
summary: Explainer to introduce key concepts of consensual digital forensics in civil society
keywords: forensics, informed consent, introduction, stages, human rights
lang: en
tags: [explainer, intro]
last_updated: 2025-02-13
some_url:
created: 2025-02-13
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---



# Explainer - Introduction to consensual forensics for the defense of Human Rights 

This document is part of a **technical documentation repository** whose main objective is to establish a baseline of proven, flexible and accessible knowledge to **boost consensual forensic analysis in support of civil society across the globe**. To organize the contents, we use the [technical documentation framework Diátaxis](../../references/00-glossary.md#diataxis). 

This particular resource fits within [the explanation category in Diataxis](https://diataxis.fr/explanation/). It describes key concepts about digital forensics, including a definition, the different stages of an investigation and a description of how forensic science can be applied for the defense of Human Rights. This is an introductory material that tries to set a baseline understanding of key concepts in relation to consensual digital forensics, and that is complementary to other resources in this repository including [how-to guides](../../how-tos/), [tutorials](../../../tutorials/) and [references](../../../references/). 

## What is digital forensics and why is it important?

[Digital forensics](https://csrc.nist.gov/glossary/term/digital_forensics) relates to the process used for the collection, preservation, analysis and presentation of digital evidence, derived from electronic media and devices, using **data management best-practices, investigation techniques** and the scientific method to arrive at sound and reproducible conclusions that can be **admitted as evidence in judicial proceedings**.  

Digital Forensics is used to discover and examine digital media with the objective of **identifying, recovering, documenting and interpreting digital information** and how it is connected with digital attacks. When aligned with standard procedure and best practices, it allows for the documentation of useful evidence that can then be used for accountability and advocacy initiatives, that in turn can reduce the impunity with which digital attacks are often carried out. 

For example, in Poland, after [digital forensic investigations led by Amnesty Tech,](https://www.amnesty.org/en/latest/news/2022/01/poland-use-of-pegasus-spyware-to-hack-politicians-highlights-threat-to-civil-society/) Citizen Lab and other civil society groups, [Poland’s government launched an investigation](https://cyberscoop.com/inside-polands-groundbreaking-effort-to-reckon-with-spyware-abuses/) into the abuse of power, providing additional clarity in which contexts digital surveillance was used, and committing to notify potential targets. 

## Where is digital forensics applied?

In general, beyond being used as an accountability tool in Civil Society, forensic investigations are carried out with different objectives and areas of focus, for example:

* **Expert investigations for judicial proceedings:** They are often carried out by investigators in alignment with local laws for criminal or civil cases. Expert investigations are often carried out by police, military or judicial entities. Historically, a lot of the documentation and processes have been developed by these groups in contexts where there is no direct consent for the investigation. 

* **Academic investigations:** Through academic investigations researchers look to develop new lines and techniques for research that create improvements in the methodologies and generate practical knowledge to advance the forensic science field. 

* **Private sector investigations:** Private sector investigations are led by internal teams or external consultants, and have the goal of identifying the origin and the scope of possible intrusions and security incidents affecting business or institutions. 

* **Investigations to protect Human Rights Defenders (HRDs)**: In the context of protection to Human Rights Defenders, forensic investigations intend to generate, preserve and present evidence of digital security incidents affecting HRDs. The goal is to enable access to remediation and accountability mechanisms that reduce the attacker's impunity and expose perpetrators that violate fundamental rights. 

Frequently, forensic investigations start when there is a detection of a possible security incident. Although **forensic analysis and incident response** pursue different goals, consolidating both processes results in a stronger incident handling and containment that is also capable of collecting and preserving important evidence. 

[**Incident response**](https://www.ibm.com/topics/incident-response) is focused in **detecting and responding to security events and incidents**. Through well defined response procedures, it is possible to minimize the impact and contain the consequences of incidents. For an effective response, it is also important to uncover the root cause of intrusions, so that the threat can be eradicated in a timely manner.  

When incident response and forensic analysis are done separately, actions that are taken without adequate coordination can have an impact both and challenge both the response and the analysis. For example, **managing an incident without considering the need to document and preserve evidence, can result in damage or destruction of files and artifacts required of the forensic investigation**. In a similar way, focusing solely on the forensic analysis, might delay the contention of an incident, resulting in higher severity consequences and a longer resolution time. 

Therefore, **it is ideal to combine both processes in what is often referred to as [Digital Forensics and Incident Response](../../references/00-glossary.md#dfir-digital-forensics-and-incident-response) (DFIR)**, so that the response considers best practices for the collection and preservation of evidence, and findings from the forensic research can be used to contain and, ultimately, prevent future incidents. 

This guide and repository are focused on the forensic aspects of an investigation. However, please **keep in mind the close relationship that forensic has with incident response processes**, so that you can integrate forensic best practices when responding to emergencies and handling requests for assistance. 

## What are the usual stages of a forensic investigation?

There are several frameworks and norms that suggest a series of phases in order to complete a forensic investigation, including [norm ISO 27037](https://www.amnafzar.net/files/1/ISO%2027000/ISO%20IEC%2027037-2012.pdf) or [NIST guide to integrate forensic analysis into incident response.](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8428.pdf)


!!! success "Best Practice" 
    Throughout these different phases, it is key to maintain and ensure the integrity of evidence, and to create confidence in the analysis process. Due to its nature, digital evidence is fragile, since it can be altered or destroyed during the collection or analysis stages. This is why, no matter what framework or best practices you follow, you should always the following basic principles during the investigation cycle: 
    
    * Whenever possible, **avoid directly manipulating or working on the collected evidence**. Instead, use local copies that do not endanger the original evidence.   
    * **Documenting is a key aspect of any forensic investigation**. Any action that you take, any discovery that you make, any tool that you use, any hypotheses or conclusions that you arrive at should be well documented. It is important that a peer can review and reproduce your findings independently, looking at the evidence and the documentation.   
    * While it is not always possible to know what will happen in a given case, if you believe it might be possible that the evidence is used as part of a legal proceeding, familiarize yourself with the relevant legislation in the jurisdiction, including by consulting with a peer expert in legal matters. 

Most of the frameworks coincide in the following phases: **identification, collection, preservation, analysis and presentation**. Below we detail what happens during each of these phases. 

### Stage 1 - Identification

During the identification phase, the analyst **determines which devices, accounts or systems might contain relevant information for the investigation**. Examples include mobile phones, computers, online accounts, storage media, among others. Ideally, to determine which evidence to collect, the analyst should engage in a conversation with the impacted person, to understand what happened, what actions have been taken and what evidence and artifacts might be available. 

### Stage 2 - Collection and acquisition 

Once you identify the devices and systems that might contain evidence, the forensic analyst determines the best way to retrieve such evidence. **The prioritization and the exact procedure to be used depends on several factors**, including the type of incident, whether support is happening remotely or on the ground, the [volatility](../../references/00-glossary.md#volatility) of the evidence and the amount of effort required for the extraction. Keep in mind the following: 

* **It is possible that the analyst identifies more sources of information that you have capacity to collect.** For example, if you are investigating a potential spyware infection, relevant data might exist in the targeted device, the network equipment, devices from the ISP, online accounts, to name a few. You should prioritize the collection of evidence that, according to your experience, has the greater value and potential for the investigation, and requires a reasonable amount of effort to collect.   
* Due to its nature, **some digital data useful for analysis is volatile**, which means it can be altered or destroyed as time passes or when you interact or turn the device off. An example of volatile data would be the list of running processes on a device. In general, it is recommended to prioritize the extraction of volatile data over non-volatile data (like hard-drives and file systems).   
* Considering the above, the analyst can then make a decision on the best way to extract information from devices. For example, you can create a **physical image**, or [bit-for-bit](../../references/00-glossary.md#bit-by-bit-copy) copy of a storage media, to duplicate the contents, including information that might still be present but whose pointers were removed. Alternatively, you can also create **logical images**, or copy of visible archives. You might also want to extract **specific information**, for example targeted log files. 

### Stage 3 - Verification and preservation 

Once you extract information, it is important to document and verify the integrity of the collected data. The goal of the integrity verification is to **demonstrate that the information that has been collected from the device has not been altered during the analysis**.Verification and preservation are always important, but they are critical in case you pretend to use the evidence in legal proceedings. Normally, the verification involves the calculation of [cryptographic hash functions](../../references/00-glossary.md#hash) at the time of extraction, that generate an unique value for or fingerprint of a given data, that can be compared and verified later in the process. 

The preservation of evidence is closely related with the concept of [chain of custody](../../references/00-glossary.md#chain-of-custody), which is especially important when dealing with physical evidence like devices, hard drives, computers, etc. It requires the establishment of a paper trail that documents where, when and how evidence was collected, where it was stored and who had access to it. 

### Stage 4 - Analysis

During this phase, the analyst uses specialized tools and manual review to study and analyze the evidence to **establish hypotheses and derive conclusions about what might have occurred**. Often, the analysis will face large amounts of data, therefore a manual analysis can be slow and challenging, especially if there is no clarity on what or where to look. Some forensic tools can facilitate this process, especially if there is access to [indicators of compromise](../../references/00-glossary.md#indicator-of-compromise-ioc). During this phase, it is important to use consistent and reproducible procedures and methodologies that can be verified. Sometimes, it won't be possible to establish any conclusion from the existing information. 

### Stage 5 - Presentation

During the last step, an analyst **prepares and presents key conclusions derived from the analysis**. How the results are presented depends on the goal of the analysis and the audience. For example, it is different to present results to a potential target seeking an understanding of whether their devices were compromised, than presenting results in a public report whose goal is to expose abuses and document findings. If the report is intended to be used in legal proceedings it is helpful to consider the local jurisdiction and what might make expert testimony admissible in court. 

## How can digital forensics be applied in the defense of Human Rights?

Organizations and individuals that defend Human Rights, for the most part, do not have robust monitoring systems to generate timely alerts of potential threats against their devices or networks. Therefore, it is common that the **detection of an incident happens when consequences are evident**, for instance when a document is leaked or when they are locked out of their online accounts. Due to the limitation in resources, it is also uncommon for organizations to have digital security specialists among their team, which means many of the digital security tasks fall on internal technology or communication teams, assisted frequently by external specialized helplines or consultants. 

When an individual or an organization detects a potential incident, either through a suspicious behavior or through an alert (for example, [apple threat notifications](../../references/00-glossary.md#threat-notification), the helpline or the digital security point of contact starts a process to investigate and [triage](../../references/00-glossary.md#triage) the situation, to understand what happened, when it happened and what actions have been taken so far. From these initial steps, **it is important that the incident handler, in addition to [considering and assessing the wellbeing of the affected Human Rights Defender](https://vita-activa.org/2025/01/22/psychological-first-aid-manual-in-english-and-arabic/), incorporates digital forensic best practices to protect and collect evidence** that could potentially be helpful for accountability purposes. 

As it was mentioned above, **incident response and digital forensic processes are closely intertwined**. It is during that initial response that the incident handler identifies which systems, devices or accounts might contain useful evidence for a forensic investigation. It’s worth highlighting that in our context, **forensic investigations should always be consensual**, which implies that before collecting any data we should provide clear information about what the process entails and what the goal is, ideally through a written form. 

Figuring out exactly what to collect depends on several factors, including the willingness of the at-risk person to share information, the type of incident, the tools and resources available, the technical proficiency of the person doing the collection, among others. In some cases, the incident handler or point of contact can do an initial triage and collection, and work in collaboration with trusted third parties to further examine the data and identify signs and indicators of compromise. While **deep technical proficiency is not required to do the collection of evidence and artifacts**, it is important that whoever is doing the collection understands key concepts and considerations like the ones included in this resource. 

For example, in **some instances it is counterproductive to turn off and ship a device to a 3rd party forensic laboratory for analysis**. This would likely destroy useful volatile evidence –data that is altered or destroyed when manipulating or shutting off a device. If we want to collect this type of data, it is more convenient to use forensic tools that allow a **live collection** that includes information like running processes, temporary files, etc. 

!!! success "Buenas Prácticas" 
    Throughout this forensic process, **one of the most important aspects is keeping a good chronological documentation** of actions taken, evidence collected, hashes, tools used, issues faced, consent, etc. 

In most cases, evidence can not be deeply analyzed on site, and additional forensic tools, manual analysis and research are necessary to establish conclusions about what might have occurred. This offsite analysis is often conducted by analysts with deeper knowledge and understanding of the operating systems in question, and also have access to tools, indicators and methodologies for analysis. 

It is possible that **the initial analysis does not provide any immediate result or match with known signatures,** especially if this analysis rellies only on known vulnerabilities and if we suspect an advanced threat actor is involved, that could engage in efforts to delete traces of their activity. It is also possible that attackers use techniques to disrupt or hinder forensic analysis efforts, on what is commonly known as [anti-forensics](https://en.wikipedia.org/wiki/Anti%E2%80%93computer_forensics). 

Therefore, **not getting an immediate result does not mean that we can fully guarantee the device has not been targeted** or compromised, both because of anti-forensic techniques as well as limitations on access to useful forensic artifacts or threat intelligence . Moreover, threat actors often move dynamically, meaning that they sometimes do not maintain persistent access to devices. Finding the footprints of a threat actor using automated analysis tools often requires access to [threat intelligence](../../references/00-glossary.md#threat-intelligence) (in the form of [indicators of compromise](../../references/00-glossary.md#indicator-of-compromise-ioc)) that can be used to compare against our local collection. Additional manual analysis can take place to try and identify patterns and logs of potential new exploits and vectors of compromise. The IOCs and skills necessary for the discovery of new attacks might not always be readily available, and sometimes it might be helpful to store forensic evidence for additional study and investigation further down the road. This should always be done in clear consent with the impacted person, and making sure data management and data security policies are being followed. 

During the last 5 years, **different projects and funds have invigorated a global community of forensic analysts, including with a few emerging laboratories across in the global majority.** This has increased local capacities, but it is still crucial that collaboration remains at the center of all these efforts. Peer-to-peer support, within regions and globally, is fundamental for the collective success, including through greater sharing of threat information as well as building of skills and knowledge. The establishment of a forensic lab is usually the first step in a process that can take several years to mature, and where collaboration is key for long-term sustainability. 

## Important considerations when conducting forensic investigations

Below we detail a few important aspects to keep in mind when conducting forensic investigations in support of at-risk users from civil society. 

### Informed consent

Different from forensic investigations in other contexts (judicial, corporate), **forensic investigations in support of Human Rights Defenders should always be consented**. This means that the analyst should guide the person requesting support through the process, explain clearly what are the expectations and potential outcomes, detail what data would be collected and clarify any questions that may arise. It should be the person asking for the support who makes the final decision on how to proceed with the investigation. A written agreement is often advised. 

It is possible that some of the artifacts that are collected during a forensic investigation contain personal information (contacts, messages, applications, photos, etc), therefore **you should be transparent with beneficiaries about what is included, while also trying to minimize or eliminate any personal information that is not relevant for the forensic analysis**. If you plan to share artifacts or collected information with 3rd parties, it is important to inform upfront and get explicit consent to share with additional parties. 

### Chain of custody

[Chain of custody (CoC)](../../references/00-glossary.md#chain-of-custody), in legal contexts, is the **chronological documentation or paper trail that records the sequence of custody, control, transfer, analysis, and disposition of materials**, including physical or electronic evidence. In particular, forensic evidence is fragile in nature, since it can be manipulated or destroyed, and therefore, it becomes important for a forensic analyst to be able to describe the collection and custody process, and prove the [integrity](../../references/00-glossary.md#data-integrity) of the evidence used for analysis. Not having a robust trail and documentation of how the evidence was collected, stored and analyzed can result in it being inadmissible for legal proceedings, or to be contested and dismissed by other specialists. 

!!! abstract "Legal Consideration"
    If you intend to file legal cases or contribute with reports or as expert witness in legal proceedings, it is advisable to seek support from legal experts with knowledge of the jurisdiction.

The best way to demonstrate and verify the integrity of evidence is through clear chronological documentation that includes hashes (unique identifiers) or digital signatures of the collected files. Legal proceedings and depositions tend to happen several months or even years later after the initial analysis and collection happened, and therefore analysts rely in documentation to clearly explain when, where and what actions were taken during the investigation. It is also worth mentioning that there are some companies in the business of verifying and ensuring integrity of digital evidence, often in close connection with local legal frameworks. For example, [Verifact operates in Brasil](https://www.verifact.com.br/)


### Risks during a forensic investigation

Forensic investigations **can lead to the exposure and documentation of Human Rights abuses against at-risk individuals, often carried out by states or other powerful actors**. Due to the impact that these investigations can have as well as the capacities and resources of both states and spyware companies, it is important to engage in holistic risk assessment exercises before engaging in collection and analysis. 

There have been documented cases of [physical surveillance](https://www.nytimes.com/2019/01/28/world/black-cube-nso-citizen-lab-intelligence.html) and legal warfare against organizations doing forensic analysis, and there are often actions from states and companies to create obstacles, stop or even criminalize efforts from forensic labs and independent researchers. **Engaging in risk assessment activities regularly, and specially ahead of the publication of reports**, is important and necessary, and can help reduce and minimize consequences of legitimate research. There is a list of organizations that can support with risk assessment in the site of the Digital First Aid Kit. 

In addition, due to the fact that analysts will be investigating digital security threats and attacks, they will be frequently in contact with malicious infrastructure. It is also important to consider [operational security](https://en.wikipedia.org/wiki/Operations_security) measures that can protect against risks of self-compromise and also mitigate and assess the risk of alerting attackers and spyware operators of ongoing investigations, which could lead to a shift in infrastructure and practices, limiting the scope of the investigation.  

## Conclusion

Digital forensic investigations involve a series of **practices, methodologies, tools, skills and standards that can lead to verifiable conclusions about digital security incidents**. In the context of Human Rights defense, evidence collected through forensic investigations can boost accountability actions that reduce the impunity that is frequently tied with digital attacks. 

Consensual forensic analysis **implies following a rigorous, systematic and objective process across a series of phases**, where the goal is to guarantee the chain of custody and demonstrate the integrity of the evidence used for the analysis. Most of the steps in a forensic investigation are not technically complex, but do require a basic understanding of key concepts like informed consent and chain of custody. Labs and forensic researchers should also assess risks and take adequate precautions to mitigate risks that emerge from forensic investigations. 

It is by working together as a community and continuing to develop trust among emerging and established forensic labs that will be able to grow and strengthen the forensic practice in civil society. Peer collaboration is key to respond holistically to the needs of at-risk communities from civil society. **We extend an open invitation to collaborate with this resource and this repository.** If you have any observation or request, you can submit it directly through the [issues section of this repository](https://github.com/Socialtic/forensics/issues). If you have additional resources you would like to include into this repository, please reach out to [seguridad@socialtic.org](mailto:seguridad@socialtic.org). 


## Comments

Do you have any **comment or suggestion** about this resource? You can use the **comment function provided below** to leave your ideas, corrections or thoughts. Please make sure to follow our [code of conduct](../../community/code-of-conduct.md) when leaving your comment. If you prefer, you can also participate in the discussion directly in the [github repository](https://github.com/Socialtic/forensics/discussions). 



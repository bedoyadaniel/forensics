---
title: Explainer - Risks, threats and mitigations for forensic labs supporting Human Rights Defenders
summary: Risks, threats and mitigations for forensic labs supporting Human Rights Defenders
keywords: risks, threats, mitigations, fornsics labs, human rights
authors: Daniel Bedoya Arroyo and Gurshabad Grover
lang: en
tags: [explainer, intro]
last_updated: 2025-05-27
some_url:
---

# Explainer: Risks, threats and mitigations for forensic labs supporting Human Rights Defenders

This document is part of a **technical documentation repository** which has the main objective of establishing a baseline of proven, flexible and accessible knowledge to **boost consensual forensic analysis in support of civil society across the globe**. To organize the contents, we use the [technical documentation framework Diátaxis](https://diataxis.fr/). This particular resource fits within [the explanation category in Diátaxis](https://diataxis.fr/explanation/). It is complementary to other resources in this repository including [how-to guides](../../../how-tos/), [tutorials](../../../tutorials/) and [references](../../../references/). 

This document describes **risks, threats and vulnerabilities for forensic analysts and threat laboratories supporting civil society**. It is an introductory material that includes examples and links to resources that can help these groups to **understand and mitigate risks** they might encounter as part of their analysis and accountability work. 

This document was co-authored by the teams at [SocialTIC](http://socialtic.org) and the [Internet Research Lab](https://irl.works/). We appreciate the reviews and suggestions from Access Now, Marianne Parrot and Martijn Grooten that improved the content. All errors remain the responsibility of the authors.   

## Threats, vulnerabilities and risks: why should you care?

In the context of online safety of at-risk individuals or civil society organizations, a **threat** is a declaration or indication of an intention to inflict damage, punish or hurt. Threats can manifest in different ways, including through physical, legal or digital attacks, natural disasters, theft, etc. 

A **vulnerability**, on the other hand, refers to weaknesses in the processes, systems, practices or habits that can lead to threats or increase their impact and consequences. It refers to any factor which makes it more likely for harm to materialise or result in greater damage. 

A **risk** is the combination of the probability that a threat happens and the severity of the impact, if it ends up occurring. Risk is not static; it varies over time, depending on internal and external factors, making regular analysis and assessment of risks a necessary practice to reduce the possibility of harm.   

In the context of forensic support for Civil Society, as described previously in the [explainer on digital forensics for Human Rights Defense](https://forensics.socialtic.org/en/explainers/01-explainer-introduction-digital-forensics/01-explainer-introduction-digital-forensics/#how-can-digital-forensics-be-applied-in-the-defense-of-human-rights), the process usually starts when a Human Rights Defender, journalist or activist **approaches a point of contact or threat lab to request assistance**. In many scenarios, and particularly if they suspect they might be facing an advanced threat, they likely have a high risk profile, exposed to digital, legal, physical, natural, psychosocial and other threats. **The exact risks an organization or individual faces are unique to their context and profile**, and even when forensics do not focus on mitigating or implementing counter measures to manage risks, it is important for points of contact, analysts and forensic labs to be aware of such risks for their beneficiaries, and to **avoid engaging in actions that might increase their risk** for whomever is in need of support. 

Note that this document analyzes risks primarily *for the forensic labs* supporting human rights defenders. There are likely additional risks for the individuals requesting support with forensic analysis, and depending on the context and profile it might be ideal to refer them to a partner organization that can help them conduct an holistic risk assessment. Examples of such organizations are included later in this resource.  
   
It is important for forensic labs, analysts and points of contact to consider risks they might face due to their engagement in technical investigations. Through forensic research, civil society organizations **push for accountability measures that can have an impact in the surveillance ecosystem** by uncovering evidence of illegal or unethical practices, which means **some opponents will consider civil society forensic research as a threat**. 

In the next sections, we will provide examples of threat actors, types of threats and attacks that forensic labs and researchers have faced in the past, as well as some resources to initiate risk assessment exercises. 

## Where do threats come from? 

In order to know what **specific threats** an analyst or organization might face at any given point, it is necessary to conduct a holistic **risk assessment**. However, below you’ll find some common types of threat actors who civil society colleagues face: 

* **Spyware or surveillance vendors:** There is a [vast network of companies that develop](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf), broker, sell, and supply surveillance technologies, the majority of them are privately owned and generate revenue from the products and services they offer. Some lists are available including this [list by the Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/markets-matter-a-glance-into-the-spyware-industry/) or [this resource by Business and Human Rights](https://www.business-humanrights.org/en/companies/). Often, these companies, their founders, or their staff have ties to the military and intelligence sectors. For example, in the case of the infamous NSO group, [one of the co-founders previously served in the military intelligence and the Mossad](https://en.wikipedia.org/wiki/NSO_Group#Founding). Spyware companies have access to advanced technical capabilities, financial resources, legal counsel, and sometimes political power and connections. Forensic research can have an impact on the company's business and reputation, like when [Cellebrite stopped operations in Serbia and other countries](https://www.amnesty.org/en/latest/news/2025/02/cellebrite-halts-product-use-in-serbia-following-amnesty-surveillance-report/) due to human rights concerns, or more recently when NSO received a [large fine of 170 million dollars in the WhatsApp vs. NSO legal case](https://thehackernews.com/2025/05/nso-group-fined-168m-for-targeting-1400.html). Moreover, the exposure of infrastructure and vulnerabilities through forensic reports often means that developers of spyware need to switch to new infrastructure and find/exploit new vulnerabilities, which creates challenges and economic impacts for their business.  

* **State actors**: Oftentimes, states, police, military or intelligence agencies act as the operators of the spyware technology, which means they control who is targeted, and when and what information is retrieved. While many governments rely on commercial or mercenary spyware, some states also develop their own technology, with varying degrees of sophistication. Forensic research by civil society can lead to the exposure of abuses and violations of law and/or human rights, and potentially lead to [accountability actions](https://tfreedmanconsulting.com/wp-content/uploads/sites/264/Spyware-Mechanisms-Framework_Final.pdf), including through legal mechanisms. Thus, state actors can look to prevent, challenge, discredit or even criminalize civil society forensic investigations. 

* **Trolls and disinformation actors:** Since at least 2022, as additional forensic research by civil society exposed misuse of spyware, [some persistent actors have emerged to discredit findings by reputable labs using pseudoscience and disinformation](https://www.cmu.edu/ideas-social-cybersecurity/events/syynimaa_attacking_ngo.pdf). These campaigns have also resulted in harassment of researchers or organizations, and distraction from research activities. In other contexts, where social [media manipulation is a common practice](https://cjp.org.in/india-among-nations-manipulating-social-media-oxford-study/), networks of trolls have emerged in connection with [threat notifications](https://support.apple.com/en-us/102174), to spread misinformation and dismiss the validity of such notifications.   
    
* **For-profit cybersecurity companies:** A few cybersecurity companies have started engaging with civil society looking for indicators of compromise or other forms of threat intelligence that can support their research and development of for-profit products. The difference in incentives, resources and goals between the private sector and civil society can lead to extractive relationships that end up harming the reputation of forensic labs, and potentially victims if their data is not managed properly. Some specific examples have been reported privately, and some critics have been posted publicly, for example [this discussion on iVerify](https://discuss.grapheneos.org/d/14993-debunking-fake-stock-pixel-os-vulnerability-from-an-edr-company).

## Examples of threats 

While it is not possible to provide a complete list of all threats a forensic analyst or lab can face, we can describe examples of threats that have been observed in the past. 

### Digital attacks

By digital attacks, we refer to actions or behaviors with malicious intent, using digital technologies and communications. For example: 

* **Spear phishing**: Spear phishing refers to well-crafted, personalized phishing messages that take advantage of confidential or sensitive information to trick the recipient into opening or downloading a resource. This technique has been used in the past to compromise online accounts or to deliver malware, for example in 2024, when it was reported by the Citizen Lab and Access Now [that an advanced actor engaged in spear phishing](https://citizenlab.ca/2024/08/sophisticated-phishing-targets-russias-perceived-enemies-around-the-globe/) to compromise authors of high profile investigations into official corruption and abuses of power in Russia.


* **Spyware attacks**: Human Rights Watch members from Jordan were attacked with spyware, [according to Access Now](https://www.accessnow.org/publication/between-a-hack-and-a-hard-place-how-pegasus-spyware-crushes-civic-space-in-jordan/#who-was-hacked). The attack happened after the release of a report criticizing government repression. Other examples include NSO targeting of Amnesty International in 2018, as reported by [Amnesty International](https://www.amnesty.org/en/latest/research/2018/08/amnesty-international-among-targets-of-nso-powered-campaign/) and [Citizen Lab](https://citizenlab.ca/2018/07/nso-spyware-targeting-amnesty-international/). 


* **Doxxing**: Doxing (also “doxxing”, or “d0xing”, a word derived from “documents”, or “docs”) consists of tracing, gathering and publishing information about someone using sources that are freely available on the internet (called [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence), or Open Source INTelligence). Although not reported publicly, there have been cases where participants in spyware investigations have been doxxed on social media. While not pertaining to forensic analysts, this report documents how [fact-checkers have faced similar threats in Indonesia.](https://www.ifj.org/media-centre/news/detail/category/press-releases/article/indonesia-fact-checker-targeted-by-doxing-attacks)   
    
* **Information compromise and information leaks**: Threat actors might seek to gain access to sensitive information that analysts or labs possess, like the identity of victims seeking support, information about unpublished indicators of compromise or other confidential information that might endanger staff members.  Attacks can also target service providers that also have access to confidential information, including online storage for case or contact management, like the [incident reported against the International Red Cross Committee (IRCC) back in 2022](https://www.theregister.com/2022/01/20/red_cross_hit_by_cyberattack/). 

### Legal attacks

Legal attacks can happen when states use national security or cybersecurity laws to criminalize forensic research. Attacks can also take place as part of legal proceedings, as described below. 

* **Criminalization of forensic research and researchers**: In Ecuador, the Swedish researcher [Ola Bini has been subject to an extensive legal process](https://www.eff.org/deeplinks/2023/03/aftermath-ola-binis-unanimous-acquittal-ecuadorian-court), where even after being declared innocent in 2023 due to lack of evidence, they were then [further prosecuted through appeals](https://peoplesdispatch.org/2024/04/08/activist-ola-bini-sentenced-to-one-year-in-prison-after-ecuadorian-court-overturns-acquittal/).    
    
* **Lawfare**: Lawfare refers to use of legal systems and institutions to damage, discredit or affect an individual or organization. For example, in relation to Citizen Lab’s involvement in the WhatsApp lawsuit against NSO, [the spyware developer attempted to use the courts to get access to sensitive information](https://theintercept.com/2024/05/06/pegasus-nso-group-israeli-spyware-citizen-lab/), including confidential information about victims. In another example, in [2018, Sandvine threatened Citizen Lab with a defamation lawsuit](https://citizenlab.ca/wp-content/uploads/2018/03/February-16-2018-letter-from-Sandvine.pdf) due to their publication of research highlighting the use of Sandvine technology to inject spyware and block websites.   
    
* **Subpoenas and data requests:** In line with attempts to criminalize research, it is possible that authorities try to use legal processes, subpoenas and other mechanisms to obtain personal information of researchers or forensic labs. For example, in 2019, the Argentinian researcher Javier Smaldone made [public data requests made by the police to ISPs and service providers](https://blog.smaldone.com.ar/2020/01/25/allanado-y-detenido-por-tuitear/) (including WhatsApp). 


### Reputational

Forensic labs could also face reputational threats related to their work on digital forensics, including through unsubstantiated claims or disinformation. Trolls and misinformation actors can also engage in social media campaigns to discredit and dismiss findings. 

* **Publications and pseudoscience:** Pseudoscience refers to statements, beliefs, or practices that claim to be both scientific and factual but are incompatible with the scientific method. Research by both Citizen Lab and Amnesty International has been criticized by “experts”, which creates disruption and consumes resources from organizations. Examples include [misinformation actors aiming to discredit](https://medium.com/@maldr0id/misinformation-in-malware-analysis-232c7bb6b73e) the \#CatalanGate research and publications.

### Physical

Physical attacks have been used to intimidate, discourage and prevent forensic research from taking place. 

* **Harassment and physical surveillance:** In 2020, [the New York Times reported a case of physical surveillance](https://www.nytimes.com/2019/01/28/world/black-cube-nso-citizen-lab-intelligence.html) of a Citizen Lab researcher by an Israeli private intelligence firm. This [Youtube video](https://www.google.com/url?q=https://youtu.be/Z8IrU_jvnFk&sa=D&source=docs&ust=1746751117649066&usg=AOvVaw2tF-ALmh6Zj-FIFyn4GmwM) recounts the story and provides details into how it developed.   
    
* **Detentions, raids and arrests:** As stated above, different laws can be used to criminalize forensic research, including national security or cybersecurity legislation. This can lead to raids, detentions and arrests. For example, in 2019, the Argentinian security researcher Javier Smaldone [was subject to raids and detention simply for being active on social media regarding vulnerabilities in e-voting machines.](https://blog.smaldone.com.ar/2020/01/25/allanado-y-detenido-por-tuitear/) 

### Psychosocial

Analysts and forensic labs providing support to at-risk individuals should take into account threats to their own well-being that can result from supporting individuals targeted by spyware. Any individual or organization providing direct service  to people at risk can expose themselves to wellbeing threats, and offering technical support for device analysis is no exception. For example, [this report from Access Now describes the psychological impact spyware has on women human rights defenders](https://www.accessnow.org/women-human-rights-defenders-pegasus-attacks-bahrain-jordan/). 

* **Compassion fatigue or secondary trauma:** [Compassion fatigue](https://en.wikipedia.org/wiki/Compassion_fatigue) or s[econdary trauma](https://en.wikipedia.org/wiki/Secondary_trauma#cite_note-Cieslak_2014-1) refers to the psychological trauma which may be incurred by contact with people who have experienced traumatic events, exposure to disturbing descriptions of traumatic events by a survivor, or exposure to others inflicting cruelty on one another.   
    
* **Burnout:** [Burnout](https://en.wikipedia.org/wiki/Occupational_burnout) is a state of chronic stress that leads to physical and emotional exhaustion, cynicism, detachment, and feelings of ineffectiveness. Burnout can leave people unable to function on a personal or professional level. Those suffering from burnout may need considerable time off to recuperate physically and psychologically or may not be able to return to work at all. Studies and research have shown that [human rights defenders and those to violations and distress, are likely to suffer from burnout](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0145188).  


### Operational

Aside from digital, physical, legal and psychological threats to the work of forensic analysts and threat labs, it is important to keep in mind risks associated with the operation and sustainability. 

* **Sustainability and access to resources:** The provision of forensic analysis requires a combination of technical know-how, access to technical tools, experience and procedures, not just to provide consistent and clear analysis, but to mitigate some of the threats outlined in this document. Maturing capacities takes time and resources. Therefore, it is important for labs to think about their sustainability, in particular if they aim to become a resource for a vulnerable community, taking into account that the development of skills and expertise requires sustained financial and human resources over several years.   
    
* **Staff retention:** There is a [well-documented shortage](https://www.weforum.org/stories/2024/04/cybersecurity-industry-talent-shortage-new-report/) of technical workers on digital security. Civil society is not the exception, and several organizations and threat labs have faced challenges finding and contracting staff with both expertise to conduct forensic analysis and sensibility and understanding of Human Rights issues. Moreover, in several cases, when organizations invest in the development of skills, there is a chance that individuals can pursue better-paying work ventures in the private sector. 

* **Resilient infrastructure and services**: The work of forensic labs is often driven by external events, such as a surge in support requests due to a political crisis in a country. For example, influencers responding to mass protests in Ethiopia encouraged protestors to contact a civil society forensic lab for support, increasing the number of support requests by more than 10x fold in 24hrs and causing the forensic lab infrastructure to crash under the load. Exploring scenarios can help forensic labs develop contingency procedures, plans and infrastructure.

## Prevention and risk management

As we have mentioned throughout this resource, we encourage forensic labs and researchers supporting civil society to **conduct** **risk assessment exercises regularly**, and particularly before engaging in research with high-risk individuals or when operating from a high-risk context.

In this resource we are not focusing on the step-by-step of how to start a risk assessment cycle, but we will **point to existing resources and partner organizations that might be able to support or advice** to prevent different types of threats.

### Resources for risk assessment

The following are some available resources to initiate and engage in exercises to assess risks: 

* [Cybersecurity Assessment Tool (CAT)](https://cybercat.tools/#assessment): The Cybersecurity Assessment Tool (CAT) is designed to measure the maturity, resiliency, and strength of an organization’s cybersecurity efforts. It can help threat labs and organizations hosting them do an assessment of their own risks, threats, vulnerabilities and opportunities.   
    
* [SAFETAG](https://safetag.org/): SAFETAG is a professional audit framework that adapts traditional penetration testing and risk assessment methodologies to be **relevant to smaller non-profit organizations based or operating in the majority world**.   
    
* [Creating a security plan](https://ssd.eff.org/module/your-security-plan): EFF has a resource under their surveillance self-defense (SSD) guide that can be especially helpful for **individuals and independent analysts** to create a security plan to manage risks.  

* [Workbook on Security](https://www.frontlinedefenders.org/sites/default/files/flds_workbook.pdf): Front Line Defenders maintains a holistic security guide for human rights defenders at risk,  that can be used to guide individual or organisational security planning. This resource is available in many different languages.

### Organizations, resources and partners in the field

The following is a list of organizations that might be able to support in managing, preparing and preventing against different type of risks:

**Technical**  

* [Access Now Digital Security Helpline](http://accessnow.org/help)  
* [Cyber hub](https://cyberhub.am/en/)  
* [SocialTIC](mailto:seguridad@socialtic.org)  
* [Front Line Defenders](https://www.frontlinedefenders.org/)  
* [Open briefing](https://openbriefing.org/)

      
**Legal support**

* [Media Legal Defense Initiative](https://www.rcmediafreedom.eu/Tools/Support-centres/Media-Legal-Defence-Initiative-MLDI)  
* [Access Now](http://accessnow.org/help)  
* [Article 19](https://www.article19.org/regional-office/mexico-and-central-america/)

**Psychosocial & well-being**  

* [Vita Activa Feminist Helpline](https://vita-activa.org/)  
  * Resources include how to [deal with indirect trauma](https://vita-activa.org/2021/02/08/trauma-indirecto/) and [why burnout affects women more.](https://vita-activa.org/2022/03/15/el-burnout-por-que-afecta-mas-a-las-mujeres/)    
* [Open briefing](https://openbriefing.org/)  
  * Resources include [risk assessment tools](https://www.openbriefing.org/services/security/risk-assessments/) and a resource on [compassion fatigue, vicarious trauma, and burnout: Infosheet for those supporting human rights defenders](https://openbriefing.org/resources/compassion-fatigue-vicarious-trauma-and-burnout-infosheet-for-those-supporting-human-rights-defenders/)

**Physical security**   

* [Frontline Defenders](https://www.frontlinedefenders.org/)  
* [Open Briefing](https://openbriefing.org/)  

      
**Sustainability**

* [Engine Room](https://www.theengineroom.org/)  
  * Resources include [how to think about compensation for a global remote team](https://www.theengineroom.org/library/rethinking-compensation-for-a-global-remote-team/) as well as a [report on funding for a sustainable ecosystem](https://www.theengineroom.org/library/tipping-the-scales-what-it-takes-to-fund-an-equitable-tech-human-rights-ecosystem/). 


**Resources for incident response**  

* [Feminist Helplines](https://feministhelplines.org/)  
* [DFAK](https://digitalfirstaid.org/)

## Conclusion

Throughout this document, we have presented threats, risks and resources that might support the risk assessment process of civil society organizations and individuals engaging in forensic analysis. If this is the first time you are reading about some of these threats, it can be surprising to know the extent to which threat actors are willing to go in order to discourage and prevent forensic research. 

Rather than undermining or depressing emerging efforts, with this resource we aim to provide the necessary context to engage in forensic analysis and research responsibly, and to emphasize the importance of operational security practices, policies and investments to ensure that our research is leading to accountability actions without inflicting more harm on those targeted or the people supporting them. 

If you have any observation or request for change on this documentation repository, you can submit an issue directly through the  [github issue section of this repository](https://github.com/Socialtic/forensics/issues). If you have additional inquiries, please reach out to [seguridad@socialtic.org](mailto:seguridad@socialtic.org).
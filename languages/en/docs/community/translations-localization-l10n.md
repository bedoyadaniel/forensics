---
title: Community - Additional translation and localization efforts
summary: Considerations for additional translation and localization efforts 
keywords: forensics, community, consensual, contribuition
lang: en
tags: [community, localization, translation]
last_updated: 2025-07-15
some_url:
created: 2025-07-15
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---

# Additional translation and localization efforts

At SocialTIC, we understand the importance of **maintaining resources that are accessible**, easy to read, and capable of **having an impact on communities with different technical capacities and from multiple regions around the world**. Due to our expertise and geographical location, our resources will often be **available first in Spanish**, and the necessary resources will be allocated afterward to translate them into English. If you are interested in **collaborating on translations** from Spanish to English—or vice versa—please contact us at: **seguridad@socialtic.org**.

If you are interested in translating the repository's content into a **new language**, we kindly ask that you **notify us** by opening a new issue or by contacting us directly at seguridad@socialtic.org. While we strongly agree on the importance of localization, there are a **few key considerations before starting a translation**:

* Capacity and sustainability: Translating and localizing content is **hard work**. At SocialTIC, we deeply appreciate any effort to promote consensual forensic analysis among vulnerable populations, especially in the global majority. However, before beginning a translation, we recommend **evaluating the medium- and long-term sustainability of the effort**. This helps ensure that new communities accessing these materials will have access to content with a **minimum level of continuity and maintenance**.  
* Content review: In our experience, it is **ideal to have a second person conduct a review** in addition to the initial translation. If you are unable to identify someone to review your translation, feel free to reach out to us—we can help coordinate support.  
* Updates and maintenance: Our **vision is for this repository to grow** and evolve continuously. We expect the **first few years to be the most intense** in terms of producing triage and acquisition materials, followed by more specialized content.  
* Style guidelines: We recommend **creating a short style guide** that includes considerations such as the use of anglicisms, inclusive language, and other key decisions.  
* Usage license: This repository extends the MVT license to support and encourage consensual forensic analysis.

---

## Content Structure

The repository is **structured to support translations into new languages**. In general, content across all languages is **organized** in the following way:

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

Additionally**, each new piece of content will have its own corresponding folder**, which contains a Markdown file with the content. For example, the explainer titled *"Introduction to Consensual Digital Forensics for the Defense of Human Rights"* is organized as follows in both English and Spanish:

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

Before starting a translation, we recommend exploring the content folders and reaching out with any questions. It is also advised to **review the style guidelines for file naming**, which are included as part of the repository’s contribution best practices.

To contribute translations directly to the repository, please follow the instructions outlined in the *pull requests* or integration requests section.
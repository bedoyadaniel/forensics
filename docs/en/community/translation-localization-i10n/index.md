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

translation-review-pending: true
---

At SocialTIC we understand the importance of maintaining **resources that are accessible**, **easy to read** and that can have an impact on **populations with different technical capabilities and in multiple regions of the world**. Due to our expertise and geographic location, our resources will often be **available first in Spanish,** and then translated into the other available languages.
# Additional translation and localization efforts
To facilitate this translation process, a script was developed that uses the *deepl* API to generate automatic translations. This script is [described in detail in the corresponding documentation](../../../../scripts/translate-readme.md). which integrates directly to the repository to generate draft versions. This automatic script requires manual revisions, so if you are interested in **collaborating with the translation of resources from Spanish to English**, or vice versa, please write to [**seguridad@socialtic.org**](mailto:seguridad@socialtic.org).

While this automatic translation script makes it easy to localize resources, there are some important considerations before starting a translation:
At SocialTIC, we understand the importance of **maintaining resources that are accessible**, easy to read, and capable of **having an impact on communities with different technical capacities and from multiple regions around the world**. Due to our expertise and geographical location, our resources will often be **available first in Spanish**, and the necessary resources will be allocated afterward to translate them into English. If you are interested in **collaborating on translations** from Spanish to English—or vice versa—please contact us at: **seguridad@socialtic.org**.

If you are interested in translating the repository's content into a **new language**, we kindly ask that you **notify us** by opening a new issue or by contacting us directly at seguridad@socialtic.org. While we strongly agree on the importance of localization, there are a **few key considerations before starting a translation**:

* Capacity and sustainability: Translating and localizing content is **hard work**. At SocialTIC, we deeply appreciate any effort to promote consensual forensic analysis among vulnerable populations, especially in the global majority. However, before beginning a translation, we recommend **evaluating the medium- and long-term sustainability of the effort**. This helps ensure that new communities accessing these materials will have access to content with a **minimum level of continuity and maintenance**.  
* Content review: In our experience, it is **ideal to have a second person conduct a review** in addition to the initial translation. If you are unable to identify someone to review your translation, feel free to reach out to us—we can help coordinate support.  
* Updates and maintenance: Our **vision is for this repository to grow** and evolve continuously. We expect the **first few years to be the most intense** in terms of producing triage and acquisition materials, followed by more specialized content.  
* Style guidelines: We recommend **creating a short style guide** that includes considerations such as the use of anglicisms, inclusive language, and other key decisions.  
* Usage license: This repository extends the MVT license to support and encourage consensual forensic analysis.

---

## Content Structure


The repository is **structured to support translations into new languages**. To handle localization and translations, we use the [plug-in mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/) with the folder structure. This means that contents across languages are organized in equal structures, with **matching file and folder names across languages.** 

Folder names are defined in English, and names are replicated across languages. Despite folder names being in English, **Spanish is the default language for the repository**. The docs/ folder have the following structure: 


```
docs/
  es/
    localized-assets/
      resource 1/
        image1.png
    home/
      getting-started/
        index.md
      roadmap/
        index.md
    explainers/
      explainer-topic-01/
        index.md
      explainer-topic-n/
        index.md
    how-tos/
      how-to-topic-01/
        index.md  
      how-to-topic-n/
        index.md
    tutorials/
      tutorial-topic-01/
        index.md  
      tutorial-topic-n/
        index.md
    references/
      reference-topic-01/
        index.md
      reference-topic-n/
        index.md
    index.md

```

Each **new content will have its new corresponding folder**, where a file with the name 'index.md' will have the contents in MarkDown fomat. For example, the 'Explainer: Introduction to consented forensics for the defense of human rights' will look as follows in the folder structure:

```
es/
  explainers/
    01-explainer-introduction-digital-forensics/
      index.md

en/
  explainers/
    01-explainer-introduction-digital-forensics/
      index.md
	
```
As you can see, **there are virtually no differences** except for the location of the files and folders. 

To contribute translations directly to the repository, please follow the instructions outlined in the [pull requests requests section](../../community/how-to-contribute/index.md#integrating-new-content-through-pull-requests).
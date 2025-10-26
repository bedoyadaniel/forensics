---
title: Explicador - Introdução à perícia digital consentida para a defesa dos direitos humanos  
summary: Documento introdutório à perícia digital consentida em benefício da sociedade civil para a defesa dos direitos humanos
keywords: forensics, informed consent, introduction, stages, human rights
lang: pt-br
tags: [explainer, intro]
last_updated: 2025-09-05
some_url:
created: 2025-02-03
comments: true
authors:
    - Daniel Bedoya
    - MariaLab
    - Data Privacy Brasil
    
---

# Explicador: Introdução à perícia digital consentida para a defesa dos direitos humanos

Este documento faz parte de um repositório de documentação técnica que tem como objetivo estabelecer uma base de conhecimento comprovada, flexível e acessível para promover a análise forense consentida em benefício da sociedade civil. A [estrutura de documentação técnica Diataxis](https://diataxis.fr/) é usada para organizar o conteúdo.

Este documento é classificado como [material explicativo](https://diataxis.fr/explanation/). Ele descreve os principais conceitos da ciência forense digital, incluindo uma definição tradicional, uma visão geral dos estágios de uma investigação e uma discussão sobre como a [ciência forense](https://es.wikipedia.org/wiki/Criminal%C3%ADstica) é aplicada no contexto digital para a defesa dos direitos humanos. É um material introdutório, que tem como objetivo fornecer uma base de conhecimento geral sobre a prática forense, e é complementado por recursos adicionais, como [guias](../../how-tos/){ data-preview }, [tutoriais](../../tutorials/){ data-preview } e [referências](../../references/){ data-preview }.

## O que é a perícia forense digital e por que ela é importante?

A perícia digital é usada para descobrir e examinar dados de dispositivos eletrônicos a fim de **identificar, recuperar, documentar e interpretar informações digitais** e sua conexão com [ataques digitais](https://protege.la/ataques/). O uso de procedimentos padrão, de acordo com as práticas recomendadas, **permite gerar evidências úteis** para impulsionar ações de **responsabilização**, o que pode reduzir a impunidade com que os ataques digitais são executados.

Por exemplo, na Polônia, após [investigações forenses lideradas pela Citizen Lab, Amnesty Tech](https://www.amnesty.org/en/latest/news/2022/01/poland-use-of-pegasus-spyware-to-hack-politicians-highlights-threat-to-civil-society/) e outros grupos da sociedade civil, o governo da [Polônia lançou uma investigação sobre possíveis abusos de poder](https://cyberscoop.com/inside-polands-groundbreaking-effort-to-reckon-with-spyware-abuses/), esclarecendo o contexto em que as tecnologias de vigilância foram usadas em detrimento da sociedade civil e comprometendo-se a notificar os indivíduos potencialmente afetados.

## Onde a perícia digital é utilizada?


As investigações forenses podem ser realizadas com diferentes objetivos e abordagens, por exemplo:

<div class="grid cards" markdown>

-   :material-police-badge:{ .lg .middle } __Investigações forenses__

    ---

    São conduzidas em conformidade com as estruturas legais e seu principal objetivo é coletar e apresentar evidências que possam ser usadas em **processos judiciais, sejam eles civis ou criminais**. As investigações forenses são conduzidas principalmente por agentes de investigação ligados ao governo. Historicamente, essa tem sido a abordagem investigativa mais comum e de onde se originam algumas das práticas e estruturas.

-   :fontawesome-solid-university:{ .lg .middle } __Pesquisa acadêmica__

    ---

    Busca identificar **novas linhas de pesquisa** que promovam métodos e gerem conhecimentos práticos e teóricos que façam avançar o campo da investigação forense.

-   :fontawesome-solid-money-bill-1-wave:{ .lg .middle } __Investigações do setor privado__

    ---

    São conduzidas por equipes internas ou consultores externos. Elas buscam esclarecer a **origem e o escopo de intrusões e incidentes** em contexto de empresas ou instituições.

-   :octicons-megaphone-16:{ .lg .middle } __Proteção dos defensores dos direitos humanos (HRDs)__

    ---

    No contexto da proteção dos defensores dos direitos humanos, as investigações forenses **buscam gerar, preservar e apresentar evidências de incidentes de segurança digital em detrimento dos defensores dos direitos humanos.** O objetivo é fornecer às pessoas afetadas acesso a mecanismos de justiça que reduzam a impunidade e exponham os abusos de poder e as violações de seus direitos fundamentais.


</div>


As investigações forenses geralmente começam quando um possível incidente de segurança é detectado. Embora a **análise forense e a resposta a incidentes** tenham objetivos diferentes, a consolidação dos dois processos fortalece a maneira como os incidentes são respondidos, preservando as evidências.

A [resposta a incidentes](https://www.ibm.com/br-pt/topics/incident-response) concentra-se em **detectar e responder a eventos de segurança**. Por meio de procedimentos de resposta, o objetivo é minimizar o impacto e conter as consequências dos incidentes. Para uma resposta eficaz, é importante identificar a causa raiz das invasões, de forma que a ameaça possa ser erradicada e a recuperação seja feita em tempo hábil.
Se a resposta a um incidente e a análise forense forem realizadas separadamente, as ações tomadas podem interferir e dificultar tanto a resposta quanto a análise. Por exemplo, **ao responder** a um incidente sem levar em consideração as necessidades de preservação de evidências, **podem ser alteradas ou destruídas provas** e artefatos necessários para a análise forense. Da mesma forma, se nos concentrarmos apenas na análise forense, poderemos **atrasar a contenção da ameaça** e aumentar as consequências e o tempo de resolução de um incidente.

Portanto, **é vantajoso [combinar ambos os processos](https://www.paloaltonetworks.es/cyberpedia/digital-forensics-and-incident-response)**, de modo que, durante a resposta a um incidente, sejam consideradas as melhores práticas para a coleta e preservação de evidências e que as descobertas resultantes da análise forense sejam utilizadas para conter e erradicar ameaças e, por fim, prevenir incidentes futuros.


``` mermaid
flowchart LR
  A[Resposta a Incidentes] --> C[DFIR];
  B[Forense Digital] --> C;
```

Este guia e repositório documental se concentram na análise forense. No entanto, é importante **considerar a estreita relação que existe entre os processos de resposta a incidentes**, de forma que as boas práticas forenses possam ser integradas durante o atendimento a casos e situações de emergência.

## Quais são as etapas de uma investigação forense?

Existem diferentes referências que propõem uma série de etapas para concluir uma investigação forense, como, por exemplo, a [norma ISO 27037](https://www.amnafzar.net/files/1/ISO%2027000/ISO%20IEC%2027037-2012.pdf) ou o guia do [NIST para a integração da análise forense em processos de resposta a incidentes](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8428.pdf).

Através deste conjunto de etapas, **procura-se garantir a integridade das provas e a confiança no processo aplicado**. Por sua natureza, as provas digitais são frágeis, pois podem ser alteradas ou destruídas durante o processo de extração ou análise.  É por isso que, independentemente do conjunto de referências utilizado, os seguintes princípios básicos devem ser levados em consideração durante todo o ciclo de uma investigação:

!!! success "Boas práticas" 

    * Na medida do possível, deve-se evitar **manipular e trabalhar diretamente sobre as evidências coletadas**. Em vez disso, é recomendável utilizar cópias de trabalho que não coloquem em risco as evidências originais.
    * **Documentar é um aspecto fundamental durante uma investigação forense**. Qualquer ação tomada sobre as evidências, ferramentas utilizadas para a análise, descobertas e hipóteses devem ser documentadas. É importante que um terceiro possa reproduzir e verificar de forma independente a análise realizada.
    * Se você pretende usar as evidências como parte de um processo judicial, é necessário **conhecer a legislação e o quadro jurídico** que torna as evidências admissíveis em um tribunal.

A maioria dos processos jurídicos de referência seguem as seguintes etapas: **identificação, coleta, preservação, análise e apresentação**. A seguir, detalhamos em que consiste cada uma dessas etapas:

``` mermaid
graph LR
  A[1- Identificação] --> B[2- Coleta e aquisição];
  B --> C[3- Verificação e preservação];
  C --> D[4- Análise];
  D --> E[5- Apresentação];
```

=== "1- Identificação"

    Durante a identificação, o analista determina **quais dispositivos, contas ou sistemas podem conter informações relevantes para a investigação**. Exemplos de dispositivos incluem telefones celulares, computadores, contas online, meios de armazenamento, entre outros. Idealmente, para determinar as evidências a serem coletadas, o analista deve entrar em contato com a pessoa afetada, para entender o que aconteceu, quais ações foram tomadas até o momento e quais evidências podem estar disponíveis.

=== "2- Coleta e aquisição"

    Uma vez identificados os dispositivos e sistemas que podem conter evidências úteis, a pessoa analista forense deve determinar a melhor forma de coletar as evidências forenses. **O que priorizar e como realizar a extração dependerá de vários fatores**, incluindo o tipo de incidente, o tipo de atendimento (no local ou remoto), a [volatilidade das evidências](https://www.sciencedirect.com/topics/computer-science/volatile-evidence) e o esforço necessário para a extração. Considerações adicionais para a extração incluem o seguinte:
    * É possível que a pessoa analista identifique **mais fontes de informação do que aquelas que podem ser extraídas**. Por exemplo, se houver suspeita de uma infecção por spyware, pode haver informações relevantes no dispositivo afetado, nos equipamentos de rede, nos equipamentos do provedor de serviços, entre outros. Deve-se priorizar as evidências que, de acordo com a experiência, tenham maior valor para a investigação e exijam menos esforço.
    * Por sua natureza, **alguns dados úteis para a análise são voláteis**, ou seja, as informações são destruídas ou alteradas com o tempo, ao desligar o dispositivo ou ao interagir com ele. Um exemplo de informação volátil é a lista de processos ativos em um dispositivo em um determinado momento. Em geral, é recomendável priorizar a extração de dados mais voláteis em relação aos menos voláteis (como o sistema de arquivos).
    * Levando isso em consideração, a pessoa analista pode optar por diferentes tipos de extração.  Por exemplo, pode-se realizar uma **cópia física** ou [cópia bit a bit](https://forense.io/glossario/o-que-e-bitstream-copy-importancia-forense-digital/) de uma unidade de armazenamento, a fim de duplicar integralmente seu conteúdo, incluindo informações presentes na unidade, mas que podem ter sido excluídas. Alternativamente, pode-se realizar uma **cópia lógica**, ou seja, uma cópia dos arquivos visíveis. Em alguns casos, o analista pode realizar uma extração de **informações específicas**, por exemplo, apenas arquivos de log.

=== "3- Verificação e preservação"

    Uma vez realizada a extração, é importante verificar a integridade das evidências coletadas. O objetivo é conseguir **demonstrar que as evidências analisadas não foram alteradas**. A verificação e a preservação são sempre importantes, mas têm especial relevância se pretende-se utilizar as evidências em processos judiciais. Normalmente, a verificação da integridade implica a utilização de [funções de hash criptográficas](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash_criptogr%C3%A1fica), que permitem produzir um valor único para um conjunto de dados. Por sua vez, a preservação está relacionada ao estabelecimento de uma [**cadeia de custódia**](https://csrc.nist.gov/glossary/term/chain_of_custody), especialmente para evidências físicas (dispositivos físicos, discos rígidos, etc.), por meio de um registro e documentação de onde, como e quem acessou as evidências.

=== "4- Análise"

    Durante a análise, a pessoa analista utiliza ferramentas especializadas e investigações manuais para estudar e analisar as evidências, a fim de **estabelecer hipóteses e conclusões** sobre o que aconteceu. Em muitas  ocasiões, a pessoa analista se depara com grandes quantidades de informações, onde uma análise manual pode ser pouco eficaz e muito lenta, especialmente se não houver clareza sobre o que e onde procurar. Algumas ferramentas forenses podem facilitar o processo, especialmente se houver acesso a [**indicadores de comprometimento**](https://trustness.com.br/glossario/o-que-e-indicadores-de-comprometimento-ioc/). Durante esta etapa, é fundamental utilizar metodologias e procedimentos consistentes, que possam ser replicáveis e verificáveis. Em algumas ocasiões, não será possível estabelecer uma conclusão a partir das informações existentes.

=== "5- Apresentação"

    A última etapa de uma análise forense envolve preparar e apresentar as informações derivadas da análise. O objetivo e o público ao qual as informações serão apresentadas devem ser levados em consideração para determinar a melhor estrutura de conteúdo. Por exemplo, se for necessário preparar um relatório como parte de um processo judicial, o relatório deve ser detalhado e incluir informações que permitam verificar e reproduzir as descobertas. Por outro lado, se o relatório for para uso interno de uma organização e for dirigido à equipe de liderança, ele pode se concentrar nas conclusões e recomendações de remediação.



## Como a perícia digital é aplicada na prática da defesa dos direitos humanos

Na grande maioria dos casos, as pessoas e organizações que defendem os direitos humanos não dispõem de sistemas de monitoramento robustos que alertem sobre possíveis invasões em suas redes ou dispositivos. Portanto, é comum que **a detecção de um possível ataque ocorra quando as consequências de um incidente são percebidas**. Também não é comum que organizações da sociedade civil tenham pessoal especializado em segurança digital, de modo que as tarefas de resposta a incidentes frequentemente recaem sobre equipes internas de tecnologia ou comunicação, às vezes apoiadas por linhas de ajuda ou consultores externos.

Quando uma pessoa ou organização identifica um possível incidente, seja por meio de comportamento suspeito ou algum alerta (por exemplo, as [notificações de ameaças avançadas da Apple](https://support.apple.com/pt-br/102174.), a linha de ajuda ou o ponto de contato em segurança digital inicia um processo de investigação e [triagem](https://claveciberseguridad.com/resposta/triagem-de-incidentes-de-segurança-conceito-e-aplicação-eficaz/) para entender o que aconteceu, quando foi identificado e quais ações foram tomadas até aquele momento. **Desde estas primeiras etapas, é fundamental que a pessoa responsável pelo gerenciamento de incidentes, além de [avaliar o bem-estar emocional](https://vita-activa.org/2022/07/11/los-primeros-auxilios-psicologicos-en-7-claves/#:~:text=Os%20primeiros%20socorros%20psicológicos%20nos,ti%20misma%20y%20tus%20acciones.), incorpore práticas de perícia digital** que possam produzir evidências capazes de subsidiar mecanismos de responsabilização.

Como mencionado anteriormente, os processos de **resposta a incidentes e perícia digital estão intimamente interligados**. É durante a fase de triagem e resposta inicial que o gestor de incidentes identifica quais dispositivos, sistemas e contas podem conter evidências forenses relevantes para a investigação. Vale ressaltar que, em nosso contexto, as **investigações forenses devem sempre ser consentidas**, portanto, antes de coletar qualquer evidência, deve-se informar claramente à pessoa em risco quais ações podem ser tomadas, os riscos envolvidos e os resultados esperados, de forma que seja a pessoa em risco quem mantenha o controle e defina o curso da investigação.

Determinar exatamente o que coletar depende de muitos fatores, incluindo a vontade da pessoa em risco, o tipo de incidente, as ferramentas, recursos disponíveis e a capacidade técnica disponível.  Em algumas ocasiões, o gestor de incidentes realiza uma triagem e coleta inicial, que é apoiada por terceiros de confiança, que têm maior capacidade técnica para a detecção e atribuição de ataques. **Não é necessário ter um conhecimento técnico profundo para apoiar a coleta e o gerenciamento de evidências,** mas é muito útil compreender os conceitos e informações importantes incluídos neste documento.

Por exemplo, em algumas ocasiões, não é conveniente simplesmente desligar e enviar um dispositivo a um laboratório de confiança para análise posterior. Ao fazer isso, pode-se perder as **evidências voláteis**, ou seja, aquelas que são modificadas ou destruídas ao manipular ou desligar um dispositivo. Nesses casos, o mais conveniente é utilizar ferramentas forenses que permitam fazer uma **coleta ao vivo**, que permite extrair informações como listas de processos, arquivos temporários, entre outros.

!!! success "Boas práticas" 
    Durante todo o processo de atendimento, é de extrema importância manter uma documentação cronológica das ações realizadas e das evidências coletadas, incluindo hashes (identificadores únicos) que permitam uma verificação posterior.

Na maioria dos casos, as evidências não podem ser analisadas no local, sendo necessário utilizar ferramentas e processos especializados para tentar estabelecer conclusões sobre o que aconteceu. Essa **análise fria** geralmente é realizada em um laboratório forense, por pessoas com conhecimentos específicos. 

Em algumas ocasiões, **é possível que a análise forense não produza nenhum resultado imediato**, especialmente se for uma ameaça avançada, em que o invasor se esforçou para eliminar rastros como logs, arquivos ou metadados. Os atacantes também podem usar técnicas conhecidas como anti-forense, que têm como objetivo dificultar ou impedir a detecção e análise de evidências digitais. (https://trustness.com.br/glossario/o-que-e-ferramentas-anti-forense-e-sua-importancia/)

Além disso, **nem sempre se tem acesso a [inteligência de ameaças](https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_de_amea%C3%A7as_cibern%C3%A9ticas) robusta** que permite identificar e atribuir possíveis ataques. Não ser capaz de confirmar um comprometimento ou tentativa de comprometimento não significa que isso não tenha acontecido. Às vezes, investigações posteriores à análise inicial podem revelar novas linhas de estudo, pelo que pode ser valioso armazenar evidências forenses para análises posteriores, sempre em conformidade com as [políticas de segurança](https://protege.la/guias-contenido/diseno-politicas-protocolos-lineamientos/) e de retenção de informações, bem como com os acordos estabelecidos no consentimento informado.

Nos últimos anos, diferentes projetos e fundos que buscam incentivar a análise forense na sociedade civil permitiram impulsionar a criação de laboratórios de ameaças para apoiar defensores em todo o mundo. Isso permitiu que o ecossistema e suas capacidades se expandissem, especialmente no sul global. No entanto, **para o sucesso dessas iniciativas, é importante fomentar e promover a colaboração entre pares**, tanto dentro quanto fora da região, para compartilhar conhecimento e [inteligência sobre ameaças](https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_de_amea%C3%A7as_cibern%C3%A9ticas). **A criação de um laboratório forense é geralmente o primeiro passo em um processo de amadurecimento** que costuma levar anos, por isso a colaboração, especialmente nos estágios iniciais, é fundamental para acompanhar de forma positiva as pessoas em risco.

## Considerações importantes ao realizar investigações forenses

A seguir, detalhamos alguns aspectos importantes a serem considerados ao realizar investigações forenses em benefício de pessoas em risco da sociedade civil:

### Consentimento informado

Ao contrário das investigações forenses em outros contextos (periciais ou corporativos), as investigações forenses para pessoas defensoras dos direitos humanos **devem sempre ser consentidas**. Isso significa que o analista deve orientar e descrever o processo, para que a pessoa defensora compreenda em sua totalidade e possa tomar uma decisão informada sobre o andamento da investigação, seja por meio de um acordo verbal ou escrito.

É possível que alguns dos artefatos forenses coletados contenham informações pessoais (contatos, mensagens, aplicativos, entre outros), portanto, manter uma comunicação transparente e sempre respeitar as decisões da pessoa defensora deve ser sempre a prioridade. Alguns fatores importantes a serem levados em consideração para obter um consentimento informado incluem: quais informações devem ser coletadas, com quem serão compartilhadas, por quanto tempo serão armazenadas, entre outros.

[Consulta a guía práctica sobre consentimento informado](../../how-tos/01-how-to-obtain-informed-consent/){ .md-button }


### Cadeia de Custódia

O processo de documentar claramente quem e de que forma a evidência é manipulada é conhecido como **cadeia de custódia**. A evidência forense pode ser manipulada ou destruída durante o processo forense, pelo que a pessoa analista deve ser capaz de demonstrar a [integridade da evidência](https://www.ibm.com/br-pt/topics/data-integrity). Caso essa demonstração não seja possível ou suficientemente robusta, é possível que as evidências **não sejam admissíveis em processos judiciais** ou sejam refutadas e rejeitadas por outres especialistas.

!!! abstract "Consideração legal"
    Se a intenção é utilizar evidências forenses para processos judiciais, é recomendável consultar especialistas no âmbito legal local.

A melhor forma de demonstrar e verificar a integridade das evidências é por meio de **documentação** clara, que inclua hashes (identificadores únicos) e/ou [assinaturas digitais](https://oneflow.com/es/blog/pki-de-firma-digita/) dos arquivos coletados, bem como uma cronologia do processo, que permita entender claramente o manuseio das evidências desde sua identificação até a apresentação. Existem algumas empresas que prestam serviços para registrar e verificar a integridade das provas em conformidade com os marcos jurídicos, como por exemplo a [Verifact no Brasil](https://www.verifact.com.br/) 


### Riscos durante uma investigação forense

As investigações forenses podem expor abusos dos direitos humanos contra pessoas em risco por parte de Estados ou outros atores, por vezes com a cumplicidade de empresas fornecedoras de tecnologias de espionagem. Devido ao **impacto** que essas investigações podem ter, tanto para os **Estados quanto para as empresas com capacidades avançadas**, existe uma oposição e recursos para obstruir, paralisar e até criminalizar os esforços dos laboratórios de ameaças da sociedade civil.

É importante que, antes de iniciar uma prática forense, seja realizada uma **avaliação de riscos holística**, que considere tanto as pessoas analistas quanto aquelas que sofrem os ataques, a fim de estabelecer medidas de prevenção e resposta. Essa análise de riscos deve se concentrar não apenas em aspectos digitais, mas também legais e de segurança física. Algumas organizações que oferecem suporte para análise de riscos estão listadas no [site de primeiros socorros digitais](https://digitalfirstaid.org/support/).

Além disso, devido à natureza da prática forense, você estará frequentemente em contato com infraestruturas maliciosas, pelo que é fundamental definir medidas de [**segurança operacional**](https://es.ifixit.com/Wiki/OPSEC_and_Personal_Online_Security)**l** que protejam as pessoas analistas. Além dos riscos operacionais, deve-se avaliar o risco de alertar os invasores sobre uma investigação em andamento, o que poderia levar a uma mudança em sua infraestrutura e operação, reduzindo o sucesso da investigação.

[Consulta el explainer sobre riscos](../02-explainer-risks-threats/){ .md-button }

## Conclusão

A perícia digital envolve uma série de **práticas, metodologias, ferramentas, conhecimentos, técnicos e padrões** que, em conjunto, permitem estabelecer conclusões verificáveis sobre eventos relacionados a incidentes de segurança digital. No contexto da defesa dos direitos humanos, as evidências coletadas por meio de investigações forenses podem potencializar ações de responsabilização e incidência, contribuindo para a responsabilização de ataques digitais. 

A análise forense consentida envolve um **processo rigoroso com uma série de etapas**, onde se busca garantir e demonstrar a integridade das evidências e da análise realizada. A maioria das etapas, com exceção da fase de análise, não são tecnicamente complexas, mas requerem familiaridade com algumas ferramentas e um entendimento básico de conceitos como **cadeia de custódia** e **consentimento informado**. Os laboratórios e profissionais forenses também devem avaliar e tomar medidas para mitigar os riscos que possam surgir como resultado das investigações.

Em conjunto e através da confiança, laboratórios forenses emergentes e outros já estabelecidos podem colaborar para fortalecer a prática forense na sociedade civil. É através da colaboração entre pares que poderemos responder de forma holística às necessidades das pessoas defensoras em risco.


## Comentários

Tem comentários ou sugestões sobre este recurso? Você pode usar a função de comentários mostrada abaixo para deixar suas ideias ou observações. Por favor, certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct/). A função de comentários leva diretamente à seção de [Discussions do Github](https://github.com/Socialtic/forensics/discussions), onde você também pode participar das discussões de forma direta.



---
title: Explicador - Riscos e ameaças para laboratórios forenses da sociedade civil
summary: Riscos e ameaças enfrentados por pessoas analistas e laboratórios forenses da sociedade civil, e recursos para análises.
keywords: risco, ameaça, mitigação, análise de riscos
lang: pt-bt
tags: [explainer, intro]
last_updated: 2025-09-05
some_url:
comments: true
created: 2025-05-27
authors:
    - Daniel Bedoya
    - Gurshabad Grover
    - MariaLab
    - Data Privacy Brasil
    

---

# Explicador: Riscos e ameaças para laboratórios forenses da sociedade civil

Este documento faz **parte de um repositório de documentação técnica** que tem como objetivo estabelecer uma base de conhecimento comprovada, flexível e acessível para **impulsionar a análise forense consensual em benefício da sociedade civil**. Para organizar o conteúdo, é utilizado o [quadro de referência de documentação técnica Diataxis](https://diataxis.fr/).

Este recurso em particular se enquadra na categoria de [explainers](https://diataxis.fr/explanation/) e **descreve os riscos, ameaças e vulnerabilidades** que analistas e laboratórios forenses da sociedade civil enfrentam devido ao seu trabalho. É um material introdutório que inclui exemplos e links para recursos preventivos que podem ajudar a compreender e mitigar os riscos enfrentados.

A versão original deste documento foi elaborada em inglês pela equipe do SocialTIC em conjunto com a equipe do Internet Research Lab. A versão aqui em Português foi elaborada pela equipe do MariaLab e revisada pela equipe do Data Privacy Brasil. Qualquer erro ou omissão é de responsabilidade dos autores.


## Ameaças, vulnerabilidades e riscos: por que devemos prestar atenção?

No contexto da segurança digital para pessoas ou organizações em risco da sociedade civil, **uma ameaça** refere-se a eventos ou situações que possam colocar em risco ou prejudicar pessoas ou recursos, incluindo dispositivos e contas online. As ameaças podem ser de diferentes tipos (físicas, legais ou digitais) e ter diferentes causas (desastres naturais, roubos, ataques direcionados, etc.).

Por outro lado, uma **vulnerabilidade** refere-se a uma deficiência ou fraqueza em processos, sistemas, práticas ou hábitos que podem propiciar ameaças ou aumentar o impacto e as consequências de um incidente.

O **risco** resulta da combinação da possibilidade de uma ameaça se concretizar com a gravidade do impacto, caso ela venha a ocorrer. O risco não é um conceito estático; ele varia com o tempo, dependendo de fatores internos e externos, por isso, realizar exercícios regulares de análise de riscos é uma prática necessária para reduzir a probabilidade e a gravidade das ameaças.

No contexto da perícia forense para a sociedade civil, como descrevemos anteriormente em [nosso explicador sobre perícia forense para a defesa dos direitos humanos](../01-explainer-introduction-digital-forensics/), o processo de atendimento geralmente começa quando uma pessoa defensora dos direitos humanos se aproxima de um ponto de contato ou de um laboratório de ameaças para solicitar assistência. Em muitos casos, é possível que a pessoa se encontre em um **contexto de alto risco, exposta a ataques digitais, legais, físicos e psicossociais**.

Os riscos específicos que uma organização ou indivíduo enfrenta **dependem do contexto e do seu trabalho específico**. Embora o foco das investigações forenses não seja a contenção e mitigação de ameaças, **é essencial considerar o contexto de riscos** e evitar iniciar ações que possam levar a um aumento dos danos e impactos sofridos pela pessoa.
Este recurso se concentra principalmente nos *riscos para os laboratórios forenses* que apoiam defensores dos direitos humanos, mas é importante estender o exercício de análise a outros processos, serviços ou políticas que possam impactar o bem-estar das pessoas em risco.

Além disso, é importante que os laboratórios forenses, analistas e pontos de contato **também considerem os riscos aos quais seu pessoal e suas operações estão expostos ao se envolver em análises técnicas sensíveis.** Por meio dessas investigações, a sociedade civil busca promover ações de responsabilização que podem ter um impacto na indústria de vigilância, ao expor evidências de práticas ilegais ou antiéticas. Por esse motivo, **alguns atores da indústria podem considerar os analistas e pesquisadores da sociedade civil como uma ameaça**. 
Nas próximas seções, apresentaremos detalhes sobre os tipos de atores, ameaças e ataques que pesquisadores e laboratórios de ameaças sofreram no passado, bem como uma série de recursos para iniciar exercícios de análise de riscos.

## De onde vêm as ameaças?

Para saber exatamente de onde vêm as ameaças que um analista ou um laboratório de ameaças enfrenta em um determinado momento, é necessário realizar um [exercício de análise de risco](https://protege.la/guias-contenido/analisis-de-riesgos-como-evaluar-y-mitigar-riesgos-en-internet/). No entanto, é possível listar alguns atores de ameaças (threat actors) que foram identificados a partir de pesquisas anteriores: 

* **Empresas e comerciantes de spyware e ferramentas de vigilância**: Hoje, em 2025, podemos afirmar que existe um [amplo ecossistema de empresas](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf) que desenvolvem, comercializam e implementam tecnologias de vigilância, em sua maioria de capital privado e com fins lucrativos. Existem algumas listas dessas empresas, incluindo esta publicação do [Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/markets-matter-a-glance-into-the-spyware-industry/) ou [este recurso da organização Business and Human Rights](https://www.business-humanrights.org/pt/empresas/). Frequentemente, as empresas, fundadores ou funcionários têm ligações com o setor militar e de inteligência. Por exemplo, no caso da empresa NSO Group, [um dos cofundadores fazia parte da agência de inteligência israelense Mossad](https://en.wikipedia.org/wiki/NSO_Group#Founding). Em geral, são atores com capacidades técnicas, recursos financeiros, assessoria jurídica e, em alguns casos, conexões e influência política. As investigações da sociedade civil podem ter um impacto nos negócios e na reputação dessas empresas, como foi o caso da multa milionária imposta à NSO como parte da punição no caso WhatsApp vs. NSO (https://thehackernews.com/2025/05/nso-group-fined-168m-for-targeting-1400.html).html) ou o impacto sobre a empresa Cellebrite na sequência das investigações lideradas pela Amnistia Internacional (https://www.amnesty.org/en/latest/news/2025/02/cellebrite-halts-product-use-in-serbia-following-amnesty-surveillance-report/) na Sérvia e noutros países.

* **Atores estatais:** Em algumas ocasiões, os Estados, a polícia, os militares ou as agências de inteligência atuam como **operadores de tecnologias de vigilância**, o que significa que mantêm o controle sobre quem é atacado, quando, por quanto tempo e com que finalidade. Embora muitos governos dependam de ferramentas comerciais ou soluções de spyware mercenário, alguns Estados têm a capacidade de desenvolver sua própria tecnologia, com diferentes níveis de sofisticação técnica. A investigação forense por parte da sociedade civil pode levar à exposição de abusos e violações dos direitos humanos por parte dos Estados, e até mesmo à prestação de contas por meio de processos judiciais. Por isso, muitos atores dentro dos Estados buscam obscurecer, obstruir e até mesmo criminalizar a investigação forense da sociedade civil.

* **Trolls e atores de desinformação:** À medida que novos relatórios continuam expondo o uso indevido de tecnologias de vigilância, pelo menos desde 2022 surgiram [atores persistentes, especialmente nas redes sociais](https://www.cmu.edu/ideas-social-cybersecurity/events/syynimaa_attacking_ngo.pdf), que utilizam a desinformação e a pseudociência para desacreditar descobertas e investigações. Estas campanhas resultam em assédio a investigadores ou organizações e distraem os investigadores do seu trabalho. Em alguns contextos, especialmente onde existem [redes sólidas para a manipulação de algoritmos e discursos](https://cjp.org.in/india-among-nations-manipulating-social-media-oxford-study/), frequentemente surgem redes de trolls em conexão com eventos como notificações de ameaças, para espalhar desinformação e desacreditar esforços de investigação e prestação de contas.

* **Empresas de cibersegurança com fins lucrativos:** Nos últimos anos, surgiram algumas empresas privadas de cibersegurança que buscam lucrar com produtos voltados para detectar e prevenir infecções por spyware. Essas empresas, em algumas ocasiões, se aproximam da sociedade civil em busca de inteligência sobre ameaças ou indicadores de comprometimento, que lhes permitam avançar em suas investigações e produtos. Devido à diferença de incentivos e recursos, muitas vezes essas relações resultam em acordos extrativistas, que podem acabar prejudicando a reputação dos laboratórios forenses e, potencialmente, impactar as vítimas se suas informações não forem tratadas de forma responsável. Alguns exemplos específicos foram relatados de forma privada e até mesmo [algumas críticas e discussões públicas enfatizam o oportunismo e as práticas antiéticas de empresas como a iVerify](https://discuss.grapheneos.org/d/14993-debunking-fake-stock-pixel-os-vulnerability-from-an-edr-company).

## Exemplos de ameaças

Embora não seja possível compilar uma lista completa de todas as ameaças que um laboratório forense pode enfrentar, podemos partir de exemplos e relatórios anteriores para explorar alguns exemplos de ameaças que foram documentadas.

### Digitais

Por ataques digitais, nos referimos a ações ou comportamentos com intenção maliciosa, que utilizam tecnologias digitais. Por exemplo:

* **Phishing direcionado:**. O phishing direcionado refere-se a mensagens bem elaboradas, personalizadas com informações confidenciais ou sensíveis, que buscam que o destinatário abra links ou baixe anexos maliciosos. Essa técnica já foi usada anteriormente contra a sociedade civil. Por exemplo, em 2024, [o Citizen Lab e a Access Now documentaram como um agente avançado usou phishing direcionado](https://citizenlab.ca/2024/08/sophisticated-phishing-targets-russias-perceived-enemies-around-the-globe/) para comprometer contas de pesquisadores de alto perfil que estavam elaborando um relatório sobre corrupção e abuso de poder na Rússia.

* **Ataques de spyware**Já foram documentadas situações em que pesquisadores e ativistas da sociedade civil foram vítimas de ataques de spyware. Por exemplo, em 2024, a Access Now relatou (https://www.accessnow.org/publication/between-a-hack-and-a-hard-place-how-pegasus-spyware-crushes-civic-space-in-jordan/#who-was-hacked) que membros da Human Rights Watch (HRW) na Jordânia foram vítimas de spyware. O ataque ocorreu depois que a equipe da HRW divulgou um relatório criticando a repressão por parte do governo.

* **Doxxing (doxing ou doxeo)**: O doxxing consiste na coleta e publicação de informações sensíveis e confidenciais sobre uma pessoa, como seu endereço físico ou número de telefone, especialmente utilizando fontes abertas de informação disponíveis na Internet (OSINT, ou [inteligência de fontes abertas](https://pt.wikipedia.org/wiki/OSINT)). Embora existam poucos relatos públicos sobre doxing contra pessoas analistas ou laboratórios forenses, vários casos foram relatados de forma privada.

* **Comprometimento ou vazamento de informações**. Os adversários podem tentar obter acesso a informações confidenciais, como a identidade das vítimas que buscam apoio ou informações sobre infraestrutura, vulnerabilidades ou indicadores de comprometimento que não são públicos. Além disso, os adversários podem tentar obter acesso a informações confidenciais sobre o pessoal do laboratório forense, especialmente se as investigações tiverem sido realizadas através do uso de pseudônimos ou nomes falsos. É importante ter em mente que os ataques também podem ser direcionados a prestadores de serviços, como sistemas de gerenciamento de casos ou armazenamento de informações na nuvem. Em 2022, foi relatado um ataque contra o Comitê Internacional da Cruz Vermelha (IRCC) que [comprometeu registros confidenciais após um comprometimento em um provedor de serviços utilizado pela organização](https://www.theregister.com/2022/01/20/red_cross_hit_by_cyberattack/).

### Legais

Os ataques legais podem ocorrer quando os Estados utilizam leis de segurança nacional ou cibersegurança para criminalizar as ações e atividades de pessoas analistas e laboratórios forenses. Também é possível que ameaças legais sejam apresentadas por empresas de spyware como parte de processos judiciais. 

* **Criminalização das investigações forense:** Em 2019, no Equador, o investigador Ola Bini foi [preso e acusado de crimes previstos na lei de crimes cibernéticos](https://www.eff.org/deeplinks/2023/03/aftermath-ola-binis-unanimous-acquittal-ecuadorian-court). Ola foi parte de um extenso processo legal, repleto de erros, e apesar de ter sido absolvido de todas as acusações em 2023, ainda [continua lutando com recursos e procedimentos legais.](https://peoplesdispatch.org/2024/04/08/activist-ola-bini-sentenced-to-one-year-in-prison-after-ecuadorian-court-overturns-acquittal/)

* **Guerra jurídica (lawfare)**: Refere-se ao uso do sistema ou de instituições jurídicas para prejudicar, desacreditar ou afetar indivíduos ou organizações. Por exemplo, em relação ao caso nos tribunais dos Estados Unidos entre a NSO e o WhatsApp, o Citizen Lab enfrentou uma série de recursos e solicitações legais que buscavam desmantelar seu trabalho e acessar informações confidenciais, incluindo a lista de vítimas. Em outro exemplo, em 2018, a empresa canadense Sandvine ameaçou o Citizen Lab com um processo por difamação devido à sua publicação sobre o uso de equipamentos Sandvine para a implantação de spyware.

* **Intimações e solicitações de dados:** Alinhado com as tentativas de criminalizar a pesquisa, é possível que as autoridades tentem usar processos legais, intimações e outros mecanismos para obter informações pessoais de pesquisadores ou laboratórios forenses. Por exemplo, em 2019, o pesquisador argentino Javier Smaldone tornou [públicos os pedidos de dados feitos pela polícia a provedores de internet e prestadores de serviços](  https://blog.smaldone.com.ar/2021/01/31/los-sotanos-de-la-policia-federal-argentina) (incluindo o WhatsApp).

### Reputacionais

Os laboratórios forenses também podem sofrer uma série de ameaças à sua reputação, às vezes por meio de afirmações infundadas ou campanhas de desinformação. Trolls e redes de manipulação de informação podem propagar e ecoar essas campanhas em um esforço para desacreditar resultados e minar os apelos à responsabilização. 

* **Publicações e pseudociência:** Pseudociência refere-se a afirmações, crenças ou práticas que se dizem científicas e verificáveis, mas que na verdade não são compatíveis com o método científico. Anteriormente, investigações do Citizen Lab e da Anistia Internacional foram criticadas por “especialistas” em segurança cibernética, o que gerou perturbações em seu trabalho. Exemplos incluem [perfis nas redes sociais que tentaram desacreditar a investigação do Citizen Lab #CatalanGate](https://medium.com/@maldr0id/misinformation-in-malware-analysis-232c7bb6b73e). 

### Físicas

Os ataques ou ameaças físicas visam intimidar e desencorajar o uso da ciência forense para investigações na sociedade civil.

* **Assédio e vigilância física:** Em 2020, o jornal [New York Times publicou um artigo relatando um caso de assédio e vigilância contra um investigador do Citizen Lab](https://www.nytimes.com/2019/01/28/world/black-cube-nso-citizen-lab-intelligence.html) por parte de um espião israelense. 

* **Detenções, buscas e prisões:** Como mencionado anteriormente, diferentes leis podem ser utilizadas para criminalizar as investigações forenses, incluindo leis de cibersegurança e segurança nacional. Através da aplicação excessiva e direcionada dessas leis, os esforços de investigação forense podem ser criminalizados e detidos. Por exemplo, em 2019, o investigador argentino [Javier Smaldone foi vítima de detenções simplesmente por criticar a segurança das máquinas de votação eletrônica].

### Psicossociais

Analistas e laboratórios forenses também sofrem consequências para seu bem-estar emocional devido ao apoio que prestam a pessoas em risco de serem vítimas de spyware. Este relatório da Access Now descreve o impacto psicológico que enfrentam as pessoas vítimas de spyware, que geralmente requerem apoio emocional e contenção, frequentemente dos pontos de contato ou linhas de ajuda da sociedade civil. 

* **Fadiga da compaixão ou trauma secundário:** [A fadiga da compaixão](https://www.unir.net/revista/salud/fatiga-por-compasion/) ou [trauma secundário](https://en.wikipedia.org/wiki/Secondary_trauma#cite_note-Cieslak_2014-1) referem-se a traumas psicológicos que surgem devido ao contato com uma pessoa que passou por um evento traumático (como a infecção de seus dispositivos com spyware).

* **Síndrome de desgaste profissional (burnout)**: [A síndrome de desgaste profissional](https://pt.wikipedia.org/wiki/S%C3%ADndrome_de_burnout) ou burnout é um estado crônico de estresse que leva a sofrimentos físicos e desgaste emocional, gerando sentimentos de cinismo, desapego e ineficácia. O esgotamento pode incapacitar uma pessoa no nível profissional. Quem sofre de esgotamento pode precisar de tempo livre adicional para recuperar a saúde física e mental ou, em determinadas situações, pode não ser capaz de se reintegrar às suas tarefas habituais.

### Operacionais

Além das possíveis ameaças digitais, físicas, legais e psicossociais, é importante ter em mente os riscos relacionados à parte operacional e à sustentabilidade dos laboratórios forenses.

* **Sustentabilidade e acesso a recursos:** A prestação de serviços de análise forense requer uma combinação de conhecimento técnico, acesso a ferramentas, experiência e procedimentos. Normalmente, os laboratórios forenses passam por um processo de amadurecimento que geralmente leva vários anos. Portanto, é importante que os laboratórios forenses considerem uma estratégia para sua sustentabilidade, especialmente enquanto desenvolvem e fortalecem as habilidades necessárias para realizar investigações forenses. 

* **Retenção de pessoal:** Existe uma [escassez de pessoal técnico](https://www.weforum.org/stories/2024/04/cybersecurity-industry-talent-shortage-new-report/) com conhecimentos em segurança digital e, em particular, com experiência em ciências forenses. A sociedade civil não é exceção, e várias organizações e laboratórios de ameaças têm enfrentado desafios na contratação e retenção de pessoal técnico qualificado que tenha a sensibilidade necessária para trabalhar com pessoas em risco. Também deve ser levado em consideração o risco de que estas pessoas técnicas busquem oportunidades melhor remuneradas no setor privado.

* **Resiliência de Infraestrutura e serviços**: O trabalho dos laboratórios forenses é afetado por eventos e fatores externos, como um aumento no número de solicitações após uma crise social ou política. Por exemplo, já foram relatados aumentos no número de solicitações após publicações virais nas redes sociais, levando a contatos em massa para linhas de assistência ou serviços de apoio, o que acaba sobrecarregando e impedindo a prestação de serviços. É importante explorar esse tipo de cenário para desenvolver planos de contingência e infraestrutura resiliente. 


## Prevenção e gerenciamento de riscos

Como mencionamos ao longo deste recurso, incentivamos as pessoas analistas e laboratórios forenses que apoiam pessoas em risco da sociedade civil a realizar exercícios de avaliação de riscos regularmente, especialmente antes de iniciar investigações com pessoas em contextos de alto risco. 
Este recurso **não é um guia passo a passo para realizar uma análise de riscos**, no entanto, fornecemos links para diferentes recursos e organizações próximas que podem oferecer assistência para prevenir diferentes tipos de ameaças.

### Recursos para análise de riscos

A seguir estão alguns recursos para iniciar exercícios de análise de riscos: 

* [Cybersecurity Assessment Tool (CAT)](https://cybercat.tools/#assessment): A ferramenta de diagnóstico de segurança cibernética, ou CAT, é uma ferramenta projetada para medir o nível de maturidade, resiliência e força de uma organização em relação à sua segurança cibernética. Ela pode ajudar laboratórios de ameaças, ou as organizações onde estes estão hospedados, a identificar seus próprios riscos, ameaças, vulnerabilidades e oportunidades. 

* [SAFETAG](https://safetag.org/): SAFETAG é uma abordagem de auditoria para a sociedade civil que adapta modelos tradicionais de testes de penetração e análise de riscos para que sejam úteis e práticos para pequenas e médias organizações da sociedade civil.

* [Plano de segurança (EFF)](https://ssd.eff.org/module/your-security-plan): A EFF disponibiliza um recurso em suas diretrizes de SSD voltado especificamente para indivíduos ou pessoas analistas independentes para criar um plano para gerenciar riscos digitais.

### Organizações e redes de apoio

A seguir, apresentamos uma lista de organizações que podem ajudar na análise, mitigação e gestão de diferentes tipos de riscos:

**Digitais ou técnicos**

* [Access Now Digital Security Helpline](http://accessnow.org/help)
* [Cyber hub](https://cyberhub.am/en/)
* [SocialTIC](https://socialtic.org/)
* [Frontline Defenders](https://www.frontlinedefenders.org/)
* [Open briefing](https://openbriefing.org/)

**Jurídico**

* [Media Legal Defense Initiative](https://www.rcmediafreedom.eu/Tools/Support-centres/Media-Legal-Defence-Initiative-MLDI) 
* [Access Now](http://accessnow.org/help)
* [Artigo 19](https://artigo19.org/) (Brasil) - [comunicacao@artigo19.org](mailto:comunicacao@artigo19.org)
* [Data Privacy](https://dataprivacy.com.br/) (Brasil) - [atendimento@dataprivacy.com.br)](mailto:atendimento@dataprivacy.com.br))

**Psicossocial e bem-estar**

* [Linha de atendimento feminista da vita activa](https://vita-activa.org/) 
* Entre seus recursos, estão práticas para [lidar com o trauma indireto](https://vita-activa.org/2021/02/08/trauma-indirecto/) e recursos sobre a síndrome do [esgotamento profissional e como ela afeta mais as mulheres](https://vita-activa.org/2022/03/15/el-burnout-por-que-afecta-mas-a-las-mujeres/).
* [Open briefing](https://openbriefing.org/)
* Entre seus recursos estão uma [ferramenta para análise de riscos](https://www.openbriefing.org/services/security/risk-assessments/) e um recurso sobre [fadiga da compaixão e trauma vicário em pessoas que apoiam defensores dos direitos humanos](https://openbriefing.org/resources/compassion-fatigue-vicarious-trauma-and-burnout-infosheet-for-those-supporting-human-rights-defenders/). 

**Segurança física**

* [Frontline Defenders](https://www.frontlinedefenders.org/)

**Sustentabilidade** 

* [Engine Room](https://www.theengineroom.org/)
* Seus recursos incluem um [material sobre remuneração em equipes remotas globais](https://www.theengineroom.org/library/rethinking-compensation-for-a-global-remote-team/), bem como um relatório sobre [como identificar fontes sustentáveis de financiamento](https://www.theengineroom.org/library/tipping-the-scales-what-it-takes-to-fund-an-equitable-tech-human-rights-ecosystem/). 


**Recursos para responder a incidentes**

* [Linhas de apoio feministas](https://feministhelplines.org/) 
* [DFAK](https://digitalfirstaid.org/) \- Kit de primeiros socorros digitais
* 
## Conclusão

Através deste documento, apresentamos uma descrição dos atores de ameaças e dos riscos que as pessoas analistas e laboratórios forenses da sociedade civil enfrentam devido ao seu trabalho. Existe um amplo ecossistema de atores de ameaças que buscam impedir ou dificultar os esforços de análise forense. Recomendamos iniciar exercícios individuais de análise de riscos, especialmente antes de iniciar investigações em contextos de alto risco.

Nossa intenção com este documento não é minimizar ou minar os esforços emergentes para realizar mais análises forenses a partir da sociedade civil. Pelo contrário, destacamos a importância de implementar práticas e políticas de segurança operacional de forma que as investigações sejam iniciadas de maneira responsável e sem aumentar o risco para pessoas que já se encontram em situações vulneráveis.

**Convidamos você a colaborar com a documentação neste repositório**. Se você tiver alguma observação ou solicitação, pode fazê-la através da [seção de problemas (issues) do repositório](https://github.com/Socialtic/forensics/issues). Se você tiver recursos que deseja integrar a este repositório documental, escreva para [seguridad@socialtic.org](mailto:seguridad@socialtic.org).


## Comentários

Tem comentários ou sugestões sobre este recurso? Você pode usar a função de comentários mostrada abaixo para deixar suas ideias ou observações. Por favor, certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct/). A função de comentários leva diretamente à seção de [Discussions do Github](https://github.com/Socialtic/forensics/discussions), onde você também pode participar das discussões de forma direta.





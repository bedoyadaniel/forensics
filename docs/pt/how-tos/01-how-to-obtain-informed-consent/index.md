---
title: Como obter e documentar um consentimento informado para uma investigação forense?
summary: Guia prático sobre consentimento informado, o que é, como obtê-lo e como documentá-lo. 
keywords: consentimento, consentimento informado, investigação forense com consentimento
lang: pt-br
tags: [how-to, intro]
last_updated: 2025-09-05
some_url:
created: 2025-03-14
comments: true
authors:
    name: Daniel Bedoya
    name: MariaLab
    name: Data Privacy Brasil

---

# Como obter um consentimento informado para uma investigação forense?

Este documento faz parte de um repositório de documentação técnica que tem como objetivo estabelecer uma base de conhecimento comprovada, flexível e acessível para impulsionar a análise forense consentida em benefício da sociedade civil. Para organizar os conteúdos, é utilizado o [quadro de referência de documentação técnica Diataxis](https://diataxis.fr/). 

O presente documento é classificado como um [guia prático](https://diataxis.fr/how-to-guides/). Descreve o que é o **consentimento informado no contexto de investigações forenses para a defesa dos direitos humanos** e apresenta um rascunho que pode ser utilizado por pontos de contato, analistas e laboratórios forenses para obter e registrar o consentimento durante uma investigação.


!!! abstract "Consideração Legal"
    Este guia **não detalha o procedimento da cadeia de custódia.** Este importante processo será descrito mais adiante em um material diferente. 


Agradecemos as referências e revisões da comunidade de prática que permitiram a elaboração deste documento.

##  O que é consentimento informado e por que é importante?

O [consentimento](https://es.wikipedia.org/wiki/Consentimiento) é um princípio que se refere à exteriorização da vontade entre duas ou mais pessoas para aceitar direitos e obrigações. No contexto da análise forense digital para pessoas da sociedade civil, o consentimento informado refere-se ao **acordo e aprovação de ações para facilitar a coleta, análise, apresentação e preservação de evidências digitais**.
 
Um aspecto fundamental em qualquer acordo de consentimento é a capacidade de quem aceita o acordo de tomar uma **decisão informada** sobre o curso da investigação e até mesmo de recusar a assistência. Na prática forense, isso significa fornecer todas as informações necessárias para que quem solicita a análise compreenda as ações, riscos, direitos e obrigações inerentes ao processo de investigação. É importante que a pessoa analista se comunique de forma clara e transparente e respeite a vontade de quem solicita o apoio. 

Durante uma investigação forense, a pessoa analista deve coletar e analisar as evidências, bem como apresentar os resultados de sua análise. Os [artefatos forenses](https://www.sec2crime.com/2021/11/01/los-artifacts-en-la-informatica-forense/) coletados podem conter informações pessoais (contatos, arquivos, fotografias, etc.) que podem acarretar riscos se forem manuseados de forma inadequada. Além disso, essas informações podem estar sujeitas a normas de proteção de informações ([LGPD](https://pt.wikipedia.org/wiki/Lei_Geral_de_Prote%C3%A7%C3%A3o_de_Dados_Pessoais), por exemplo) e, além da regulamentação existente, exigem um tratamento responsável, idealmente apoiado por políticas de gestão, proteção e retenção de informações (https://protege.la/guias-contenido/diseno-politicas-protocolos-lineamientos/).** 

!!! abstract “Consideração Legal”
    Os dados coletados estarão sujeitos à legislação para proteção e tratamento de informações da **jurisdição local de residência da pessoa que receberá o diagnóstico forense.**

No Brasil, podemos nos basear nos artigos **3 e 4 da LGPD**, a seguir:

* Art. 3º Esta Lei aplica-se a qualquer operação de tratamento realizada por pessoa natural ou por pessoa jurídica de direito público ou privado, independentemente do meio, do país de sua sede ou do país onde estejam localizados os dados, desde que:
    - I - a operação de tratamento seja realizada no território nacional;
    - II - a atividade de tratamento tenha por objetivo a oferta ou o fornecimento de bens ou serviços ou o tratamento de dados de indivíduos localizados no território nacional; ou [(Redação dada pela Lei nº 13.853, de 2019)](https://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2019/Lei/L13853.htm#art2) [Vigência](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art65)
    - III - os dados pessoais objeto do tratamento tenham sido coletados no território nacional.
* Art. 4º Esta Lei não se aplica ao tratamento de dados pessoais:
    - IV - provenientes de fora do território nacional e que não sejam objeto de comunicação, uso compartilhado de dados com agentes de tratamento brasileiros ou objeto de transferência internacional de dados com outro país que não o de proveniência, desde que o país de proveniência proporcione grau de proteção de dados pessoais adequado ao previsto nesta Lei.


Dependendo da abordagem da organização que presta o apoio e da natureza da investigação, existem diferentes alternativas para a **apresentação dos resultados da análise**. Em geral, através da prática forense, pretende-se chegar a processos de responsabilização que envolvem **ações de incidência, tais como relatórios, campanhas, litígios, entre outros**. Essas ações podem **acarretar consequências e riscos**, tanto para a organização que realiza a análise quanto para a pessoa afetada pelo ataque. Alguns riscos incluem, por exemplo, perseguição legal, assédio e represálias adicionais por parte de governos ou empresas desenvolvedoras de tecnologias de vigilância.
 
Mesmo em situações em que não se pretende publicar resultados ou entrar em litígios, existe um risco e uma responsabilidade ao coletar informações para uma investigação forense. Portanto, é importante que ambas as partes (quem analisa e quem solicita a análise) identifiquem e estabeleçam **acordos sobre a coleta e o manuseio das informações**, de forma a aceitar e minimizar os riscos que possam surgir em decorrência da investigação forense.

Embora seja a pessoa que solicita a análise quem decide de maneira informada quais informações está disposta a compartilhar, bem como o curso da investigação, **é importante que a organização que realiza a análise também compartilhe expectativas, políticas e termos de uso da assistência prestada.** Alguns exemplos de termos de serviço incluem os termos da [Linha de Ajuda da Access Now](https://www.accessnow.org/helpline-terms-of-service/) e a [política de privacidade da Amnesty Tech](https://securitylab.amnesty.org/privacy-policy/).

## Origem e aplicação do consentimento informado em investigações forenses consentidas

O consentimento informado não é uma prática exclusiva da perícia digital. É frequentemente utilizado em áreas como medicina, jornalismo ou mesmo atividades recreativas de alto risco, quando, por **princípios éticos ou legais**, é necessário que uma pessoa compreenda os riscos a que se expõe antes de aceitar participar em alguma atividade. Exemplos incluem iniciar um tratamento médico, participar num estudo farmacológico e até mesmo saltar de paraquedas.
 
Compreender as possíveis consequências da ação é importante em todos os contextos. Na medicina, por exemplo, obter um consentimento informado implica fornecer ao paciente informações pertinentes sobre os riscos e benefícios do tratamento, alternativas, qual é o papel tanto do paciente quanto da equipe médica e o direito de recusar o tratamento. É responsabilidade ética e legal do profissional médico garantir que o consentimento seja realmente informado.
Ao realizar uma **investigação forense em benefício de uma pessoa da sociedade civil**, o processo de consentimento tem como objetivo fornecer informações claras sobre aspectos da investigação, tais como:
 
* Que informações ou dispositivos serão recolhidos? Que [informações pessoais](https://es.wikipedia.org/wiki/Informaci%C3%B3n_personal) estão incluídas nessa coleta?
* O que acontecerá durante a investigação?
* Com quem essas informações serão compartilhadas?
* Quais são os possíveis riscos da investigação forense?
* Quais resultados podem ser esperados?
* É permitido mencionar publicamente o nome da pessoa em risco em ações de incidência ou prestação de contas? É permitido mencionar de forma anônima?
* Por quanto tempo as informações coletadas serão armazenadas?

**Idealmente, o consentimento deve ser solicitado antes da coleta de evidências.** **Muitas das perguntas são discutidas verbalmente durante as etapas iniciais de uma investigação, mas é recomendável considerar um documento escrito que inclua alguns dos acordos principais.** Embora o consentimento informado faça parte da responsabilidade ética e legal de quem realiza a análise, é também uma oportunidade para esclarecer dúvidas e garantir que quem solicita a análise compreenda o processo e os riscos, de forma a ter a autonomia necessária para decidir o curso da investigação. 

Deve-se levar em consideração que muitas das pessoas que solicitam assistência estão **imersas em contextos de alto risco**, portanto, estabelecer uma relação de confiança baseada na **transparência e na escuta ativa** é fundamental. O [manual de primeiros socorros psicológicos da organização Vita Activa](https://vita-activa.org/wp-content/uploads/2025/01/Vita-Booklet-Final.pdf) inclui uma seção sobre como realizar **entrevistas empáticas** que permitem atender às necessidades mais imediatas de quem solicita apoio.
 
Tenha em consideração que apresentar um documento com linguagem jurídica e uma descrição dos riscos adicionais **pode causar angústia e preocupação**. A prioridade durante uma análise forense consentida deve ser o **bem-estar da pessoa que presta apoio**. Certifique-se de esclarecer dúvidas e tente gerar confiança e clareza sobre o procedimento que será realizado.
 
Na seção a seguir, apresentamos um **modelo de carta de consentimento informado** que pode ser **adaptado de acordo com as necessidades e particularidades da investigação forense**. Incluímos um passo a passo de como adaptar o documento e algumas considerações para sua aplicação.

## Como gerar um documento de consentimento informado?

Para gerar uma carta de consentimento a partir do modelo proposto, siga as seguintes etapas: 

1- **Baixe** o [rascunho da carta de consentimento informado](../../assets/01-how-to/exemplo-pt-br-carta-de-consentimento-para-analise-forense_BRASIL.odt). O formato utiliza campos de formulário, de forma que, ao converter para PDF, possa ser preenchido facilmente.

![captura da carta de consentimento](../../../es/assets/01-how-to/carta-de-consentimiento.png "Carta de consentimento")

Nos links a seguir, você pode **baixar o rascunho da carta de consentimento** em diferentes formatos:

* [Carta de consentimento em ODT](../../assets/01-how-to/exemplo-pt-br-carta-de-consentimento-para-analise-forense-odt.odt)
* [Rascunho da carta de consentimento em Google docs (ESPAÑOL)](https://docs.google.com/document/d/1YPiMO7WuGwE7hMHLZ9VPQkTLALN_bhmL0DASaZn3r2A/template/preview). 


2- **Preencha e verifique** as seções destacadas em amarelo: 

* **Nome da organização**: Inclua o nome da organização que realizará a análise forense
* **Objetivo da investigação**: Ajuste o objetivo, conforme necessário, indicando claramente quais ações serão realizadas durante a investigação forense e com qual finalidade.
* **Consentimento para publicar:** Se o objetivo for publicar os resultados da investigação, mantenha e ajuste o texto correspondente para obter o consentimento necessário. Se você não tem intenção de publicar os resultados, exclua esta seção. 
* **Detalhes das informações a serem coletadas**: Detalhe as [informações que serão coletadas](#quais-informações-sensíveis-são-coletadas-durante-uma-análise-forense?) para a análise forense, dependendo do tipo de dispositivo e processo de aquisição.
* **Link para a política de tratamento de dados:** Se houver, inclua o link para a política de tratamento de dados. **Esclareça se as informações serão compartilhadas com terceiros.**
 Veja esse exemplo da MariaLab de [política de privacidade e tratamento de dados adequados à LGPD](https://www.marialab.org/politica-de-privacidade/).
* **Confidencialidade da investigação**: Especifique se a participação na investigação será uma informação confidencial, de forma que quem solicita a análise compreenda que não será compartilhados detalhes sobre a análise.

3- **Converta o documento em formato PDF e compartilhe-o** com a pessoa que solicita a análise. Idealmente, o consentimento deve ser solicitado após uma conversa inicial de triagem, onde são esclarecidas dúvidas e determinados os escopos da pesquisa. 

4- **Solicite à pessoa que solicita a análise que revise e preencha o documento.** Esclareça quaisquer dúvidas que surjam da leitura do documento e solicite sua assinatura. Se for pertinente, você também pode considerar serviços de assinatura de documentos online (como [DocuSign](https://www.docusign.com/), [Dropbox Sign](https://sign.dropbox.com/), [Gov.br](https://www.gov.br/pt-br/servicos/assinatura-eletronica). Sistemas de assinatura eletrônica de chave pública (como [PGP](https://es.wikipedia.org/wiki/Pretty_Good_Privacy), [OpenSSL](https://es.wikipedia.org/wiki/OpenSSL) ou assinaturas digitais nacionais) também são úteis para garantir a integridade de um documento assinado. 

5- Assim que receber o documento de consentimento, verifique se todos os campos estão preenchidos e armazene-o de acordo com as políticas de segurança da informação existentes. Leve em consideração qualquer **acordo sobre retenção de dados para determinar por quanto tempo armazenar os artefatos forenses**. 

## Quais informações confidenciais são coletadas durante uma análise forense? 

As informações precisas a serem coletadas **dependerão das particularidades de cada caso e serão determinadas pela pessoa analista forense**.

A seguir, estão listados os **artefatos forenses que normalmente são coletados** em diferentes tipos de análises de dispositivos móveis, bem como as informações que geralmente incluem para Android/Google e iOS/Apple.

### Android

* [Google Takeout](https://olhardigital.com.br/2022/07/20/dicas-e-tutoriais/o-que-e-e-como-usar-o-google-takeout/): O Google Takeout (disponível em [takeout.google.com](http://takeout.google.com)) permite selecionar dados a serem exportados sobre diferentes produtos do Google, incluindo **informações de acesso à conta do Google, informações de download de aplicativos da PlayStore, informações sobre o registro e atividade da conta, mensagens, entre outros**. A lista é extensa, por isso é recomendável solicitar pontualmente o que for necessário para a análise e evitar extrair informações que contenham fotografias, e-mails ou outros dados pessoais não relevantes. Ao solicitar e documentar o consentimento, esclareça o que será solicitado ao Google Takeout e o tipo de informação incluída.

* [Relatório de erros do Android](https://developer.android.com/studio/debug/bug-report?hl=es-419): O “relatório de erros” é um arquivo gerado pelo sistema operacional Android para ajudar a encontrar e diagnosticar erros nos aplicativos e no sistema operacional. **Em geral, não incluem [dados pessoais](https://www.tre-pr.jus.br/transparencia-e-prestacao-de-contas/lei-geral-de-protecao-de-dados/o-que-sao-dados-pessoais)**, mas incluem informações sobre aplicativos instalados no dispositivo, informação sobre redes Wi-Fi e arquivos de log que podem descrever ações realizadas pelo usuário ou pelo sistema.

* [Aquisição do AndroidQF](https://github.com/mvt-project/androidqf): O AndroidQF permite extrair informações de um dispositivo Android para realizar uma análise forense. **A maioria dos arquivos coletados não contém informações confidenciais,** mas, opcionalmente, é possível gerar uma cópia das mensagens SMS e MMS. Especificamente, ele coleta configurações do sistema, lista de processos, lista de serviços, cópia de logs, lista de aplicativos instalados, lista de arquivos do sistema e cópia dos arquivos temporários. Opcionalmente, também é possível exportar uma cópia dos aplicativos instalados. 

### iOS

* [Arquivos de diagnóstico](https://it-training.apple.com/tutorials/support/sup075/): Os arquivos de diagnóstico do iOS incluem informações que podem ser úteis para identificar e resolver problemas no dispositivo, como logs do sistema operacional, relatórios de erros, informações sobre os aplicativos instalados, detalhes sobre a versão do hardware e do sistema operacional, entre outros. **Em geral, não inclui [dados pessoais](https://www.tre-pr.jus.br/transparencia-e-prestacao-de-contas/lei-geral-de-protecao-de-dados/o-que-sao-dados-pessoais)**, mas alguns arquivos podem conter detalhes como e-mail, nome de usuário, localização ou detalhes sobre o uso de aplicativos.
 
* [Backup](https://support.apple.com/en-us/108771): Os arquivos de backup permitem fazer uma cópia das informações incluídas em um dispositivo iOS. **Por padrão, inclui informações confidenciais**, como fotos, mensagens, dados do Apple Mail, contatos, calendários, notas, entre outros. Recomenda-se usar ou implementar soluções que reduzam as informações confidenciais após a extração e antes do compartilhamento.

## Consideraciones importantes al obtener el consentimiento

Ao solicitar e obter consentimento para realizar investigações forenses, leve em consideração o seguinte:

- **Proteção e tratamento de dados pessoais**: Durante uma investigação forense, é possível que a pessoa analista adquira, armazene e analise informações confidenciais, que podem incluir mensagens, contatos, listas de aplicativos, entre outros. **Além das responsabilidades legais sobre proteção de informações, devem ser implementados processos e políticas que reduzam e protejam essas informações e garantam o cumprimento dos acordos estabelecidos no formulário de consentimento**. Caso não existam, é recomendável que os laboratórios forenses [desenvolvam políticas sobre o tratamento de informações](https://protege.la/guias-contenido/diseno-politicas-protocolos-lineamientos/) (por exemplo, a [política de tratamento de informações da CiviCERT](https://www.civicert.org/civicert-information-management-policy/)), que orientem a atuação durante a investigação forense e deem clareza a quem solicita a análise.

- **Revisão jurídica:** As informações incluídas neste documento, bem como o rascunho proposto, têm como objetivo servir de orientação para que organizações da sociedade civil possam implementar processos de consentimento prévio à conclusão da análise forense. No entanto, pode não ser adequada ou suficiente em contextos específicos. Caso tenha acesso a aconselhamento jurídico, é recomendável discutir o processo e o formulário com especialistas, que possam ajustar e ampliar o escopo conforme necessário. Algumas organizações que podem oferecer apoio jurídico incluem:
 
- [Hiperderecho](https://hiperderecho.org/contacto/) (Peru, América Latina) - [hola@hiperderecho.org](mailto:hola@hiperderecho.org)
- [Access Now Helpline](https://accessnow.org/help) (Global) - [help@accessnow.org](mailto:help@accessnow.org) (Solicite para ser conectado com o Tech Legal Counsel ou laboratório forense)
- [Artigo 19](https://artigo19.org/) (Brasil) - [comunicacao@artigo19.org](mailto:comunicacao@artigo19.org)
- [Data Privacy](https://dataprivacy.com.br/) (Brasil) - [atendimento@dataprivacy.com.br)](mailto:atendimento@dataprivacy.com.br))


## Conclusión

**O objetivo do consentimento informado é proporcionar transparência e clareza, de forma que quem solicita a análise possa decidir o alcance e o curso da investigação**, levando em consideração os possíveis riscos. Além da documentação do consentimento, é importante que a pessoa analista apresente (verbalmente ou por escrito) informações claras sobre o processo de análise, incluindo quais informações serão coletadas, quais dados sensíveis estão incluídos nessas informações, quais resultados podem ser esperados do processo, com quem as informações adquiridas serão compartilhadas, por quanto tempo serão armazenadas, entre outros.
 

Durante o processo de consentimento, também são reconhecidos e aceitos os riscos inerentes a uma investigação forense. Além de concordar com esses riscos, **é importante que a organização que realiza a coleta e a análise – e qualquer outra organização com quem os dados sejam compartilhados – trate as informações de maneira responsável**, em conformidade com as políticas de proteção e retenção de dados.


## Comentários

Tem comentários ou sugestões sobre este recurso? Você pode usar a função de comentários mostrada abaixo para deixar suas ideias ou observações. Por favor, certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct/). A função de comentários leva diretamente à seção de [Discussions do Github](https://github.com/Socialtic/forensics/discussions), onde você também pode participar das discussões de forma direta.



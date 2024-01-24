## Atividade didática - Curso de Análise de Dados em Python - Zênite Serena - Banco de Dados

### Contextualização

Atividade que fez parte do bootcamp "Python: Fundamentos e Análise de Dados" da [{reprograma}](https://reprograma.com.br/curso-python/), realizado no segundo semestre de 2023. A presente atividade foi realizada na Semana 10 do curso.

[Repositório no GitHub](https://github.com/zenite-serena/Atividade-Didatica-Banco-de-Dados)

Desafio: Manipular dados usando SQLite. Gerar visualizações usando a biblioteca MatPlotLib.

### Objetivos da análise

O intuito dessa análise foi comparar as mudanças relativas de temperatura em 3 subsets de países, escolhidos de acordo com critérios geográficos e populacionais.

Com base no artigo "Change in cooling degree days with global mean temperature rise increasing from 1.5 °C to 2.0 °C", publicado na revista Nature, embora países na África central e subsaariana vem sofrendo e sofrerão com os maiores aumentos em temperatura em termos absolutos, são países no norte da Europa que sofrem e sofrerão com os maiores aumentos em temperatura em termos relativos.

A partir da análise do banco de dados da FAOSTAT, criamos gráficos que facilitam a visualização destes dados e corroboram o que foi apontado pelo estudo.

["Change in cooling degree days with global mean temperature rise increasing from 1.5 °C to 2.0 °C"](https://www.nature.com/articles/s41893-023-01155-z)

["Northern Europe faces biggest relative increase in uncomfortable heat and is dangerously unprepared"](https://theconversation.com/northern-europe-faces-biggest-relative-increase-in-uncomfortable-heat-and-is-dangerously-unprepared-new-research-209745)

###	Breve descrição da base de dados

O banco de dados utilizado é referente a mudanças de temperatura, coletado e disponibilizado pelo FAOSTAT (Food and Agriculture Organization of the United Nations) na mudança média de temperatura por país. O banco de dados cobre o período de 1961-2020. Os dados estão disponíveis por mês, estação e ano (considerando anomalias médias anuais, i.e., mudanças de temperatura com respeito a uma climatologia de base, correspondendo ao período de 1951-1980).

[Temperature Change Data](https://www.kaggle.com/datasets/sevgisarac/temperature-change/data)

### Tratamento de dados

Para o tratamento de dados foram criados subsets baseados em regiões geográficas e características populacionais, de modo a facilitar a visualização e processamento de dados.

Foram removidas colunas julgadas desnecessárias e dados nulos. Também foram normalizados os valores de temperatura para plotagem do gráfico.

Para os gráficos, foram escolhidos 1 país de cada subset e os valores correspondentes ao verão dos respectivos hemisférios.

### Conclusão

Os gráficos permitem a fácil visualização de um grave problema, possivelmente o maior desafio que a humanidade já enfrentou.

O resultado é consistente com o que têm apresentado inúmeras organizações como o IPCC (Intergovernmental Panel on Climate Change) e a NASA (National Aeronautics and Space Administration), que alertam para os perigos da mudança climática impulsionada pela queima de combustíveis fósseis e o efeito estufa.

Embora os gráficos explicitem uma mudança relativa em temperaturas do norte da Europa, não devemos achar que o problema não será grave também nos trópicos. Uma análise futura poderá fazer uso de dados absolutos e não relativos para o propósito de alerta.

A análise cruzada com outros dados, como aqueles relativos à emissão de CO², podem nos dar uma ideia das desigualdades globais de um problema compartilhado. Fica o alerta de que os países do Sul Global sofrerão os devastadores efeitos de um problema que, historicamente, não é de sua responsabilidade.

["Which countries are historically responsible for climate change?"](https://www.carbonbrief.org/analysis-which-countries-are-historically-responsible-for-climate-change/)

<img src="exercicios\para-casa\temp_change_braz.png" width="60%"/>
<img src="exercicios\para-casa\temp_change_switz.png" width="60%"/>
<img src="exercicios\para-casa\temp_change_nigeria.png" width="60%"/>

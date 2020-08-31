# pythonFlask

Criar Web APIs usando Python e Flask
====================================

<h1>Pré-requisitos</h1>
Python 3, <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask Web Framework</a> e browser são necessários para esse "tutorial". Para quem não possui Python instalado, sugiro instalar pelo pacote do <a href="https://www.anaconda.com/">Anaconda</a>. Para "escrever" código Python você pode usar diversos IDEs de desenvolvimento como: sublime, VS Code, PyCharm e até mesmo um editor de texto. Para esse tutorial e outros trabalhos, uso o <a href="https://www.jetbrains.com/pycharm/">PyCharm</a>.

<h1>Introdução a APIs</h1>
Uma web API permite que informação ou funcionalidade seja manipulada por outros programas via internet. Por exemplo, com a web API do twitter você pode escrever um código que executa tarefas como: apresentar tweets favoritos ou coletar metadados de tweets.

O termo API, abreviação de Application Programming Interface na lingua inglesa, refere-se a uma parte de um programa de computador projetado para ser usado ou manipulado por outro programa, em oposição a uma interface projetada para ser usada ou manipulada por um humano. Os programas de computador freqüentemente precisam se comunicar entre si ou com o sistema operacional subjacente, e as APIs são uma forma de fazê-lo. Neste tutorial, no entanto, usaremos o termo API para nos referirmos especificamente a APIs da web.

<h1>Quando criar uma API</h1>
Geralmente é necessário se:

<ul>
  <li>Para grandes datasets que consomem muitos recursos via download</li>
  <li>Para acesso a dados em tempo real</li>
  <li>Para situações de alta volatilidade de dados</li>
  <li>Como restrição de acesso a dados com alta disponibilidade</li>
  <li>Quando existe mais de uma operação envolvida. Ou seja, além da operação de recuperação de dados, exista a necessidade de inserir, atualizar e/ou excluir dados</li>
</ul>

Uma API é uma ótima maneira de compartilhar dados e/ou funcionalidades com outras pessoas ou programas. Entretanto, se os dados possuem tamanho relativamente pequeno, as APIs nem sempre são a melhor maneira de compartilhá-los. Nesse caso, talvez fosse interessante fornecer "data dump" na forma de arquivos JSON, XML ou CSV.  

<h1>Terminologia API</h1>
Ao construir ou usar APIs, encontramos frequentemente os seguintes termos:

<ul>
  <li><b>HTTP(Hypertext Transfer Protocol)</b> é o principal meio de comunicação de dados na web. O HTTP implementa vários métodos que informa para qual direção e o que deve acontecer com os dados. Os dois métodos ais comuns são GET e POST.</li>
  <li><b>URL(Uniform Resource Locator)</b> é um endereço de um recurso na web (https://www.jetbrains.com/pycharm/). Consite de um protocolo (http://), domínio (jetbrains.com) e um path opcional (/pycharm). Uma URL descreve a localização de um recurso específico, como uma página da web. Ao ler sobre APIs é possível ver os termos URL, request, URI e endpoint usados para descrever ideias próximas ou semelhantes. Como forma de simplificar, o tutorial dará preferência ao termo URL e solicitações GET, portanto, não é preciso de nenhum software especial para fazer as requisições.</li>
  <li><b>JSON(JavaScript Object Notation)</b> é um texto baseado em formato de armazenamento de dados que tem por objetivo ser de fácil leitura por humanos e máquinas. JSON é o formato de retorno mais comum através de uma API e XML é o segundo mais comum.</li>
  <li><b>REST(REpresentational State Transfer)</b> é uma padronização que descreve algumas melhores práticas para implementação de APIS. Arquitetar e implementar APIs com alguns ou todos esses padrões é chamado de REST APIs. Embora use de alguns padrões REST, o tutorial pode ser descrito como Web API ou HTTP API.  </li>
</ul>

<h1>O que foi feito...</h1>
Utilizando o conceito MVC (model, view, controller) foram criadas as seguintes classes:

- DAO (Data Access Object): classe que gerencia o acesso ao sqLite;
- CiclistaDAO (Ciclista Data Access Object): classe que gerencia quais acessos em quais objetos do sqLite;
- CiclistaDTO (Ciclista Data Transfer Object): classe que possui o modelo do objeto ciclista;
- CiclistaDLO (Ciclista Logical Object): classe de interface que define a lógica, ou seja, classe que implementa as funcionalidade ou casos de uso.

E por último o arquivo api.py que utiliza o Flask Framework para definir as rotas e seus métodos de acesso.

O tutorial permite entender como funciona como funciona o processo de crud (create, read, update e delete) através de uma Web API. 


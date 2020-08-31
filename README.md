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
  <li><b>HTTP(Hypertext Transfer Protocol)</b></li>
  <li><b>URL(Uniform Resource Locator)</b></li>
  <li><b>JSON(JavaScript Object Notation)</b></li>
  <li><b>REST(REpresentational State Transfer)</b></li>
</ul>



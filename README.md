# Desafio Técnico Morada.ai: Caixa Eletrônico API

## Descrição
E uma API simples que simula saques em um caixa eletrônico com um numero minimo de cedulas.
Para fazer esse projeto, utilizei o Flask do Python por ser um projeto simples. Decidi usar o Flask e também utilizei o pytest para escrever um testar  a lógica do caixa eletrônico.
Poderia de usado o Django do python ou entao o typescript junto com nodeJs com express que saberia fazer a api, mas pelo fato  de ser uma api simples decidi utilizar o flask

## Principais Desafios
O unico desafio de fato dessa API foi a lógica para verificar a quantidade mínima de cédulas para saque, que não achei tão difícil, mas foi a parte que precisei raciocinar mais.

## Explicando a Logica de saques
Para saber a quantidade mínima de cédulas para o saque, eu pego o valor que vem da requisição, por exemplo, 380. Crio um loop dentre as notas que o caixa é permitido sacar. 
Verifico se o valor da requisição é maior ou igual à cédula que está no loop atual. Se for verdadeiro, acesso o dicionário que criei anteriormente com as chaves das cédulas permitidas e com valor inicial de zero. 
Acesso a chave desse dicionário e atribuo o valor da divisão inteira do valor da requisição, nesse exemplo, 380, com o valor da chave, que neste caso é 100. O resultado será 3. Em seguida, pego o resto da divisão, que será 80,
e faço a divisão inteira com a próxima chave, que é 50, o que irá retornar 1. E assim, vou fazendo a divisão de todas as cédulas permitidas com o valor enviado na requisição e pegando o resto até acabar o loop 
e retornar o dicionário com as cédulas mínimas necessárias para o saque.

## Rodando o projeto no seu computador

0. Voce precisa ter o python instalado no seu computador
```bash
python -V (verificar a versão do Python)
```

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale as dependências do projeto `Flask-Pytest`:
```shell
pip install -r requirements.txt
```

4. Rode o comando para executar o challenge:
```shell
python app.py
```

# 🧪 Testes Automatizados com TDD em Python

Este repositório apresenta a aplicação de **Test-Driven Development (TDD)** com **Python**, utilizando a biblioteca **pytest**. O objetivo do projeto é demonstrar a importância dos testes automatizados no desenvolvimento de software, cobrindo conceitos como **testes unitários, exceções, marks e cobertura de testes**.

---

## 📌 O que você vai aprender

✅ **Fundamentos do TDD**: Desenvolver software escrevendo testes antes do código.  
✅ **Uso do pytest**: Criar testes automatizados de forma simples e eficiente.  
✅ **Cobertura de testes**: Verificar quais partes do código estão sendo testadas.  
✅ **Tratamento de exceções**: Garantir que erros sejam identificados corretamente.  
✅ **Uso de Marks**: Agrupar e categorizar testes para diferentes cenários.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **pytest** (Framework para testes)
- **pytest-cov** (Cobertura de testes)

---

## 📂 Estrutura do Projeto

```
📁 MeuProjetoTDD
│── 📂 tests  # Diretório com os testes
│    ├── test_meu_codigo.py  # Arquivo com os testes
│── meu_codigo.py  # Código principal
│── requirements.txt  # Dependências do projeto
│── README.md  # Documentação do projeto
```

---

## ⚙️ Como Executar os Testes

1️⃣ Clone este repositório:
```sh
 git clone https://github.com/seu-usuario/MeuProjetoTDD.git
```

2️⃣ Acesse o diretório do projeto:
```sh
 cd MeuProjetoTDD
```

3️⃣ Crie um ambiente virtual e ative-o:
```sh
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

4️⃣ Instale as dependências:
```sh
pip install -r requirements.txt
```

5️⃣ Execute os testes:
```sh
pytest
```

6️⃣ Para verificar a cobertura de testes:
```sh
pytest --cov
```

---

## 📜 Exemplo de Teste
Aqui está um exemplo simples de um teste unitário escrito com pytest:

```python
import pytest
from meu_codigo import calcular_idade

def test_calcular_idade():
    assert calcular_idade("2000-03-13") == 25  # Considerando o ano de 2025
```

---

## 📬 Contato
Caso tenha dúvidas ou sugestões, sinta-se à vontade para entrar em contato!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](www.linkedin.com/in/cristoferruan-dev) 
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cristoferrxan)

🚀 **Aprender e testar é o caminho para a excelência no desenvolvimento!**

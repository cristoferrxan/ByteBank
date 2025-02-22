Testes Automatizados com TDD em Python 🐍
Este projeto explora a prática de Test-Driven Development (TDD) com Python, usando pytest para a criação de testes automatizados. O objetivo é demonstrar como escrever código mais confiável e robusto, garantindo que ele funcione corretamente desde o início.

📌 Tecnologias Utilizadas
Python 🐍
pytest 🔧
TDD (Test-Driven Development)
Cobertura de testes
Exceptions e Marks no pytest
🚀 O que você vai aprender
✅ Como escrever testes automatizados com pytest
✅ Os fundamentos do Test-Driven Development (TDD)
✅ Como utilizar marks e exceptions em testes
✅ Como medir a cobertura de testes para garantir a qualidade do código

📂 Estrutura do Projeto
bash
Copiar
Editar
📁 MeuProjetoTDD/
 ├── codigo/               # Código principal do projeto
 ├── tests/                # Testes automatizados
 ├── .coverage             # Relatório de cobertura de testes
 ├── pytest.ini            # Configuração do pytest
 ├── requirements.txt      # Dependências do projeto
 ├── coverage_relatorio.html # Relatório de cobertura em HTML
 └── README.md             # Você está aqui! 🎯
🛠 Como Rodar o Projeto
Clone o repositório

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual e ative

bash
Copiar
Editar
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate  # Windows  
Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt  
Execute os testes

bash
Copiar
Editar
pytest  
Gerar relatório de cobertura

bash
Copiar
Editar
pytest --cov=codigo  
Visualizar relatório de cobertura no navegador

bash
Copiar
Editar
python -m http.server 8000  
Depois, acesse: http://localhost:8000/coverage_relatorio.html

📚 Entendendo TDD
TDD é uma metodologia onde primeiro escrevemos os testes e só depois implementamos o código. O fluxo de trabalho é:

1️⃣ Escrever um teste para a funcionalidade desejada.
2️⃣ Rodar o teste e ver ele falhar (pois o código ainda não foi escrito).
3️⃣ Implementar o código necessário para o teste passar.
4️⃣ Executar os testes novamente e confirmar que estão passando.
5️⃣ Refatorar o código mantendo os testes funcionando.

📜 Conclusão
Este projeto foi desenvolvido para demonstrar a importância dos testes automatizados e da abordagem TDD. Se tiver dúvidas ou sugestões, fique à vontade para abrir uma issue no repositório! 😊

🔗 Conecte-se comigo: Github:https://github.com/cristoferrxan // Linkedn:www.linkedin.com/in/cristoferruan-dev


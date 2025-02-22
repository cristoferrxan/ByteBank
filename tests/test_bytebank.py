from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass():
    """
    Classe de testes para verificar o funcionamento da classe Funcionario.
    
    Foca em validar os métodos de cálculo de idade, extração de sobrenome
    e decréscimo salarial.
    """
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_25(self):
        """
        Testa o método idade() para um funcionário nascido em 13/03/2000.
        
        Given:
            - Data de nascimento válida no formato 'DD/MM/AAAA'
        When:
            - Cria instância com data '13/03/2000'
            - Chama o método idade()
        Then:
            - Deve retornar 25 anos (considerando ano base 2025)
        """
        # Given - Contexto
        entrada = '13/03/2000'  
        esperado = 25
        
        # When - ação   
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  

        # Then - desfecho
        assert resultado == esperado  
        
    def test_quando_sobrenome_recebe_Cristofer_Ruan_deve_retornar_Ruan(self):
        """
        Testa a extração do sobrenome para o nome 'Cristofer Ruan'.
        
        Verifica:
            - Remoção de espaços em branco excedentes
            - Captura do último nome após split
            - Case sensitive do resultado
            
        Cenário:
            Nome com dois termos e espaços antes/depois
        """
        # Given - Contexto
        entrada = ' Cristofer Ruan ' 
        esperado = 'Ruan'
        
        #When - Ação
        cristofer = Funcionario(entrada, '23/07/2002', 11111)
        resultado = cristofer.sobrenome() 
        
        # Then - desfecho
        assert resultado == esperado 
        
    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):
        """
        Testa o decréscimo de 10% para salários altos (>= R$100.000,00).
        
        Critérios:
            - Aplica 10% de redução em salários igual ou acima do limite
            - Verifica cálculo exato sem arredondamentos
            - Valida alteração direta no atributo salario
            
        Caso específico:
            Entrada: 100.000 → Saída esperada: 90.000
        """
        # Given - Contexto
        entrada_salario = 100000   
        entrada_nome = 'Paulo Bragança' 
        retorno = 90000
        
        #When - Ação
        funcionario_teste = Funcionario(entrada_nome, '09/09/1989', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        
        # Then - desfecho
        assert resultado == retorno
        
    @mark.calcular_bonus
    def test_calcular_bonus_recebe_1000_deve_retornar_100(self):
        """
        Testa o cálculo de bônus para salário de R$ 1.000,00.
        
        Verifica:
            - Aplicação correta de 10% sobre o salário
            - Caso válido para bonificação padrão
            - Tipo de retorno numérico
            
        Cenário:
            Salário dentro do limite permitido para bonificação
    """
         # Given - Contexto
        entrada = 1000
        retorno = 100
        
        #When - Ação
        funcionario_teste = Funcionario('teste', '01/01/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()
        
        # Then - desfecho
        assert resultado == retorno
        
    @mark.calcular_bonus      
    def test_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        """
    Testa a exceção para cálculo de bônus com salário alto.
    
    Valida:
        - Lançamento de exceção para salários acima do permitido
        - Mensagem de erro esperada (se aplicável)
        - Tipo de exceção específica
        
    Edge case:
        Salário 100x maior que o limite de bonificação
    """
         # Given
    with pytest.raises(ValueError) as excinfo:  # Exceção específica
        entrada = 100000
        
        # When
        funcionario_teste = Funcionario('teste', '01/01/2000', entrada)
        funcionario_teste.calcular_bonus()  # Linha que deve lançar a exceção
        
    # Then
    assert "Salário muito alto para bônus" in str(excinfo.value)  # Valida mensagem
#Vamos criar uma calculadora simples que recebe dois números e uma operação (soma, subtração, multiplicação ou divisão) e retorna o resultado.
def calcular(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."
# Exemplo de uso
if __name__ == "__main__":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ").strip().lower()
    
    resultado = calcular(num1, num2, operacao)
    print(f"O resultado da {operacao} é: {resultado}")
# Testes
def test_calcular():
    assert calcular(2, 3, 'soma') == 5
    assert calcular(5, 2, 'subtracao') == 3
    assert calcular(4, 3, 'multiplicacao') == 12
    assert calcular(8, 2, 'divisao') == 4
    assert calcular(8, 0, 'divisao') == "Erro: Divisão por zero não é permitida."
    assert calcular(5, 3, 'modulo') == "Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."
if __name__ == "__main__":
    test_calcular()
    print("Todos os testes passaram!")
# A função de teste verifica se a calculadora funciona corretamente para as operações básicas e lida com erros como divisão por zero e operações inválidas.
# --- gerenciador_notas.py ---

def calcular_media(notas):
    """
    Calcula a média aritmética simples a partir de uma lista de notas numéricas.

    Esta função realiza o somatório de todos os elementos contidos no argumento
    e divide pelo número total de ocorrências. Há um tratamento prévio para
    evitar erros de divisão por zero caso a lista seja fornecida vazia.

    Args:
        notas (list): Uma lista composta por números de ponto flutuante (floats)
                      representando as notas obtidas pelo estudante.

    Returns:
        float: O valor da média aritmética calculada. Retorna 0.0 caso a lista
               de notas informada esteja vazia.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=7.0):
    """
    Avalia o status final de aprovação de um estudante com base em sua média.

    A função aplica uma regra de negócio condicional simples para validar se a
    média alcançada atinge ou supera a nota de corte estipulada pela instituição.

    Args:
        media (float): O valor numérico correspondente à média final do aluno.
        media_minima (float, opcional): A nota de corte mínima exigida para obter
                                        a aprovação. O valor padrão é 7.0.

    Returns:
        str: Retorna a string exata 'Aprovado' se a média for satisfatória, ou 
             a string 'Reprovado' caso a média seja estritamente menor que o corte.
    """
    if media >= media_minima:
        return 'Aprovado'
    else:
        return 'Reprovado'


def gerar_relatorio(alunos):
    """
    Processa a listagem de estudantes cadastrados e renderiza um relatório em bloco.

    A rotina realiza uma iteração controlada (loop) sobre a coleção de estudantes,
    consome as funções lógicas de cálculo de média e validação de status, e imprime
    uma tabela formatada visualmente no terminal com colunas de largura fixa.

    Args:
        alunos (list): Uma lista de dicionários, onde cada dicionário deve possuir
                       obrigatoriamente as chaves 'nome' (str) e 'notas' (list).

    Returns:
        None: A função realiza apenas a saída de dados em terminal (print), 
              não retornando nenhum valor em memória.
    """
    print("=" * 60)
    print(f"{'RELATÓRIO ACADÊMICO INTEGRADO':^60}")
    print("=" * 60)
    print(f"{'Nome do Estudante':<30} | {'Média':>10} | {'Situação':>12}")
    print("-" * 60)
    
    if not alunos:
        print(f"{'Nenhum estudante registrado na base de dados.':^60}")
    else:
        for aluno in alunos:
            media_final = calcular_media(aluno["notas"])
            situacao_final = verificar_aprovacao(media_final)
            print(f"{aluno['nome']:<30} | {media_final:>10.2f} | {situacao_final:>12}")
            
    print("=" * 60)


if __name__ == "__main__":
    estudantes = [
        {"nome": "Airton Luis Barboza", "notas": [8.5, 9.0, 9.5]},
        {"nome": "Ana Maria da Silva", "notas": [6.0, 5.5, 7.0]},
        {"nome": "Lucas Oliveira Santos", "notas": [4.0, 5.0, 3.5]},
        {"nome": "Beatriz Rodrigues", "notas": [7.0, 7.5, 8.0]}
    ]
    gerar_relatorio(estudantes)

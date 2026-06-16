# --- test_notas.py ---
import unittest
# CORREÇÃO DO ERRO 1: Importação real para tornar o arquivo executável por terceiros
from gerenciador_notas import calcular_media, verificar_aprovacao

class TestGerenciamentoNotas(unittest.TestCase):
    """
    Suíte de testes automatizados para validar a robustez e integridade
    das rotinas matemáticas e lógicas do sistema acadêmico.
    """

    def test_calculo_media_fluxo_normal(self):
        """1. Valida o cálculo correto da média aritmética sob condições normais."""
        notas_aluno = [8.0, 9.0, 7.0, 10.0]
        media_calculada = calcular_media(notas_aluno)
        self.assertEqual(media_calculada, 8.5)

    def test_verificacao_aprovacao_comum(self):
        """2. Valida o status de aprovação comum com base na nota de corte padrão (7.0)."""
        media_aprovado = 7.5
        situacao = verificar_aprovacao(media_aprovado)
        self.assertEqual(situacao, 'Aprovado')

    def test_verificacao_reprovacao_comum(self):
        """3. Valida o status de reprovação comum com base na nota de corte padrão (7.0)."""
        media_reprovado = 6.9
        situacao = verificar_aprovacao(media_reprovado)
        self.assertEqual(situacao, 'Reprovado')

    def test_calculo_media_lista_vazia_edge_case(self):
        """4. Valida o caso extremo (Edge Case) enviando uma lista de notas vazia."""
        notas_vazias = []
        media_calculada = calcular_media(notas_vazias)
        self.assertEqual(media_calculada, 0.0)

    def test_verificacao_aprovacao_media_vazia_edge_case(self):
        """5. Valida se a rotina de aprovação lida corretamente com a média do edge case vazia."""
        notas_vazias = []
        media_calculada = calcular_media(notas_vazias)
        situacao = verificar_aprovacao(media_calculada)
        self.assertEqual(situacao, 'Reprovado')

    def test_estabilidade_corte_zero_absoluto(self):
        """6. Testa o acionamento limitador configurando a média de corte mínima com o valor 0 (zero)."""
        media_aluno = 0.0
        situacao = verificar_aprovacao(media_aluno, media_minima=0.0)
        self.assertEqual(situacao, 'Aprovado')


if __name__ == '__main__':
    unittest.main()

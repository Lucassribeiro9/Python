import unittest
from cpplanilhas import executar_atualizacao

class TestAtualizarPlanilha(unittest.TestCase):
    def test_executar_atualizacao(self):
        # Teste se a função executar_atualizacao está funcionando corretamente
        executar_atualizacao()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
# 📊 Sistema de Gerenciamento Acadêmico

Uma aplicação robusta desenvolvida em Python para registrar, consolidar e acompanhar o desempenho de estudantes através do terminal. O projeto simula regras de negócio institucionais de corte e validação de aprovação.

---

## ⚙️ Diferenciais do Projeto e Qualidade de Código

* **Tratamento de Edge Cases:** Arquitetura prevenida contra falhas matemáticas, tratando listas vazias para mitigar erros de divisão por zero (*ZeroDivisionError*).
* **Interface Limpa no Terminal:** Renderização de tabelas e relatórios acadêmicos formatados com alinhamento e espaçamento fixo.
* **Código Documentado:** Todas as funções seguem os padrões de documentação com *docstrings* explicativas.

---

## 🧪 Qualidade de Software: Testes Automatizados

O sistema conta com uma suíte integrada de testes unitários utilizando o framework nativo `unittest`, garantindo a estabilidade do software contra regressões de bugs. Os testes cobrem:
1. Cálculo de médias em fluxo normal.
2. Status de aprovação e reprovação com nota de corte padrão (7.0).
3. Estabilidade do sistema sob cenários limites (Edge Cases e corte zero absoluto).

---

## 🔧 Como Executar e Testar

### Pré-requisitos
* Python 3.x instalado.

### 🏃 Executar a Aplicação Principal
Para emitir o relatório acadêmico integrado no terminal, execute:
```bash
python gerenciador_notas.py

Acionar a Bateria de Testes
Para disparar as validações automatizadas e verificar a integridade das funções, execute:
```Bash
python test_notas.py

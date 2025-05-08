# 🧪 Projeto Sprint 8 — Automação de Testes com Selenium

Este projeto faz parte da Sprint 8 do Bootcamp de QA da TripleTen.  
O objetivo é realizar a automação de testes end-to-end no app Urban Routes utilizando **Python** e **Selenium**.

---

## 🚗 Funcionalidades Testadas

- Preencher rota com endereços de origem e destino
- Autenticar número de telefone com código SMS (via interceptação de log)
- Adicionar cartão de crédito
- Adicionar comentário para o motorista
- Pedir cobertor e lenços
- Pedir dois sorvetes
- Verificar se modelo do carro aparece após pedido

---

## 🛠️ Tecnologias Utilizadas

- Python 3.9
- Selenium WebDriver
- Pytest
- WebDriverWait
- Google Chrome + ChromeDriver
- Padrão Page Object Model (POM)

---

## 📁 Estrutura do Projeto

```
├── main.py                  # Arquivo com os testes automatizados
├── data.py                  # Dados de teste e constantes
├── helpers.py               # Funções auxiliares
├── pages/                   # Classes de páginas com ações
│   ├── base_page.py
│   ├── order_page.py
│   ├── pages.py
├── urban_routes_mock.html   # Página mockada para testes locais
```

---

## ▶️ Como Executar os Testes

### 1. Ative o ambiente virtual (se já configurado):
```bash
source .venv/bin/activate
```

### 2. Execute os testes com o pytest:
```bash
pytest main.py
```

---

## ✅ Requisitos

- Python 3.9
- Google Chrome instalado
- ChromeDriver compatível com a versão do seu navegador

---

## 📦 Observação

Caso o servidor oficial da Urban Routes não esteja disponível, use o arquivo `urban_routes_mock.html` localmente para rodar os testes.

---

## ✍️ Autor

**Matheus — QA em formação na TripleTen**

---

## 🧑‍💻 Diretrizes de nomenclatura de código

- **Nomes de variáveis** são escritos em `snake_case` e descrevem sua finalidade;
- **Constantes** são escritas em maiúsculas;
- **Comentários** são usados para explicar blocos importantes de código;
- A **organização do código** é modular, com blocos de código reutilizáveis importados para onde for necessário;
- Evite funções de espera (`wait`) desnecessárias que fazem com que o teste seja executado por mais tempo do que o necessário;
- Siga uma **convenção de nomenclatura** para títulos de teste que começam com `test_` e fornecem uma descrição clara do cenário de teste. Os títulos dos testes são fornecidos no resumo.

### Diretrizes de nomenclatura de código

- **Nomes de variáveis** são escritos em `snake_case` e descrevem sua finalidade;
- **Constantes** são escritas em maiúsculas;
- **Comentários** são usados para explicar blocos importantes de código;
- A **organização do código** é modular, com blocos de código reutilizáveis importados para onde for necessário;
- Evite funções de espera (`wait`) desnecessárias que fazem com que o teste seja executado por mais tempo do que o necessário;
- Siga uma **convenção de nomenclatura** para títulos de teste que começam com `test\_` e fornece uma descrição clara do cenário de teste. Os títulos dos testes são fornecidos no resumo.

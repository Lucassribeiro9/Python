# Calculadora

Uma calculadora básica com interface gráfica desenvolvida em Python usando PySide6.

## Funcionalidades

- Operações básicas (+, -, *, /)
- Potenciação (^)
- Inversão de número (N)
- Backspace (◀)
- Limpar (C)
- Exibição em tempo real da operação sendo realizada

## Características

- Interface moderna e responsiva
- Atualização em tempo real do display
- Suporte a números decimais
- Validação de entrada de dados
- Mensagens de erro amigáveis

## Estrutura do Projeto

```
calculadora_g/
├── __pycache__/
├── consts.py           # Constantes do projeto
├── files/              # Arquivos de recursos
├── main.py            # Ponto de entrada da aplicação
├── main_window.py     # Classe principal da janela
├── style/             # Componentes visuais
│   ├── buttons.py     # Gerenciamento dos botões
│   ├── display.py     # Componente do display
│   ├── info.py       # Componente de informação
│   └── styles.py     # Estilos visuais
└── utils.py          # Funções utilitárias
```

## Requisitos

- Python 3.12+
- PySide6

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando

```bash
python main.py
```



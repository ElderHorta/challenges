# Desafio Técnico — Engenharia de Dados

Solução para o teste técnico de engenharia de dados da FIEMG, usando Python, pandas e SQL (via pandasql/SQLite).

## Estrutura

```
├── content/
│   ├── buyers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── payments.csv
│   ├── products.csv
│   └── sellers.csv
├── modelo_teste.ipynb                # Respostas finais dos 4 desafios
├── modelo_exploracao_dados.ipynb     # Quality check e exploração dos dados
└── Desafio Técnico - Engenharia de Dados.pdf
```

## Pré-requisitos

Python 3.9+ com os seguintes pacotes:

```bash
pip install pandas pandasql
```

## Como rodar

1. Abra o notebook de respostas `modelo_teste.ipynb` no VS Code (ou Jupyter)
2. Execute todas as células em ordem (**Run All**)

Os desafios estão nas células 11 a 14:

| Célula | Desafio |
|--------|---------|
| 11 | Faturamento bruto mensal — últimos 12 meses |
| 12 | Top 10 sellers por crescimento de GMV (QoQ) |
| 13 | Pedidos com desconto abusivo (> 40% do valor bruto) |
| 14 | Produtos com alto volume mas nunca o item de maior valor unitário |

Para exploração e quality check dos dados, abra `modelo_exploracao_dados.ipynb` e execute todas as células.

## Observações

- As queries usam SQLite via `pandasql` — a sintaxe pode diferir ligeiramente de outras sintaxes SQL (`STRFTIME`, `DATE(...)`) 

## Desafio
A descrição do desafio está no arquivo Desafio Técnico - Engenharia de Dados.pdf

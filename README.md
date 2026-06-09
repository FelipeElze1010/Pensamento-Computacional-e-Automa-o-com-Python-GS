# 🚀 Mission Control AI
### Sistema Inteligente de Monitoramento de Missão Espacial

**GS2026.1 – Pensamento Computacional e Automação com Python | FIAP**

---

## 👨‍🚀 Equipe

| Nome | RM |
|---|---|
| Felipe Elze da Silva | 572024 |
| Henrique Eduardo da Silva | 571803 |

**Missão:** Nova Horizonte - Alpha  
**Equipe:** Equipe Saturn

---

## 📋 Descrição do Projeto

O **Mission Control AI** é um sistema em Python que simula o monitoramento inteligente de uma missão espacial experimental. O sistema analisa ciclos de monitoramento com 5 parâmetros operacionais, gera alertas automáticos, calcula o nível de risco de cada ciclo e exibe um relatório final completo.

---

## 🛰️ Áreas Monitoradas

| Posição | Área | Unidade |
|---|---|---|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (Bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

---

## ⚠️ Regras de Alerta

### Temperatura
| Condição | Classificação | Pontos |
|---|---|---|
| < 18°C | ATENÇÃO | 1 |
| 18°C a 30°C | NORMAL | 0 |
| 30°C a 35°C | ATENÇÃO | 1 |
| > 35°C | CRÍTICO | 2 |

### Comunicação
| Condição | Classificação | Pontos |
|---|---|---|
| < 30% | CRÍTICO | 2 |
| 30% a 59% | ATENÇÃO | 1 |
| ≥ 60% | NORMAL | 0 |

### Bateria
| Condição | Classificação | Pontos |
|---|---|---|
| < 20% | CRÍTICO | 2 |
| 20% a 49% | ATENÇÃO | 1 |
| ≥ 50% | NORMAL | 0 |

### Oxigênio
| Condição | Classificação | Pontos |
|---|---|---|
| < 80% | CRÍTICO | 2 |
| 80% a 89% | ATENÇÃO | 1 |
| ≥ 90% | NORMAL | 0 |

### Estabilidade
| Condição | Classificação | Pontos |
|---|---|---|
| < 40% | CRÍTICO | 2 |
| 40% a 69% | ATENÇÃO | 1 |
| ≥ 70% | NORMAL | 0 |

---

## 🎯 Classificação dos Ciclos

| Pontuação | Classificação |
|---|---|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

## 🔧 Funções Implementadas

| Função | Descrição |
|---|---|
| `analisar_temperatura()` | Classifica temperatura e retorna status/pontos |
| `analisar_comunicacao()` | Classifica comunicação e retorna status/pontos |
| `analisar_bateria()` | Classifica bateria e retorna status/pontos |
| `analisar_oxigenio()` | Classifica oxigênio e retorna status/pontos |
| `analisar_estabilidade()` | Classifica estabilidade e retorna status/pontos |
| `classificar_ciclo()` | Classifica o ciclo com base na pontuação total |
| `gerar_recomendacao()` | Gera recomendação automática por situação |
| `analisar_tendencia()` | Compara primeiro e último ciclo |
| `identificar_area_mais_afetada()` | Identifica área com maior risco acumulado |
| `gerar_relatorio_final()` | Exibe relatório consolidado da missão |

---

## ▶️ Como Executar

```bash
python mission_control.py
```

Não são necessárias bibliotecas externas. O sistema roda com Python 3.x puro.

---

## 📁 Estrutura do Repositório

```
mission-control-ai/
│
├── README.md
└── mission_control.py
```

---

## 📌 Observações

- Os dados simulados são fixos no código e representam uma missão com progressão realista: início estável → crise → recuperação.
- A inteligência do sistema é baseada em regras lógicas (estruturas condicionais).
- Nenhuma biblioteca externa é utilizada.

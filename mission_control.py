# ============================================================
# MISSION CONTROL AI
# GS2026.1 - Pensamento Computacional e Automacao com Python
# Missao: Nova Horizonte - Alpha
# Equipe: Equipe Saturn
# Integrantes:
#   Felipe Elze da Silva    - RM: 572024
#   Henrique Eduardo da Silva - RM: 571803
# ============================================================

# --- Dados da missao ---
NOME_MISSAO = "Nova Horizonte - Alpha"
NOME_EQUIPE = "Equipe Saturn"

# --- Matriz principal: [temperatura, comunicacao, bateria, oxigenio, estabilidade] ---
dados_missao = [
    [22, 95, 91, 97, 93],
    [26, 84, 76, 95, 87],
    [32, 61, 55, 90, 68],
    [37, 40, 35, 85, 52],
    [41, 25, 17, 76, 33],
    [35, 52, 30, 80, 48],
    [30, 68, 45, 86, 62],
    [25, 79, 60, 91, 75],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]


# ============================================================
# FUNCOES DE ANALISE
# ============================================================

def analisar_temperatura(valor):
    """Classifica a temperatura e retorna (status, pontos, descricao)."""
    if valor < 18:
        return "ATENCAO", 1, "Temperatura abaixo do ideal"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estavel"
    elif valor <= 35:
        return "ATENCAO", 1, "Temperatura elevada"
    else:
        return "CRITICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):

    if valor < 30:
        return "CRITICO", 2, "Comunicacao com a base em nivel critico"
    elif valor < 60:
        return "ATENCAO", 1, "Comunicacao instavel"
    else:
        return "NORMAL", 0, "Comunicacao estavel"


def analisar_bateria(valor):
    """Classifica a bateria e retorna (status, pontos, descricao)."""
    if valor < 20:
        return "CRITICO", 2, "Bateria em nivel critico"
    elif valor < 50:
        return "ATENCAO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estavel"


def analisar_oxigenio(valor):
    """Classifica o oxigenio e retorna (status, pontos, descricao)."""
    if valor < 80:
        return "CRITICO", 2, "Oxigenio em nivel critico"
    elif valor < 90:
        return "ATENCAO", 1, "Oxigenio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigenio adequado"


def analisar_estabilidade(valor):
    """Classifica a estabilidade e retorna (status, pontos, descricao)."""
    if valor < 40:
        return "CRITICO", 2, "Estabilidade operacional critica"
    elif valor < 70:
        return "ATENCAO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    """Classifica o ciclo com base na pontuacao de risco."""
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"


def gerar_recomendacao(resultados):
    """Gera recomendacao automatica com base nos status do ciclo."""
    criticos = [r for r in resultados if r[0] == "CRITICO"]
    atencao  = [r for r in resultados if r[0] == "ATENCAO"]

    if not criticos and not atencao:
        return "Manter operacao normal e continuar monitoramento."

    recomendacoes = []
    for status, _, descricao, area in [(r[0], r[1], r[2], r[3]) for r in resultados]:
        if status == "CRITICO":
            if area == "Temperatura interna":
                recomendacoes.append("Verificar controle termico da missao.")
            elif area == "Comunicacao com a base":
                recomendacoes.append("Tentar restabelecer contato com a base.")
            elif area == "Sistema de energia":
                recomendacoes.append("Ativar modo de economia de energia.")
            elif area == "Suporte de oxigenio":
                recomendacoes.append("Acionar protocolo de suporte a vida.")
            elif area == "Estabilidade operacional":
                recomendacoes.append("Reduzir operacoes nao essenciais.")

    if len(criticos) >= 3:
        return "ALERTA GERAL: Ativar modo de seguranca e priorizar suporte a vida, energia e comunicacao."

    if recomendacoes:
        return " | ".join(dict.fromkeys(recomendacoes))

    return "Monitorar sistemas em atencao e preparar plano de contingencia."


def analisar_tendencia(riscos):
    """Compara risco do primeiro e ultimo ciclo para identificar tendencia."""
    if riscos[-1] > riscos[0]:
        return "A missao apresentou tendencia de PIORA."
    elif riscos[-1] < riscos[0]:
        return "A missao apresentou tendencia de MELHORA."
    else:
        return "A missao permaneceu ESTAVEL em relacao ao inicio."


def identificar_area_mais_afetada(pontos_por_area):
    """Identifica a area com maior pontuacao acumulada de risco."""
    max_pontos = max(pontos_por_area)
    indice = pontos_por_area.index(max_pontos)
    return areas_monitoradas[indice], max_pontos


def gerar_relatorio_final(riscos, pontos_por_area, ciclo_critico, medias):
    """Exibe o relatorio final consolidado da missao."""
    tendencia = analisar_tendencia(riscos)
    area_afetada, pts_area = identificar_area_mais_afetada(pontos_por_area)
    risco_medio = sum(riscos) / len(riscos)
    qtd_criticos = sum(1 for r in riscos if r >= 6)
    classificacao_final = classificar_ciclo(risco_medio)

    print("\n" + "=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao : {NOME_MISSAO}")
    print(f"Equipe : {NOME_EQUIPE}")
    print(f"Integrantes:")
    print(f"  Felipe Elze da Silva      - RM: 572024")
    print(f"  Henrique Eduardo da Silva - RM: 571803")
    print(f"\nQuantidade de ciclos analisados: {len(riscos)}")
    print(f"\nMedias dos parametros monitorados:")
    print(f"  Media de temperatura  : {medias[0]:.2f} C")
    print(f"  Media de comunicacao  : {medias[1]:.2f}%")
    print(f"  Media de bateria      : {medias[2]:.2f}%")
    print(f"  Media de oxigenio     : {medias[3]:.2f}%")
    print(f"  Media de estabilidade : {medias[4]:.2f}%")
    print(f"\nCiclo mais critico    : Ciclo {riscos.index(max(riscos)) + 1}")
    print(f"Maior pontuacao de risco: {max(riscos)}")
    print(f"Risco medio da missao : {risco_medio:.2f}")
    print(f"Ciclos criticos       : {qtd_criticos}")
    print(f"\nTendencia da missao:")
    print(f"  {tendencia}")
    print(f"\nPontuacao acumulada por area:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontos_por_area[i]} pontos")
    print(f"\nArea mais afetada:")
    print(f"  {area_afetada} ({pts_area} pontos)")
    print(f"\nClassificacao final da missao:")
    print(f"  {classificacao_final}")
    print(f"\nConclusao:")
    if qtd_criticos == 0:
        print("  A missao transcorreu de forma controlada. Todos os sistemas")
        print("  operaram dentro dos parametros aceitaveis.")
    elif qtd_criticos <= 2:
        print("  A missao apresentou instabilidade em alguns ciclos.")
        print("  A equipe deve manter monitoramento e plano de contingencia ativo.")
    else:
        print("  A missao enfrentou multiplos ciclos criticos.")
        print("  Recomenda-se revisao completa dos sistemas antes de nova operacao.")
    print("=" * 60)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    print("=" * 60)
    print("        MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missao : {NOME_MISSAO}")
    print(f"Equipe : {NOME_EQUIPE}")
    print(f"Integrantes:")
    print(f"  Felipe Elze da Silva      - RM: 572024")
    print(f"  Henrique Eduardo da Silva - RM: 571803")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)

    # Acumuladores
    riscos          = []
    pontos_por_area = [0, 0, 0, 0, 0]
    soma_colunas    = [0, 0, 0, 0, 0]

    for i, ciclo in enumerate(dados_missao):
        temp, com, bat, oxi, est = ciclo

        # Analise individual de cada sensor
        r_temp = analisar_temperatura(temp)  + ("Temperatura interna",)
        r_com  = analisar_comunicacao(com)   + ("Comunicacao com a base",)
        r_bat  = analisar_bateria(bat)       + ("Sistema de energia",)
        r_oxi  = analisar_oxigenio(oxi)      + ("Suporte de oxigenio",)
        r_est  = analisar_estabilidade(est)  + ("Estabilidade operacional",)

        resultados = [r_temp, r_com, r_bat, r_oxi, r_est]

        # Calculo do risco do ciclo
        pontuacao = sum(r[1] for r in resultados)
        riscos.append(pontuacao)

        # Acumula pontos por area
        for j, r in enumerate(resultados):
            pontos_por_area[j] += r[1]

        # Acumula valores para media
        for j, val in enumerate(ciclo):
            soma_colunas[j] += val

        # Classificacao e recomendacao
        classificacao = classificar_ciclo(pontuacao)
        recomendacao  = gerar_recomendacao(resultados)

        # Exibicao do ciclo
        print(f"\nCICLO {i + 1}")
        print("-" * 60)
        print(f"Temperatura  : {temp} C   | {r_temp[0]:<8} | {r_temp[2]}")
        print(f"Comunicacao  : {com}%  | {r_com[0]:<8} | {r_com[2]}")
        print(f"Bateria      : {bat}%  | {r_bat[0]:<8} | {r_bat[2]}")
        print(f"Oxigenio     : {oxi}%  | {r_oxi[0]:<8} | {r_oxi[2]}")
        print(f"Estabilidade : {est}%  | {r_est[0]:<8} | {r_est[2]}")
        print(f"\nPontuacao de risco do ciclo: {pontuacao}")
        print(f"Classificacao do ciclo     : {classificacao}")
        print(f"Recomendacao               : {recomendacao}")

    # Medias finais
    medias = [soma_colunas[j] / len(dados_missao) for j in range(5)]

    # Relatorio final
    gerar_relatorio_final(riscos, pontos_por_area, riscos.index(max(riscos)), medias)


if __name__ == "__main__":
    main()

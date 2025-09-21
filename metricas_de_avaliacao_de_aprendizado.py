def calcular_metricas(vp, vn, fp, fn):
    """
    Calcula as principais métricas de avaliação para um modelo de classificação.

    Args:
        vp (int): Verdadeiros Positivos
        vn (int): Verdadeiros Negativos
        fp (int): Falsos Positivos
        fn (int): Falsos Negativos

    Returns:
        dict: Um dicionário contendo Acurácia, Precisão, Sensibilidade (Recall),
              Especificidade e F-score.
    """
    metricas = {}
    total_populacao = vp + vn + fp + fn

    # 1. Acurácia
    if total_populacao > 0:
        metricas["Acurácia"] = (vp + vn) / total_populacao
    else:
        metricas["Acurácia"] = 0.0

    # 2. Precisão
    # Evita divisão por zero se o modelo nunca previu casos positivos
    if (vp + fp) > 0:
        metricas["Precisão"] = vp / (vp + fp)
    else:
        metricas["Precisão"] = 0.0

    # 3. Sensibilidade (Recall)
    # Evita divisão por zero se não houver casos positivos reais
    if (vp + fn) > 0:
        metricas["Sensibilidade (Recall)"] = vp / (vp + fn)
    else:
        metricas["Sensibilidade (Recall)"] = 0.0

    # 4. Especificidade
    # Evita divisão por zero se não houver casos negativos reais
    if (vn + fp) > 0:
        metricas["Especificidade"] = vn / (vn + fp)
    else:
        metricas["Especificidade"] = 0.0

    # 5. F-score
    precisao = metricas["Precisão"]
    sensibilidade = metricas["Sensibilidade (Recall)"]
    # Evita divisão por zero se precisão e sensibilidade forem zero
    if (precisao + sensibilidade) > 0:
        metricas["F-score"] = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)
    else:
        metricas["F-score"] = 0.0

    return metricas

if __name__ == "__main__":
    # Cenário 1: Filtro de Spam (Modelo Ruim)
    print("--- Cenário 1: Filtro de Spam (Modelo Ruim) ---")
    spam_vp = 0
    spam_vn = 1
    spam_fp = 7
    spam_fn = 17
    resultados_spam = calcular_metricas(spam_vp, spam_vn, spam_fp, spam_fn)

    for metrica, valor in resultados_spam.items():
        # Imprime o resultado formatado como porcentagem
        print(f"{metrica}: {valor:.2%}")

    print("\n" + "="*50 + "\n")

    # Cenário 2: Teste Médico (Modelo Especializado)
    print("--- Cenário 2: Teste Médico (Modelo Especializado) ---")
    medico_vp = 95
    medico_vn = 5
    medico_fp = 10
    medico_fn = 1
    resultados_medico = calcular_metricas(medico_vp, medico_vn, medico_fp, medico_fn)

    for metrica, valor in resultados_medico.items():
        # Imprime o resultado formatado como porcentagem
        print(f"{metrica}: {valor:.2%}")

import numpy as np


def fator_umidade(h):
    f = 1.0 - ((h - 70.0) / 30.0) ** 2
    return np.clip(f, 0.0, 1.0)


def fator_temperatura(t):
    t_opt = 28.0
    c = 8.0
    return np.exp(-((t - t_opt) ** 2) / (2 * c ** 2))


def fator_luminancia(luz):
    k = 0.005
    return 1.0 - np.exp(-k * luz)


def fator_uv(uv):
    uv_limite = 5.0
    taxa_dano = 0.4
    if uv <= uv_limite:
        return 1.0
    else:
        return np.exp(-taxa_dano * (uv - uv_limite))


def calcular_crescimento_real(taxa_potencial_maxima, h, t, luz, uv):
    f_h = fator_umidade(h)
    f_t = fator_temperatura(t)
    f_l = fator_luminancia(luz)
    f_uv = fator_uv(uv)

    crescimento_real = taxa_potencial_maxima * f_h * f_t * f_l * f_uv
    return crescimento_real, f_h, f_t, f_l, f_uv


if __name__ == "__main__":
    G_POTENCIAL = 15.0

    print("=== SIMULADOR DE DESENVOLVIMENTO AGRONÔMICO ===")
    print("Insira as variáveis do ambiente atual:\n")

    try:
        sensor_umidade = float(input("Umidade Relativa (%): "))
        sensor_temperatura = float(input("Temperatura (°C): "))
        sensor_luz = float(input("Luminância (W/m²): "))
        sensor_uv = float(input("Índice UV: "))

        cresc_real, fh, ft, fl, fuv = calcular_crescimento_real(
            G_POTENCIAL,
            sensor_umidade,
            sensor_temperatura,
            sensor_luz,
            sensor_uv
        )

        print("\n=== DIAGNÓSTICO DO DESENVOLVIMENTO ===")
        print(f"Condição ideal esperada: {G_POTENCIAL} g/dia\n")
        print("Fatores Ambientais (1.0 = Perfeito, < 1.0 = Perda por estresse):")
        print(f"- Umidade      : {fh:.2f}")
        print(f"- Temperatura  : {ft:.2f}")
        print(f"- Luminância   : {fl:.2f}")
        print(f"- Índice UV    : {fuv:.2f}\n")
        print(f"CRESCIMENTO REAL CALCULADO: {cresc_real:.2f} g/dia")

    except ValueError:
        print("\nErro de entrada: O sistema aceita apenas valores numéricos. Tente novamente.")
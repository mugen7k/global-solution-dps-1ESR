# Modelagem Matemática Orbitária Aplicada ao Desenvolvimento Agrícola

 Telfort | ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![NumPy](https://img.shields.io/badge/NumPy-1.26.4-darkgreen) ![WeasyPrint](https://img.shields.io/badge/WeasyPrint-61.0-blueviolet)

Este repositório contém o projeto desenvolvido para a **Global Solution 2026** na disciplina de **Differentiated Problem Solving** do curso de Engenharia de Software da FIAP. O objetivo é aplicar conceitos de funções matemáticas e programação em Python para resolver problemas reais na Terra utilizando infraestruturas da Indústria Espacial.

## 🌌 Contexto Espacial e Agronómico

O projeto simula a taxa de crescimento diário da cultura da soja (*Glycine max*) tirando partido do **Sensoriamento Remoto Satelital**. Em vez de depender de sensores físicos dispendiosos no solo, o modelo utiliza dados climáticos que podem ser integralmente extraídos ou inferidos através de constelações de satélites em órbita terrestre baixa (LEO), como *Landsat*, *Sentinel* e *SMAP*.

O algoritmo integra quatro funções matemáticas distintas baseadas na **Lei do Mínimo de Liebig**, operando de forma multiplicativa para determinar o impacto ecológico na planta.

---

## 📐 O Modelo Matemático

Cada variável ambiental foi modelada utilizando uma família de funções específicas, normalizadas para retornar um fator de eficácia entre `0.0` (paragem metabólica) e `1.0` (ótimo fisiológico):

1. **Umidade Relativa ($h$):** Função Polinomial Quadrática (Parábola com concavidade para baixo), estabelecendo o pico ideal em 70%.
2. **Temperatura da Superfície ($t$):** Função Exponencial Composta (Curva Gaussiana), modelando a cinética enzimática com centro em 28°C.
3. **Luminância PAR ($luz$):** Função Exponencial Assintótica, representando a curva de saturação dos fotossistemas da planta.
4. **Radiação UV ($uv$):** Função de Decaimento Exponencial com Limiar (*Threshold*), onde o stresse celular começa a ser computado apenas acima do Índice UV 5.

A equação final do sistema é dada por:

$$\text{Crescimento Real} = G_{\text{potencial}} \times G(h) \times F(t) \times P(luz) \times D(uv)$$
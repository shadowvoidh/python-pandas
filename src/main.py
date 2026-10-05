import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# Parte 2.1 - Criar a tabela
# ==========================================
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fábio", "Gabi", "Hugo"],
    "turma": [" A", "B ", "A", " B", "A ", "B", " A ", "B"],
    "idade": [15, 16, np.nan, 15, 17, np.nan, 16, 15],
    "peso": [52.0, 68.5, 55.0, np.nan, 60.2, 75.0, np.nan, 58.0],
    "altura": [1.60, 1.75, 1.62, 1.70, np.nan, 1.80, 1.58, np.nan],
}
df = pd.DataFrame(dados)

# ==========================================
# Exercício 1 - Consultar a tabela
# ==========================================
print("--- Exercício 1 ---")
print(df[["nome", "altura"]])
print("\nAlunos com altura > 1.65m:")
print(df[df["altura"] > 1.65])
print("\nValores vazios por coluna:")
print(df.isna().sum())

# ==========================================
# Exercício 2 - Limpar espaços em branco
# ==========================================
print("\n--- Exercício 2 ---")
print("Turmas antes do strip:", df["turma"].unique())
df["turma"] = df["turma"].str.strip()
print("Turmas depois do strip:", df["turma"].unique())

# ==========================================
# Exercício 3 - Tratar valores vazios
# ==========================================
print("\n--- Exercício 3 ---")
copia_drop = df.copy().dropna()
print(f"Alunos sobraram com dropna(): {len(copia_drop)}")

limpo = df.copy()
limpo["idade"] = limpo["idade"].fillna(limpo["idade"].median())
limpo["peso"] = limpo["peso"].fillna(limpo["peso"].mean())
limpo["altura"] = limpo["altura"].fillna(limpo["altura"].mean())
print(f"Alunos mantidos com fillna(): {len(limpo)}")

# ==========================================
# Exercício 4 - Trocar dados
# ==========================================
limpo["turma_num"] = limpo["turma"].map({"A": 1, "B": 2})
limpo = limpo.replace({"nome": {"Hugo": "Hugo S."}})

# ==========================================
# Exercício 5 - Gerar gráficos
# ==========================================
limpo["imc"] = limpo["peso"] / (limpo["altura"] ** 2)

# Histograma
plt.hist(limpo["peso"], bins=5)
plt.title("Distribuição de Peso")
plt.xlabel("Peso (kg)")
plt.ylabel("Quantidade de Alunos")
plt.show()

# Dispersão
plt.scatter(limpo["altura"], limpo["peso"])
plt.title("Relação entre Altura e Peso")
plt.xlabel("Altura (m)")
plt.ylabel("Peso (kg)")
plt.show()

# Barras
limpo.groupby("turma")["peso"].mean().plot(kind="bar")
plt.title("Peso Médio por Turma")
plt.xlabel("Turma")
plt.ylabel("Peso Médio (kg)")
plt.show()

# ==========================================
# Desafio - Classificar pelo IMC
# ==========================================
limpo["categoria_imc"] = pd.cut(
    limpo["imc"],
    bins=[0, 18.5, 25, np.inf],
    labels=["abaixo", "normal", "acima"],
)

contagem_imc = limpo["categoria_imc"].value_counts()
plt.bar(contagem_imc.index, contagem_imc.values)
plt.title("Alunos por Categoria de IMC")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")
plt.show()
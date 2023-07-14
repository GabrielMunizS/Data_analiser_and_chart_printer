import pandas as pd
import ast
import matplotlib.pyplot as plt

# O programa lê o banco de dados e "printa" a quantidade de linhas(filmes) que há
Leitura_braba = pd.read_csv('credits.csv')

print(f'Nûmero de filmes na base de dados: {len(Leitura_braba)}')

# O programa lê o banco de dados e vê a quantidade de Gênero que existem sendo contado por qual Gênero aparece e por cada vez que um Gênero aparece

Genero = pd.read_csv("movies_metadata.csv")

Genero['genres'] = Genero['genres'].apply(ast.literal_eval,)
def get_genres(genres):
  return [n['name'] for n in genres]

Genero['genres'] = Genero['genres'].apply(get_genres)
genres = pd.Series(sum(Genero['genres'], [])).value_counts()

# Converte a coluna release_date de string para datetime fazendo possivel utilizar dt.year.min() e dt.year.max() entregando o dia de lançamento fazendo

Leitura_braba = pd.read_csv('movies_metadata.csv')
Leitura_braba['release_date'] = pd.to_datetime(Leitura_braba['release_date'], format='%Y-%m-%d', errors='coerce')

# Obtém o ano mínimo e máximo da coluna release_date
Ano_minimo = Leitura_braba['release_date'].dt.year.min()
Ano_maximo = Leitura_braba['release_date'].dt.year.max()


# Obtém a média da coluna vote_average
Media_grafico = Leitura_braba['vote_average'].mean()


# Exibe os valores

print(f'Nûmero de filmes na base de dados: {len(Leitura_braba)}')

print(f'Quantidade de filmes por gênero:')

print(genres)

print(f'Ano de lançamento mais antigo: {Ano_minimo}')

print(f'Ano de lançamento mais recente: {Ano_maximo}')

print(f'Média da avaliação de todos os filmes: {round(Media_grafico, 2)}')

#criando graficos
Cor = "red"
plt.figure(figsize=(20, 6))
plt.bar(genres.index[:10], genres.values[:10], color=Cor)
plt.title('10 gêneros com mais filmes')
plt.xlabel('Gênero')
plt.ylabel('Filmes')
plt.show()

plt.figure(figsize=(20, 6))
plt.hist(Leitura_braba['release_date'].dt.year, bins=12)
plt.title('Distribuição dos anos de lançamento')
plt.xlabel('Ano')
plt.ylabel('Quantidade(filmes)')
plt.show()

#Importar bibliotecas
import pandas as pd

#Extrair os IDs do arquivo CSV
df = pd.read_csv("SDW2023.csv")
user_ids = df['UserID'].tolist()
print(user_ids)
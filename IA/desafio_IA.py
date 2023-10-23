#Importar bibliotecas
import pandas as pd

#-------------------------------------------------------------------------

#Extrair os IDs do arquivo CSV
df = pd.read_csv("SDW2023.csv")
user_ids = df['UserID'].tolist()
print(user_ids)

from IPython.core.async_helpers import indent
#Obter os dados de cada ID usando a API da Santander Dev Week 2023
import requests
import json

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print (json.dumps(users, indent = 2))

#-------------------------------------------------------------------------------

# Instalar openai
# Documentação Oficial da API OpenAI: https://platform.openai.com/docs/api-reference/introduction
# Informações sobre o Período Gratuito: https://help.openai.com/en/articles/4936830

# Para gerar uma API Key:
# 1. Crie uma conta na OpenAI
# 2. Acesse a seção "API Keys"
# 3. Clique em "Create API Key"
# Link direto: https://platform.openai.com/account/api-keys

# Substitua o texto TODO por sua API Key da OpenAI, ela será salva como uma variável de ambiente.
openai_api_key = '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'

#Implementar a integração com CHATGPT usando o modelo GPT-4

import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          #"content": "Você é um especialista em marketing bancário."
          "content": "Você é um especialista em enconomia."
      },
      {
          "role": "user",
          #"content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
          "content": f"Crie uma mensagem para {user['name']} como administrar da melhor forma os ganhos mensais (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Atualizar os dados
def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")


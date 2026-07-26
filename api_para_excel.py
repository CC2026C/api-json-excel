import pandas as pd
import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

resposta = requests.get(url)

df = pd.DataFrame(resposta.json())

df = df[["sigla", "nome", "regiao"]]
df["regiao"] = df["regiao"].apply(lambda x: x["nome"])

df.columns = ["UF", "Estado", "Regiao"]

df.to_excel("estados_br.xlsx", index=False)

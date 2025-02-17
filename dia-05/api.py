
# %%
import requests

url = "https://api.opendota.com/api/heroes"

resposta = requests.get(url)


# %%

resposta.status_code
# %%

dados = resposta.json()
# %%

dados
# %%

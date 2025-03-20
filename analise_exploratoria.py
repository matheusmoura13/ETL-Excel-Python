# Importar biblioteca pandas para ler o arquivo e transformar em DataFrame
import pandas as pd

# pandas profile (ydata_profiling)
from ydata_profiling  import ProfileReport

df = pd.read_csv('Jornada de Dados 2024 _ BD Teste - meta_ads_criativos.csv')
profile = ProfileReport(df, title='Profiling Report', explorative=True)
profile.to_file("output.html")
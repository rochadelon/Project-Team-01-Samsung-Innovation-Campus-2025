import urllib
import pandas as pd #dataframes
import seaborn as sns #gráficos
import matplotlib.pyplot as plt
import glob #localizar arquivos

### Importando os dados ###


extension = 'csv'
# Caminho correto com a pasta e a extensão
all_filenames = glob.glob('/workspaces/Project-Team-01-Samsung-Innovation-Campus-2025/data/*.{}'.format(extension))

df_ouvidoria_aneel = pd.concat([
    pd.read_csv(f, encoding='latin1', sep=';', on_bad_lines='skip') 
    for f in all_filenames
])


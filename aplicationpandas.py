import pandas as pd

#DataFrame apartir de um dicionário
clientes = {
    'nome' : ['Gabriel', 'Joaquim'], 'data_nasc' : ['13/05/2001', '14/05/2001'],
}
clientes_df = pd.DataFrame(clientes)

#Transformando uma base de dados excel em um DataFrame
base_df = pd.read_excel("D:\Pandas\estimativa_dou_2021.xlsx")
print(base_df.describe())


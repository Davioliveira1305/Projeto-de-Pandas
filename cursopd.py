import pandas as pd

#leitura do dataset
data = pd.read_csv('D:\Pandas\GasPricesinBrazil_2004-2019.csv', sep=';')

#Função que mostra a qtd de linhas que o usuário deseja mostra do DataFrame
##print(data.head(10))

#Função que mostra informaçãoes do DataFrame
##data.info()

#Criando um DataFrame
#DataFrame apartir de um dicionário
clientes = {
    'nome' : ['Gabriel', 'Joaquim'], 'data_nasc' : ['13/05/2001', '14/05/2001'],
}
clientes_df = pd.DataFrame(clientes)

#Renomeando o nome das colunas do DataFrame(fazendo uma cópia)
clientes_df_renomeado = clientes_df.rename(columns={'nome' : 'Nome', 'data_nasc' : 'data_de_nascimento'})

#Renomeando o nome das colunas do DataFrame(no mesmo DataFrame)
clientes_df.rename(columns={'nome' : 'Nome', 'data_nasc' : 'data_de_nascimento'}, inplace=True)

#Renomeando o nome das colunas do DataFrame apartir de uma lista
clientes_df.columns = ['NOME', 'DATA_NASC']

#Selecionando uma determinada coluna do DataFrame
data['ESTADO']

#Selecionando uma determinada linha do DataFrame
data.iloc[0]

#Criando Series
serie = pd.Series([12.5,6.7,3.2],index=['Prova1','Prova2','Prova3'], name='Notas do aluno joãozinho')

#Serie do DataFrame passado como referência(view)
product_view = data['PRODUTO']

#Serie do DataFrame passado como uma cópia
product_copy = data['PRODUTO'].copy()

#Atribuindo listas ou series
nrows, ncols = data.shape
new_products = [f'Produsct{i}' for i in range(nrows)]
data['PRODUTO'] = product_copy

#Criando uma coluna a partir de um valor constante/default
data['DANDA PEIDO'] = 'DEFAULT'
data['PREÇO MÉDIO REVENDA(EM DOLÁRES)'] = data['PREÇO MÉDIO REVENDA'] * 5.0

#Índices
times_socios = pd.DataFrame({'AVALIAÇÃO' : ['BOM', 'BOM'], 'QTD_SÓCIOS' : [67000, 65757]}, 
                            index=['CEARÁ', 'stella'])




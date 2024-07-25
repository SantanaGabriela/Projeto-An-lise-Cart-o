import streamlit as st
import pandas as pd
import plotly.express as px
import plotting


#Carregando Dados
df = pd.read_csv('cartao.csv')

#converter a colina NumCartao para os nomes dos titulores dos cartões
df['Titular' ] = df['NumCartao'].map({
    7840517590708225: 'Gabriela Santana',
    7142474765870246: 'Eduardo Aguiar'

})

#convertendo a coluna da  numeração do cartão para uma string(str)
df['NumCartao'] = df['NumCartao'].astype(str)

#converter a coluna data_compra para datatime(o formato da data para o formato brasileiro

df['data'] = pd.to_datetime(df['data'])
valor_total = df['ValorCompra'].sum()



##Análise de Dados

#valor gasto de categoria por mês e por titular: 

gasto_categoria_gabriela_junho = df[(df['Titular'] == 'Gabriela Santana')& (df['data'].dt.month == 6) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_eduardo_junho = df[(df['Titular'] == 'Eduardo Aguiar')& (df['data'].dt.month == 6) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_gabriela_maio = df[(df['Titular'] == 'Gabriela Santana')& (df['data'].dt.month == 5) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_eduardo_maio = df[(df['Titular'] == 'Eduardo Aguiar')& (df['data'].dt.month == 5) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_gabriela_abril = df[(df['Titular'] == 'Gabriela Santana')& (df['data'].dt.month == 4) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_eduardo_abril = df[(df['Titular'] == 'Eduardo Aguiar')& (df['data'].dt.month == 4) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_gabriela_marco = df[(df['Titular'] == 'Gabriela Santana')& (df['data'].dt.month == 3) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_eduardo_marco = df[(df['Titular'] == 'Eduardo Aguiar')& (df['data'].dt.month == 3) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_gabriela_fevereiro = df[(df['Titular'] == 'Gabriela Santana')& (df['data'].dt.month == 2) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_eduardo_fevereiro = df[(df['Titular'] == 'Eduardo Aguiar')& (df['data'].dt.month == 2) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_gabriela_janeiro = df[(df['Titular'] == 'Gabriela Santana')& (df['data'].dt.month == 1) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()
gasto_categoria_eduardo_janeiro = df[(df['Titular'] == 'Eduardo Aguiar')& (df['data'].dt.month == 1) & (df['data'].dt.year == 2024)].groupby('categoria')['ValorCompra'].sum().reset_index()



#Configurando pagina Streamlit

st.set_page_config(layout= 'wide')
st.title('Análise De Compras No Cartão De Crédito')


#Menu lateral:
st.sidebar.title('Análise Cartão de Crédito')
PaginaSelecionada=st.sidebar.selectbox("Selecione o titular da Conta", ['Gabriela Santana', 'Eduardo Aguiar'])

#Função para condicional da página  selecionada
def visualiza_dados_gabriela():
    st.header(f'Olá, {PaginaSelecionada}! Visualize seus gastos por mês')
    mes_selecionado =  st.selectbox("Selecione o mês", ["Junho", "Maio", "Abril", "Março", "Fevereiro","Janeiro"] )
    
    if mes_selecionado == "Junho":
        #st.write(f'Valor Total Gasto :R$ {valor_total_gasto_jun:.2f}')
        fig = px.bar(gasto_categoria_gabriela_junho, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)

    elif mes_selecionado == "Maio":
       fig = px.bar(gasto_categoria_gabriela_maio, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
       st.plotly_chart(fig)
    elif mes_selecionado == "Abril":
        fig = px.bar(gasto_categoria_gabriela_abril, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)
    elif mes_selecionado == "Março":
         fig = px.bar(gasto_categoria_gabriela_marco, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
         st.plotly_chart(fig)
    elif mes_selecionado == "Fevereiro":
         fig = px.bar(gasto_categoria_gabriela_fevereiro, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
         st.plotly_chart(fig)
    elif mes_selecionado == "Janeiro":
         fig = px.bar(gasto_categoria_gabriela_janeiro, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
         st.plotly_chart(fig)

def visualiza_dados_eduardo():
    st.header(f'Olá, {PaginaSelecionada}! Visualize seus gastos por mês')
    mes_selecionado =  st.selectbox("Selecione o mês", ["Junho", "Maio", "Abril", "Março", "Fevereiro","Janeiro"] )
    
    if mes_selecionado == "Junho":
        #st.write(f'Valor Total Gasto :R$ {valor_total_gasto_jun:.2f}')
        fig = px.bar(gasto_categoria_eduardo_junho, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)

    elif mes_selecionado == "Maio":
       fig = px.bar(gasto_categoria_eduardo_maio, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
       st.plotly_chart(fig)
    elif mes_selecionado == "Abril":
        fig = px.bar(gasto_categoria_eduardo_abril, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)
    elif mes_selecionado == "Março":
         fig = px.bar(gasto_categoria_eduardo_abril, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
         st.plotly_chart(fig)
    elif mes_selecionado == "Fevereiro":
         fig = px.bar(gasto_categoria_eduardo_fevereiro, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
         st.plotly_chart(fig)
    elif mes_selecionado == "Janeiro":
         fig = px.bar(gasto_categoria_eduardo_janeiro, x='categoria', y='ValorCompra', title=f'Gastos por Categoria em {mes_selecionado}',color='categoria', color_discrete_sequence=px.colors.qualitative.Pastel)
         st.plotly_chart(fig)



#Condição Menu Lateral
if PaginaSelecionada =='Gabriela Santana':
    visualiza_dados_gabriela()
   

elif PaginaSelecionada =='Eduardo Aguiar':
    visualiza_dados_eduardo()



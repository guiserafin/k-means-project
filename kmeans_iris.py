#Importando as bibliotecas que serão utilizadas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as rd

def cluster(titulo, dados,eixo_x, eixo_y, eixo_z = False):
    # Passo 1 e 2 - Escolher um numero de clusters (k) e selecionar um centroide aleatorio para cada cluster

    # No nosso caso o numero de clusters sempre será 3, já que temos 3 classes de flores, Setosa, Versicolor e Virginica
    K = 3

    # Selecionar pontos de observação aleatórios como centroides
    Centroids = (dados.sample(n=K)) #Pega n amostras aleatorias (n = K)

    plt.scatter(dados[eixo_x], dados[eixo_y], c='black') #coloca os pontos no grafico

    plt.scatter(Centroids[eixo_x], Centroids[eixo_y], c='red') #Colore os centroides aleatorios com a cor vermelha

    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)
    plt.show()

    # Observe que os centroides escolhidos são aleatorios

    # Passo 3 - Atribui todos os pontos ao centroide de cluster mais próximo
    # Passo 4 - Recomputar centroides de clusters recém-formados
    # Passo 5 - Repetir Passo 3 e 4
    
    # Podemos parar de repetir os passos 3 e 4 quando um dos seguintes critérios for atendido:
        # 1 - Centroides dos clusters recém-formados não alteram
        # 2 - Pontos permanecem no mesmo cluster
        # 3 - Um número maximo arbitrário de iterações foi alcançado

diff = 1 # Acho que é a variável que vai ficar de olho se o nossos centroides recem formados alteram ou não
j=0

while(diff!=0):
    XD=dados
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c[eixo_x]-row_d[eixo_x])**2
            d2=(row_c[eixo_y]-row_d[eixo_y])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        dados[i]=ED
        i=i+1

    C=[]
    for index,row in dados.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    dados["Cluster"]=C
    Centroids_new = dados.groupby(["Cluster"]).mean()[[eixo_y,eixo_x]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
        print(diff.sum())
    Centroids = dados.groupby(["Cluster"]).mean()[[eixo_y,eixo_x]]

    return

#objeto dados - csv lido pelo pandas
dados = pd.read_csv('iris.csv') 

dados.head()

#Na primeira tabela, vamos separar as flores por classe e demonstrar a amostragem de cada classe que temos no nosso csv
contagem_flores = dados['variety'].value_counts()

contagem_flores.plot(kind="bar", color=['blue', 'red', 'green'])

plt.title("Quantidade de cada flor presente no csv")
plt.xlabel("Classes")
plt.ylabel("Quantidade")

plt.show()


#Agora, plotaremos 4 graficos, separando as flores em cada propriedade que esta no csv, ou seja, largura e comprimento da petala, e largura e comprimento da sepala
# e vamos fazer o clustering de cada grafico

cluster("Sepalas", dados, "sepal.length", "variety")

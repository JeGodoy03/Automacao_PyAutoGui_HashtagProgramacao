#Passo a passo do seu programa
#Passo 1: entrar no sistema da empresa
#abriria o navegador
#Passo 2: Fazer login
#Passo 3: Abrir a base de dados
#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

pyautogui.click(x=242, y=81)
pyautogui.write(link) 
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=658, y=511)
pyautogui.write('pythonimpressionador@gmail.com')
pyautogui.press('tab') 
pyautogui.write('jess123')
pyautogui.press('tab') 
pyautogui.press('enter')

time.sleep(2)

import pandas 

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=732, y=367)
    codigo = str(tabela.loc[linha, 'codigo'])
    
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)

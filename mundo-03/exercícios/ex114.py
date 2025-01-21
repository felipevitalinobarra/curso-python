"""
Enunciado do Exercício:
    Crie um código em Python que teste se o site Pudim (www.pudim.com.br) está acessível pelo computador usado.
"""

import requests

def verificar_site():
    try:
        resposta = requests.get('http://pudim.com.br', timeout=5)
        if resposta.status_code == 200:
            print('\033[1;32mO site pudim está acessível!\033[m')
        else:
            print(f'\033[1;31mO site Pudim não está acessível. Código de status: {resposta.status_code}\033[m')
    except requests.ConnectionError:
        print('\033[1;31mErro! Não foi possível conectar ao site Pudim.\033[m')
    except requests.Timeout:
        print('\033[1;31mErro! A conexão com o site Pudim demorou muito para responder.\033[m')
    except Exception as e:
        print(f'\033[1;31mErro inesperado: {e}\033[m')

if __name__ == '__main__':
    verificar_site()
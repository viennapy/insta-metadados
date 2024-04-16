import instaloader
import os
from time import sleep

loader = instaloader.Instaloader()


def postagem_usuario(nome_usuario): # BAIXAR POSTAGENS 
    try:
        loader.download_profile(nome_usuario, profile_pic_only=False)
        print('POSTEGENS BAIXADAS...')
    except instaloader.exceptions.ProfileNotExistsException:
        print('Perfil não encontrado.')
    except instaloader.exceptions.ConnectionException:
        print('Falha na conexão...')
    except Exception as e:
        print('Ocorreu um erro inesperado:', e)

opção = 0
sleep(1)

# PARTE 1 >

while opção != 4:
    print('============ ESCOLHA UMA OPÇÃO ============')
    print('   [ 1 ] ANALISAR O PERFIL >               |') 
    print('   [ 2 ] FAZER DOWNLOAD DE POSTS >         |')
    print('   [ 3 ] LIMPAR O TERMINAL >               |')
    print('   [ 4 ] SAIR DO PROGRAMAR >               |') 
    print('=================   X    ==================')
    opção = int(input('ESCOLHA UMA OPÇÃO: '))
    sleep(1)

    if opção == 1:  # ANALISA O PERFIL
        usuario = input('DIGITE O NOME DO PERFIL: ').lower()

        try:
            perfil = instaloader.Profile.from_username(loader.context, usuario)

            print('ID DO PERFIL: ', perfil.userid)
            sleep(2)
            print('URL DA IMAGEM DO PERFIL: ', perfil.profile_pic_url)
            sleep(2)
            print('NOME DE USUÁRIO: ', perfil.username)
            sleep(2)
            print('SEGUNDO NOME: ', perfil.full_name)
            sleep(2)
            print('NÚMEROS DE SEGUIDORES: ', perfil.followers)
            sleep(2)
            print('ESTÁ SEGUINDO: ', perfil.followees)
            sleep(2)
            print('BIO: ', perfil.biography)
            sleep(2)
            print('NÚMERO DE PUBLICAÇÃO: ', perfil.mediacount)
            sleep(2)
            print('PRIVADO OU LIVRE: ', 'Privado' if perfil.is_private else 'Público')
            sleep(2)

        except instaloader.exceptions.ProfileNotExistsException:
            print('USUÁRIO NÃO ENCONTRADO.')
        except instaloader.exceptions.ConnectionException:
            print('FALHA NA CONEXÃO...')
        except Exception as e:
            print('OCORREU UM ERRO INESPERADO.', e)


    # PARTE 2 >
 
    if opção == 2: # DOWNLOAD DOS POSTS
        nome_usuario = input('DIGITE O NOME DO PERFIL: ')
        postagem_usuario(nome_usuario)

    
    # PARTE 3 >

    if opção == 3: # LIMPAR O TERMINAL...

        def limpar():
            sistema_operacional = os.name

            if sistema_operacional == 'posix': # LINUX ou MAC
                 os.system('clear')
        
            if sistema_operacional == 'nt': # WINDOWS
                 os.system('cls')
        
            else:
                print('O SISTEMA OPERACIONAL NÃO FOI ENCONTRADO :( ')
        
        limpar()


    # PARTE 4 >

    if opção == 4: # SAIR DO PROGRAMAR
        sleep(2)   
        print('VOCÊ SAIU DO PROGRAMAR...')
        sleep(2)
        break

print('OBRIGADO(A) POR USAR NOSSA FERRAMENTA :)')

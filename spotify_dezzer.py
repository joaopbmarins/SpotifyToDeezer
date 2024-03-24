import json
import requests
from keys_s_d import spotify_oauth
from keys_s_d import deezer_oauth

id_pl = []
id_ms = []
head_spotify = {'Accept': 'application/json', "Content-Type": "application/json",
                'Authorization': "Bearer " + spotify_oauth}
musicas_liked = []
sair = False


def spotify_liked():
    try:
        req = requests.get('https://api.spotify.com/v1/me/tracks?market=BR&limit=50&offset=0', headers=head_spotify)
        liked_songs = json.loads(req.text)
        total = int(liked_songs['total'])
        print(total)
        for i in range(0, total):
            musicas_liked.append(liked_songs['items'][i]['track']['name'])
    except Exception as err:
        print(err)


def criar_playlist(nome):
    try:
        req = requests.post(
            'https://api.deezer.com/user/me/playlists&access_token=' + deezer_oauth + '&title=' + nome)
        pl = json.loads(req.text)
        id_pl.append(pl['id'])
    except Exception as err:
        print(err)


def pesquisa_musica(nome_da_musica):
    for i in range(0, 50):
        try:
            req = requests.get('https://api.deezer.com/search/track?q=' + nome_da_musica[i])
            pes = json.loads(req.text)
            id_ms.append(pes['data'][0]['id'])
        except Exception as err:
            print(err)


def add_musica_pl(id_ms, id_pl):
    for i in range(0, 50):
        try:
            req = requests.post('https://api.deezer.com/playlist/' + str(
                id_pl[0]) + '/tracks&access_token=' + deezer_oauth + '&songs=' + str(
                id_ms[i]))
        except Exception as err:
            print(err)


while not sair:
    print('O que vc quer fazer:')
    print('1 Puxar musicas do spotify')
    print('2 Criar playlist pro deezer')
    print('3 Pesquisar uma musica no deezer')
    print('4 Colocar uma musica na playlist no deezer')
    print('5 Fechar')
    op = input('Escolha um numero: ')
    if op == '1':
        spotify_liked()
        print('Pronto\n')
    elif op == '2':
        nome_pl = input('Qual vai ser o nome dela: ')
        criar_playlist(nome_pl)
        print('Pronto\n')
    elif op == '3':
        pesquisa_musica(musicas_liked)
        print('Pronto\n')
    elif op == '4':
        add_musica_pl(id_ms, id_pl)
        print('Pronto\n')
    elif op == '5':
        print('Saindo...')
        sair = True

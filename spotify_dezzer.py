import json
import requests
import spotipy
import spotipy.util as util
from keys_s_d import deezer_oauth
from keys_s_d import spotify_userid
from keys_s_d import cli_id, cli_id_sec,url

total = ''
username = spotify_userid
scope = 'user-library-modify playlist-read-private user-library-read playlist-modify-private user-read-currently-playing user-read-private user-read-playback-state user-modify-playback-state'
id_pl = []
id_ms = []
musicas_liked = []
sair = False


def spotify_liked():
    token = util.prompt_for_user_token(username, scope, cli_id, cli_id_sec, url)
    spotifyObject = spotipy.Spotify(auth=token)
    results = spotifyObject.current_user_saved_tracks(50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        musicas_liked.append(track['name'])
    global total
    total = results['total']
    total_1 = int(total) - 50

    if total_1 > 50:
        results = spotifyObject.current_user_saved_tracks(50, 50)
        for idx, item in enumerate(results['items']):
            track = item['track']
        total_1 = total_1 - 50
    else:
        results = spotifyObject.current_user_saved_tracks(total_1, 50)
        for idx, item in enumerate(results['items']):
            track = item['track']
            musicas_liked.append(track['name'])


def criar_playlist(nome):
    try:
        req = requests.post(
            'https://api.deezer.com/user/me/playlists&access_token=' + deezer_oauth + '&title=' + nome)
        pl = json.loads(req.text)
        id_pl.append(pl['id'])
    except Exception as err:
        print(err)


def pesquisa_musica(nome_da_musica):
    for i in range(0, int(total)):
        try:
            req = requests.get('https://api.deezer.com/search/track?q=' + nome_da_musica[i])
            pes = json.loads(req.text)
            id_ms.append(pes['data'][0]['id'])
        except Exception as err:
            print('Erro ao encontrar a musica',err)


def add_musica_pl(id_ms, id_pl):
    for i in range(0, int(total)):
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
    print('5 Para digitar o ID da playlist que ira adicionar a musica')
    print('6 Fechar')
    op = input('Escolha um numero: ')
    if op == '1':
        spotify_liked()
        print('Pronto\n')
    elif op == '2':
        nome_pl = input('Qual vai ser o nome dela: ')
        criar_playlist(nome_pl)
        print(id_pl)
        print('Pronto\n')
    elif op == '3':
        pesquisa_musica(musicas_liked)
        print('Pronto\n')
    elif op == '4':
        add_musica_pl(id_ms, id_pl)
        print('Pronto\n')
    elif op == '5':
        op1 = input('Digite a ID da playlist para adicionar as musicas nela: ')
        id_pl.clear
        id_pl.append(op1)
        print('Pronto\n')
    elif op == '6':
        print('Saindo...')
        sair = True


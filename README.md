# SpotifyToDeezer

É um programa em python3 que passa uma playlist do Spotify (ou musicas favoritadas) para uma playlist no Deezer. Toda a parte de oauth2 é feita manualmente no deezer ou seja você precisa entregar a chave para o programa, entretanto para o spotify se utiliza muito uma biblioteca especifica que já tem todo o oauth2 automatizado. Fiz esse código no tédio da pandemia e provavelmente tem muitos erros bobos, mas funcionava razoavelmente bem.

## Requirements 
Instale a biblioteca externa Spotipy
```bash
pip install spotipy 
```
Crie um arquivo keys_s_d.py com nesse formato e preencha com suas informações.
```python
#Deezer
deezer_oauth = ''

#Spotify
spotify_userid = ''
url = ''
cli_id_sec= ''
cli_id = ''
```
## Usage
Execute o spotify_dezzer.py com o keys_s_d.py na mesma pasta e aparecerá um menu com cada função em ordem que deve é recomendado ser utilizada. Se você está utilizando pela primeira vez o Spotipy vai pedir que você conecte com a conta do spotify em seguida abre uma pagina no navegador para isso e quando terminar de autenticar no navegador você deve copiar o link final para o programa para que assim o spotipy consiga a oauth do spotify, nas proximas vezes isso não deve ser necessário. 

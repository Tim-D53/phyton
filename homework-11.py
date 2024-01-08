import requests

api_key = "8eiVkPHVCgADpmWVeyNFHesJCBuKLxAr"
name_gif = input("gif name: ")

resp = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={name_gif}&limit=5')

data = resp.json()

for gif in data['data']:
    gif_url = gif['images']['downsized']['url']
    print(gif_url)

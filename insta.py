import httpx
import json
def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "YOUR KEY",
        "X-RapidAPI-Host": "YOUR HOST"
    }

    response = httpx.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:
        dict={}
        if rest['Type'] == 'Post-Image':
            dict['type']='image'
            dict['type']=rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media']=rest['media']
            return dict
        elif rest['Type'] == 'Carusel':
            dict['type'] = 'carusel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'


import requests

def get_cat_images(api_key):
    url = 'https://api.thecatapi.com/v1/images/search'
    h = {'x-api-key': api_key}
    try:
        cat_image = requests.get(url, headers=h ).json()
        return cat_image
    except:
        #Log to container stdout
        print ('Error getting image in cats API')
        return False
    
def get_cats_info():
    return (requests.get('https://cat-fact.herokuapp.com/facts').json())['all']
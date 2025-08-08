import requests

def authenticate(CLIENT_ID,SECRET_ID,PASSWORD,REDDIT_USERNAME):
    # Use HTTPBasicAuth to authenticate with Reddit
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_ID)

    data = {
        'grant_type': 'password',
        'username': REDDIT_USERNAME,
        'password': PASSWORD
    }
    
    headers = {
        'User-Agent': 'PoliticalLeanings/0.1'
        }
    
    response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

    TOKEN = response.json()['access_token']

    headers['Authorization'] = f'bearer {TOKEN}'
    return headers


def grabStory(headers,PostNumber,subreddit):

    response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/top', headers=headers, params={'limit': PostNumber, 't': 'week'})

    while response.status_code != 200:
        Exception("Cannot get short story")
        response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/top', headers=headers, params={'limit': PostNumber, 't': 'week'}) 

    # Convert to JSON
    data = response.json()

    posts = data.get("data", {}).get("children", [])
    if len(posts) < PostNumber:
        print(f"Not enough posts found in /r/{subreddit}.")
        return None
    fullStory = posts[PostNumber -1]['data']['title'] + ". " + posts[PostNumber-1]['data']['selftext'] + " filler"#Includes title of the post and the accompying body. The filler is so the speech includes the full text without cutting out the start and ending
    
    return fullStory



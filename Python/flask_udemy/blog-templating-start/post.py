import requests
class Post:
    def get_blog(self):
        blog_link = 'https://api.npoint.io/c790b4d5cab58020d391'
        response = requests.get(blog_link)
        data = response.json()
        return data



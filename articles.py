from newspaper import Article
import requests

# url = 'https://brightside.me/wonder-animals/photographers-show-us-the-beauty-of-peacock-spiders-and-we-cant-spot-2-similar-ones-798461/'
# article = Article(url)
# article.download()
# article.parse()

# print(article.top_image)
# print(article.summary)

url = "http://10.10.74.89:8080/nxadmin/api/v1/auth/login"

payload = "{\n    \"user_name\": \"rsafari\",\n    \"user_password\": \"123456789\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

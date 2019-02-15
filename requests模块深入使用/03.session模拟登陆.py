import requests

headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

url = 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'

data = {'input1':'hello_lwz','input2':'lwz199508@'}
session = requests.session()

reponse = session.post(url,headers=headers,data=data)

print(reponse.content.decode())
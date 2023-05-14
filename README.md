# chatGPT-simple-proxy

[中文用户看这里](https://blog.restkhz.com/post/chatGPT-simple-proxy)

First, this little simple project is based on:

https://github.com/ioanmo226/chatgpt-web-application

**So, huge thank to @ioanmo226!**

I modified part of the javascript and wrote a another simple backend with flask to give this program **the ability to understand context.**

1. To prevent abuse, I added a simple **permission authentication**.
2. Now, **GPT-4 is supported**.

![chatGPT-simple-proxy-example](https://github.com/restkhz/blogImages/blob/main/img/Screenshot_20230411_085904.png?raw=true "chatGPT-simple-proxy-example")

## How to use

1. ```git clone https://github.com/restkhz/chatGPT-simple-proxy.git```
2. ```pip install -r requirements.txt```
3. ```export AUTH=<1 or 0. set to 1 to enable authentication> PORT=<3001>  TOKEN=<sk-xxx...>```
4. If you set `AUTH` to `1` in the previous step, modify `users.json` to assign credentials.
5. ```python chatGPT_proxy.py```

### With Docker

Image is about 144Mb

1. ```git clone https://github.com/restkhz/chatGPT-simple-proxy.git```
2. Modify `Dockerfile` to fit your environment.
3. ```sudo docker image build -t chatgpt-proxy .```
4. ```sudo docker container run -p <port>:3001 -v .:/app chatgpt-proxy```

## Warning

Please do not use it in a production environment.
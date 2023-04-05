# chatGPT-simple-proxy

First, this little simple project is based on:

https://github.com/ioanmo226/chatgpt-web-application

**So, huge thank to @ioanmo226!**

I modified part of the javascript and wrote a another simple backend with flask to give this program the ability to understand context.

To prevent abuse, I added a simple permission authentication.

## How to use

1. ```git clone ```
2. ```pip install -r requirements.txt```
3. ```export AUTH=<1 or 0. set to 1 to enable authentication> PORT=<3001>  TOKEN=<sk-xxx...>```
4. If you set `AUTH` to `1` in the previous step, modify `users.json` to assign credentials.
5. ```python chatGPT_proxy.py```

### With Docker
Image is about 144Mb

1. ```git clone ```
2. Modify `Dockerfile` to fit your environment.
3. ```sudo docker image build -t chatgpt-proxy .```
4. ```sudo docker container run -p <port>:3001 chatgpt-proxy:0.1```
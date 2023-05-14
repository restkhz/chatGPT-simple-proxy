FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

# set 1 to enable auth, 0 to disable.
# the usernames and passwords were stored in user.json
ENV AUTH=1

# server port in the CT,
# you don't really need to change it.
ENV PORT=3001

#OpenAI token. Something start with sk-xxx...
ENV TOKEN=sk-xxx

VOLUME /app

CMD python3 chatGPT_proxy.py

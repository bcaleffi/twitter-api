FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install python3.8 -y && \
    apt-get install python3-pip -y && \
    apt-get install sqlite3 -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
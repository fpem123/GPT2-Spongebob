FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apt-utils wget && \
    apt-get -qq -y install curl && \
    apt-get install -y unzip

RUN pip install --upgrade pip
RUN pip install transformers \
    flask

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=1-9fwrJXDpZdzcMJsn9s_I4HfOW-gTu9C" > /dev/null
RUN curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=1-9fwrJXDpZdzcMJsn9s_I4HfOW-gTu9C" -o GPT2-large_Spongebob.zip
RUN unzip GPT2-large_Spongebob.zip
RUN rm GPT2-large_Spongebob.zip

EXPOSE 80

CMD ["python3", "main.py"]

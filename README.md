# GPT2-Spongebob

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/fpem123/GPT2-Spongebob)

This project generates Rick and Morty script using GPT-2 model.

Base model: gpt-2 large

Fine tuning data: https://www.kaggle.com/mikhailgaerlan/spongebob-squarepants-completed-transcripts

Model download: https://drive.google.com/file/d/1-9fwrJXDpZdzcMJsn9s_I4HfOW-gTu9C/view?usp=sharing

    How to use:
      * First, Choose Rick and Morty character name.
      * Second, Fill what the character will say in text. This will be base of script.
      * And then, Fill number in length. Text is created as long as "length". I recommend between 100 and 300.
      * If length is so big, generate time will be long.


### Post parameter
    
    name: The Spongebob character name.
    text: The base of script.
    length: The size of generated text.

### ** With CLI **

    curl -X POST "https://master-gpt2-spongebob-fpem123.endpoint.ainize.ai/Spongebob" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "name=Spongebob" -F "text=Hello" -F "length=100"

### ** With swagger **

API page: https://ainize.ai/fpem123/GPT2-Spongebob?branch=master

### ** With a demo **

Demo page: https://master-gpt2-spongebob-fpem123.endpoint.ainize.ai/

### Image reference

    static/README.md

--
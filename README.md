# GPT2-SpongeBob

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/fpem123/GPT2-Spongebob)

This project generates SpongeBob script using GPT-2 model.

Fine tuning data: [Kaggle](https://www.kaggle.com/mikhailgaerlan/spongebob-squarepants-completed-transcripts)

Model download: [Google dirve](https://drive.google.com/file/d/1-9fwrJXDpZdzcMJsn9s_I4HfOW-gTu9C/view?usp=sharing)

### Model information

    Base model: gpt-2 large
    Epoch: 50
    Train runtime: 14723.0716
    Loss: 0.0268

### How to use:
    * First, Choose SpongeBob character name.
    * Second, Fill what the character will say in text. This will be base of script.
    * And then, Fill number in length. Text is created as long as "length". I recommend between 100 and 300.
    * If length is so big, generate time will be long.


### Post parameter
    
    name: The SpongeBob character name.
    text: The base of script.
    length: The size of generated text.

### Image reference

    static/README.md

## * With CLI *

    curl -X POST "https://master-gpt2-spongebob-fpem123.endpoint.ainize.ai/SpongeBob" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "name=SpongeBob" -F "text=Hello" -F "length=100"

## * With swagger *

API page: [Ainize](https://ainize.ai/fpem123/GPT2-Spongebob?branch=master)

## * With a Demo *

Demo page: [End-point](https://master-gpt2-spongebob-fpem123.endpoint.ainize.ai/)


--
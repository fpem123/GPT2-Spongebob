from transformers import pipeline, set_seed, AutoTokenizer, AutoModelForCausalLM
import torch


tokenizer = AutoTokenizer.from_pretrained('./GPT2-large_Spongebob')
model = AutoModelForCausalLM.from_pretrained('./GPT2-large_Spongebob')

seq = "Spongebob: What? What is this? I don't wanna die!"
input_ids = tokenizer.encode(seq, return_tensors='pt')


sample_outputs = model.generate(input_ids, pad_token_id=50256,
                                do_sample=True,
                                max_length=300,
                                top_k=40,
                                num_return_sequences=1)


for idx, output in enumerate(sample_outputs):
    print(idx)
    rnm_story = tokenizer.decode(output, skip_special_tokens=True).split('\n')

    for i in range(len(rnm_story)):
        rnm_story[i] = rnm_story[i].split(':')

    for s in rnm_story:
        print(s)

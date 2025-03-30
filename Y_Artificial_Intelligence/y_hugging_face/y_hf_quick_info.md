# Datasets :
    Preprocessesed Data which can be used for training your models 

    > pip install datasets


# Transformers library :
    
    > pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


    Python code to see if torch recgnizes GPU
        >>> torch.cuda.is_available()
        Mostly the above code will return "FALSE" because I am using Virtualbox


    > pip install transformers


    To confirm if "transformers" is working properly or not 
        >>> python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we kind of you'))"
        -   As you did not mention which model to use , it will use a DEFAULT one 
        -   For the very first time , it Downloads big files which I presume as "WEIGHTS" of the 
            model along with 
            other necessities.
        -   They get downloaded into your systems cache file , the directory will be as below
            "~/.cache/huggingface/" 
        -   You can change environment variables to change that cached location

    To start with an example text generation :

        >>> import torch
        >>> from transformers import pipeline

        >>> model_id = "meta-llama/Llama-3.2-3B-Instruct"
        >>> pipe = pipeline(
                                "text-generation",
                                model=model_id,
                                torch_dtype=torch.bfloat16,
                                device_map="auto",
                            )
        >>> messages = [
                            {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
                            {"role": "user", "content": "Who are you?"},
                        ]
        >>> outputs = pipe(
                                messages,
                                max_new_tokens=256,
                            )
        >>> print(outputs[0]["generated_text"][-1])

import transformers

pipeline = transformers.pipeline(
    "text-generation",
    model="microsoft/phi-4",
    model_kwargs={"torch_dtype": "auto"},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a medieval knight and must provide explanations to modern people."},
    {"role": "user", "content": "How should I explain the Internet?"},
]

outputs = pipeline(messages, max_new_tokens=128)
print(outputs[0]["generated_text"][-1])


======================================================================
import torch
from transformers import pipeline
pipe = pipeline(
     "text-generation",
     model="lmsys/fastchat-t5-3b-v1.0",
     model_kwargs={"torch_dtype": torch.bfloat16},
     device_map="auto"
)
messages = {"role": "user", "content": "How should I explain the Internet?"}
outputs = pipeline(messages)
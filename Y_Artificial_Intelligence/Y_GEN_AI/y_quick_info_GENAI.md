---------------------------------- Check later -- start ------------------------------------------

LLM :
RAG :
    TYPES :
        1) Corrective RAG
        2) SELF RAG
        3) AGENTIC RAG 

    RAG CHUNKING TYPES :
        1)  FixedSize chunking          = Breaks at every N number of chars
        2)  RecursiveCharacter Chunking = Recursively drills down until the pieces fit your size 
                                          limit without breaking a sentence or paragraph apart.
        3)  Semantic Chunking           = Break happens based on meaning 
        4)  Hierarchical or 
            parent-child or 
            Big-small chunking          = Data will be chunked in small to big possible lengths

    Embedding Models : 

AGENTS :
MCP - MODEL CONTEXT PROTOCOL :
Agent 2 Agent :
DAG - subject to correction :











---------------------------------- check later -- end ----------------------------------------------

Terminology :
    Tokenization : Dividing a much complex item in simpler possible item according to the necessity
        character tokenizer : 
            "the cat sat on the mat" -->> 
            ["T","h","e"," ","c","a","t"," ","s","a","t"," ","o","n"," ","t","h","e"," ","m","a","t","."]
        subword tokenizer :
            "unbelievable"
            ["un", "believe", "able"]
        Word tokenizer :

        sentence tokenizer

        Example tokenizers : BPE(Byte pair encoding) , Auto Tokenizer from transformers library hugging face
        Website to test : https://tiktokenizer.vercel.app/

    Embedding :
        Word embeddings Examples :
            Word2Vec
            Glove
            FastText
        Sentence embeddings :
            BERT
            Sentence BERT
            Universal sentence encoder
        Vector embedding : (used for images or sounds or anything that needs to be embedded)
    Lemmatization
    stemming
    Positional encoding : I think it numerically represents the sequence in which the prompt text was given
        "the cat sat" is given , if PE is not there "sat the cat" could be interpreted for futher steps 
    POS tagging
    Name entity recognition and relation
    chunking
    stop word removal

    MOE : Mixture of Experts 
        For any given query instead of engaging the entire billions of parameter , it only engages the section 
        that will best be responsible for the QUERY'S topic.
        Those are called ACTIVATED PARAMETERS
    DENSE MODEL : opposite of MOE

    RAG
    MCP
    EVAL

    Types of Models :
        Auto regressor 
        Diffusion
        Flow based model
        Energy based models
        Variational model
        GAN
        Normalizing flows
        Score based models
        Neural ODE s
        

Attention mapping of words in a sentence to each other


emirates
5 days 


Foundational models :(Subject to correction)
    BERT 
    GPT
    LLaMa
    BLOOM
    FLAN-T5
    PaLM


Day 4 12:28 starting 


AI WORKFLOWS = "AI MODEL"+"some tools" orchestrated in flow by human

AI AGENT = an "AI MODEL" + Ability to be aware of its environment and learn how to react as need autonomously
            with out any human suggestion.



AI TOOLS :
    Cursor 
    Windsurf
    IBM watson x -> agent builder 


Latest Breakthroughs :
    Darwin Godel Machine :
        Self improving AI system ,iteratively modifies its python code base.

Ai researchers :
    Andrej karpathy - open AI
    Yan leecun - Meta 

LLM LEADER BOARDS :
    https://lmarena.ai/?leaderboard
    https://scale.com/leaderboard
    https://arcprize.org/leaderboard

DATABRICKS GENAI :
    MOSAIC AI PLATFORM :
        WHAT IS IT :
            - A unified suite of tools in DATABRICKS designed to help organizations 
            build, deploy, govern, and monitor enterprise-grade AI applications.

        HISTORY:
        - DATABRICKS bought "MOSAIC ML" in 2023 for $1.3B 

        Components :
            - Model Training -> A framework for fine-tuning or training opensource LLMS
            - Model Serving
            - AI Gateway
            - Vector Search
            - Agent Framework & Evaluation
            - MLflow Integration

        Note :  Each component of MOSAIC AI PLATFORM interacts with MLFLOW to provide observability 
                and lifecycle management (Subject to correction)

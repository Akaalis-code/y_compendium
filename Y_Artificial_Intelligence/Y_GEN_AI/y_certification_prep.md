--------- Check later -- Start -------------------------------------------------------

Lang Chain vs LamaIndex .
Autogen agentic framework .
Embedding vs Vector embedding 


Code snippet used :

    %pip install -U --quiet databricks-sdk==0.49.0
                            "databricks-langchain>=0.4.0"
                            databricks-agents mlflow[databricks]
                            databricks-vectorsearch==0.55
                            langchain==0.3.25
                            langchain_core==0.3.59
                            bs4=0.0.2
                            markdownify==0.14.1
                            pydantic==2.10.1
                            mlflow
                            openai
                            pyMuPDF
    dbutils.library.restartPython()

    from databricks_langchain import chatDatabricks

    chat_model = chatDatabricks(
                                    endpoint = "databricks-meta-llama-3-3-70b-instruct" ,
                                    temperature = 0.1 , 
                                    max_token = 250 ,
                                )
    
    chat_model.invoke("<My query>")



Distance formulas for similarities :
    Euclidean Distance
    Cosine similarity 
    Manhattan distance 
--------- Check later -- End -------------------------------------------------------


Exam evaluation syllabus : 45 questions 90 minutes 
    Designing Application - 14%
        Prmpt engineering 
        Model Selection
        Input and Output in Model
        Business Requirement to solution 
        Tools
    Data preparation - 14%
        RAG Solution 
        Data Gathering and Extraction
        Chunking Strategy
        Right Prompts fro RAG
        Tools and metrics to evaluate retrieval performance 
    Application Development -30%
        Frameworks like LANGCHAIN for building te application
        Prompt formats
        LLM Safety , Gaurdrails
        Utilize Agent Framework for dveloping agentic systems 
    Assembling and Deploying Apps - 22%
        Creating chain based application
        Register model with unity catalog using MLFLOW
        Deploy an end point for basic RAG application
        Vector serch
        Utilize agent framework for developing agentic systems
    Governance - 8%
        Guardrail techniques
        Legal or licensing requirements 
    Evaluation and monitoring - 12%
        LLM Selection (based on Size or Architecture)
        Key metrics to monitor a specific LLM
        Inference logging
        Use Inference tables and Agent Monitoring to track a live LLM endpoint 







LLM -> reasoning and generate content 
Agentic AI -> LLM+Actions in real world
    Autonomy , Agency , Authority 

PRAL -> Perceive Reason Act Learn


Tokenization :
    Braeking of a large para or sentence or words into basic chunks .
    The size of the Basic chunk is dependent on use case .
    In most scenarios the BASIC CHUNK SIZE if a word.

    Online example tokenizer :
        platform.openai.com/tokenizer

Embedding :
    Each Token will be understood by computer in a ARRAY of NUMERIC form in Multi dimensional space.
    The Axes of those multidimension may or may not be a human understandable characteristic nature of data.

Prompt Engineering types :
    SALT :
        Style
        Audience 
        Length
        Tone
    
    RTF :
        Role
        Task
        Format - Like you want output in any JSON or a tabular or any other form .
    
    CTF :
        Context
        Task
        Format
    
    RASCEF :
        Role
        Action
        Steps
        Context
        Examples
        Format
    

RAG (Retrieval Augmented Generation) :
    Limitations of traditional LLM :
        LLM tend to hallucinate 
        LLM has limited context window 
        LLM has knowledge cutoff
        LLM may not have domain specific info 
    
    My question :   
        Q)  How does RAG differ from sending my prompt by just adding all the context it requires to answer along with question ?
        A)  I think (Subject to correction) , Suppose if the knowledge we have to send as context is 1000 pages , 
            Generaly we have to send all the 1000 pages text in our prompt in which may be 10 pages are related to our query,
            But what RAG solution gives us is , Store all the knowledge in EMBEDING form in Vector data base , 
            and this time our prompt will conssts of our query augmented with only those few pages relavant to our question .
    
    RAG STEPS :
        Index and Embedding
        Vector store or vector DB
        Filtering and reranking
        Generation
        Retrieval nd similarity search
        Prompt Augmentation 


    Practical RAG steps in Databricks :
        Load raw data into UC volumes

        Preprocess data

        chunking - Example website for practical "chunkviz.up.railway.app"
            Code -
                from langchain.text_splitter import RecursiveCharacterTextSplitter
                raw_text = ....read(my_files.pdf)
                text_splitter_object = RecursiveCharacterTextSplitter(chunk_size = 200 , chunk_overlap = 20)

        Create delta table with those chunks 

        Embedding - Converting text into numerical representation
            Embedding model is resonsible for doing that 
            Embedding dimension size 
            Examples Embedding models -
                databricks-bge-large-en -- by databricks   -- Free(preview)      -- English language only -- Native in DBX
                text-embedding-3-small  -- by openai       -- 0.02$/1 mil token  -- Multi language        -- Via API
                all-MiniLM-L6-v2        -- by Huggingface  -- Free (self host)   -- English only          -- Custom 
                text-embedding-ada-002  -- Azure OpenAi    -- 0.1$/1 mil token   -- Multi                 -- Via Api
                embed-english-v3.0      -- Cohere          -- Free and paid tiers-- English               -- Via API 
            Vector search strategies -
                KNN
                ANN
            Indexing strategies -
                Tree         -- Annoy  -- spotify
                Graph        -- HNSW   -- 
                Clustering   -- FAISS  -- Facebook
                Hashing      -- LSH    --  
                Compression  -- SCaNN  -- Google

        Indexing 

        Vector database -
            Mosaic AI Vector Search by databricks -
                serverless vector database integrated directly into the Databricks Data Intelligence Platform. 
                It is specifically designed to support Retrieval Augmented Generation (RAG)

RAG Code :

    PDF -> Text chunks
    Text chunks -> Embeddings
    Store in Vector store
    Build Vector Search Index
    Query via Vector Search Client 
        from databricks .vector_search.client import VectorSearchClient
        client = VectorSearchClient()

Resume at 33.Vector Search index 
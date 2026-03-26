--------- Check later -- Start -------------------------------------------------------

Lang Chain vs LamaIndex .
Autogen agentic framework .
Embedding vs Vector embedding 




Distance formulas for similarities :
    Euclidean Distance
    Cosine similarity 
    Manhattan distance 

Creating indexs :
   create_index   vs   create_delta_sync_index   vs   create_direct_access_index


Architecture:

    Decoder-only (e.g., GPT-2, GPT-3, LLaMA, Falcon) → best for text generation.

    Encoder-only (e.g.,  BERT, RoBERTa, DistilBERT) → best for classification, embeddings, retrieval tasks.

    Encoder-decoder (e.g., T5-style, Seq2Seq) → versatile, good for translation and summarization.



    Architecture	Input Context	Output Style	                        Best Use Cases
    Decoder-only	Left-to-right	Autoregressive	                        Text generation, dialogue, creative writing
    Encoder-only	Bidirectional	Non-generative	                        Classification, embeddings, retrieval
    Encoder-decoder	Bidirectional   (encoder) + autoregressive (decoder)	Seq2Seq	Translation, summarization, text-to-text

Databricks GenAI Indemnity -->> post this to linkedin 


Building LLM application :
    The industry has standardized around a few key pillars: 
        Framework orchestration -
            LANGCHAIN -
                LCEL (LangChain Expression Language)
                LangChain is mostly Directed Acyclic
            LANGGRAPH
            Other tools -
                Data-Centric Frameworks (RAG Specialists) - 
                    LlamaIndex
                    Haystack (by deepset)
                Multi-Agent & Orchestration Frameworks - 
                    CrewAI
                    Microsoft AutoGen
                    OpenAI Swarm
                Enterprise & Developer-First Frameworks - 
                    Semantic Kernel (Microsoft)
                    DSPy (Stanford)
                    Vellum

        Prompt engineering, 
        Security guardrails,
        Agentic reasoning.
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


    Note : Each component of MOSAIC AI PLATFORM interacts with MLFLOW to provide observability and lifecycle management (Subject to correction)

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
        MODEL tends to hallucinate 
        MODEL has limited context window 
        MODEL has knowledge cutoff
        MODEL may not have domain specific info 
    
    Question :   
        How does RAG differ from sending "my prompt + all the context it requires to answer" to a model ?

    Answer :
        In a way it is same when you are talking about 10 to 20 lines of context window, 
        But the actual difference comes when the context scales up to thousand of documents .

        Example : 
            Suppose you know your question has an awnser in 5000 PDF docs , Manually attaching all the text isnt practical.
            Moreover doing that will make you run out of TOKEN WINDOW , and its costly .

            In RAG it follows below steps :-
                1) Embed the entire 5000 docs 
                2) Store in vector DB 
                3) Do a Semantic search to extract only related info to your original question
                    "5000 docs" became -->> "Few related line of info" 
                4) ADD the extracted similar items to your question 
                5) send the "QUESTION + only related info from Semantic search" as PROMPT
    
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
                from langchain.text_splitter import RecursiveCharacterTextSplitter ## depricated 
                raw_text = ....read(my_files.pdf)
                text_splitter_object = RecursiveCharacterTextSplitter(chunk_size = 200 , chunk_overlap = 20)

        Create delta table with those chunks 

        Embedding - Converting text into numerical representation
            Embedding model is responsible for doing that 
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
    PDF file -> DBKS tables 
        CODE :
            from databricks.sdk import WorkspaceClient
            import os

            # Replace with your actual workspace URL and Personal Access Token (PAT)
            w = WorkspaceClient(
                                    host="https://adb-1234567890.12.azuredatabricks.net",
                                    token="dapiexample1234567890abc"
                                )

            # Test the connection by listing your catalogs
            for catalog in w.catalogs.list():
                print(catalog.name)

    PDF -> Text chunks

    Text chunks -> Embeddings

    Store in Vector store

    Build Vector Search Index - 
        It does indexing based on similarities , rather than exact match 
        I think this can be done on any delta table (Subject to correction ) if you want to do a similarity search .

    Query via Vector Search Client - communicating point with vector store for Adding or retrieving embeddings or indexes or do similaity search
        from databricks.vector_search.client import VectorSearchClient
        client = VectorSearchClient()
        # Or, if outside Databricks:
        # vsc = VectorSearchClient(
        #                           workspace_url="https://adb-xxx.azuredatabricks.net",
        #                           personal_access_token="dapi..."
        #                          )
        vs_index = client.create_index (
                                            endpoint_name      = "vs_endpoint",
                                            index_name         = "documents_index"
                                            source_table_name  = "catalog.schema.table_with_chunks" # Not yet embedded I think 
                                            embedding_column   = "<column which has the text chunks>"
                                            id_column          = "<Primary key column in chunks table>"
                                        )
        
        clent.list_endpoints()
        client.list_indexes(<vector store name>)
        index = client.get_index(index_name = "<catalog.schema.indexname")

        # Simiarity Search 
        result_dict = index.similarity_search(
                                                query_text  = "<your query , like the usual prompt or questions>"
                                                columns     = ["<primary_key_column>","<data_chunks_col>"] # Check if all columns need to be given or not
                                                num_results = 3
                                              )
        
        # Reranker - suppose if you know a chunk needs to be considered with more priority , thank what was given by the index .

    LANGCHAIN -

        CODE SNIPPET -
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

            Or Use below cmd if you are running in your terminal                 
                %pip install -U databricks-sdk \
                                databricks-langchain \
                                databricks-agents \
                                mlflow[databricks] \
                                databricks-vectorsearch \
                                langchain \
                                langchain_core \
                                bs4 \
                                markdownify \
                                pydantic \
                                mlflow \
                                openai \
                                pyMuPDF

            dbutils.library.restartPython()

            from databricks_langchain import chatDatabricks
            # Below three lines are config , if you run from local machine (subjet to correction)
            # Optional: Set environment variables in code if not set in system
            # os.environ["DATABRICKS_HOST"] = "https://your-workspace-url"
            # os.environ["DATABRICKS_TOKEN"] = "dapi..."
            chat_model = chatDatabricks(
                                            endpoint = "databricks-meta-llama-3-3-70b-instruct" ,
                                            temperature = 0.1 , 
                                            max_token = 250 ,
                                        )
            
            chat_model.invoke("<My query>")
        
        Retriever - 
            from databricks_langchain import DatabricksVectorSearch

            vector_store = DatabricksVectorSearch(index_name = "<Your Vector Search Index Name>")
            retriever    = vector_store.as_retriever(search_kwargs =    {{
                                                                            "k": 3,   # Number of chunks that should be retured
                                                                            "distance_threshold": 0.5,  # Only return results with a score better than 0.5 (Subject to verification)
                                                                            "filters": {"department": "Engineering"} # Metadata filter (Subject to verification)
                                                                        }}
                                                    )
            relavant_document = retriever.invoke("what is Databricks")
        
        Format relavant info into context -

            def format_context(docs):
                chunk_contents = [f"Passage: {d.page_content}\n" for d in docs]
                return "".join(chunk_contents)
            
            format_context(relavant_document)
        
        Now work on PROMPT Template - query + context 

            Chain Config -
                chain_config =  {   "llm_model_serving_endpoint_name" : "databricks-meta-llama-3-3-70b-instruct" #The foundation model 
                                    "vector_search_endpoint_name"     : "demoeps"
                                    "vector_search_index"             : "workspace.default.my_index"
                                    "llm_prompt_template"             : """you are an helpful AI assistant , use the context {context}""",
                                } 
            
            from langchain_core.prompts import ChatPromptTemplate
            from databricks_langchain.chat_models import ChatDatabricks
            from operator import itemgetter

            prompt = ChatPromptTemplate.from_message    (
                                                            [
                                                                ("system",chain_config.get("llm_prompt_template")),
                                                                ("user","{question}")
                                                            ]
                                                        )
        
        Building Chains -

            model  = chat_model
            answer = (prompt | model | StrOutputParser()).invoke(   {
                                                                        'question':'who is data fudiciary?' ,
                                                                        'context':relevant_docs # check the variable correctly 
                                                                    }
                                                                )


#### Resume at 56 



--------------------- Practise exam concepts -- start ------------------------------------------------------
- GAN
- CNN
- Zero shot classification :
        Defined as an AI's ability to categorize data into classes it was never explicitly trained on.
        Unlike traditional models that require thousands of labeled examples, zero-shot models leverage "world knowledge" 
        from massive pre-training to recognize new categories via semantic descriptions or relationships.

- when would you use fine tuning technique

- Summarization :
        Extractive summarization
        Abstarctive summa
        Tokenized sentence reduction
        Frequence based summarization 

- Vector library like FAISS instead of a vector database
- keyword matching (like BM25
- Lost-in-the-Middle Problem:   Research indicates that LLMs pay a disproportionate amount of attention to the 
                                beginning and end of a very long prompt, often overlooking critical information 
                                placed in the middle section of the input text. 

- Eval tools :
    Open Source :
        - RAGAS
        - Deep eval 
        - Arize Phoenix
    Integrated Platform Tools (Databricks / Enterprise) :
        - MLflow LLM Evaluate
        - Mosaic AI Agent Evaluation
        - 


- Metrics:
    Accuracy / Exact Match	    Factual correctness
    BLEU / ROUGE	            Overlap with reference text
    Recall@K / NDCG	            Retrieval relevance (RAG)
    LLM-as-a-Judge	            Semantic correctness
    Human Evaluation	        Gold standard

- AI in SQL queries :
    SELECT 
        product_name,
        review_text,
        -- Calling an LLM to summarize a review
        ai_query    (
                        "gpt-4o", 
                        "Summarize this review in 10 words: " || review_text
                    ) AS short_summary
    FROM customer_reviews;

    Other tools :
        ai_summarize
        ai_translate
        ai_fix_grammar
        ai_classify
        ai_embedding()-->> to embed the any text or column of text .
    
    SELECT title, author
    FROM library_table
    ORDER BY vector_similarity(title_vector, ai_embedding('A story about a small adventurer')) DESC
    LIMIT 5;
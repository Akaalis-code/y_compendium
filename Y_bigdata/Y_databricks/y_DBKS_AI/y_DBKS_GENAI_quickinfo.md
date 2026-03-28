# Create a MODEL endpoint :
    DATABRICKS UI -> Left Panel -> Serving -> Right side top "create serving endpoint"


# Cost realted info of endpoint :
    - The input and output DBU s for each foundational models are mentioned .
    - The model that you created runs on "SERVERLESS COMPUTE"  (Subject to verification)
    - If the model endpoint is not prompted for a while the serverless shuts down to least number of machines.
      In case while creating endpoint , if you had choosen option "SCALE TO ZERO" , then all compute shuts down 
      for this model . Note that this still cost you more that 0 dollars.
      Generally in production you dont select this , so that SERVERLESS always stays live with minimum compute atleast.
    - There is a STOP button for your serverless to stop serving your model , 
      Only when you STOP , you will incurr absolute zero dollars.
    
    Types of MODELS based on COST and other factors : (Subject to corrections , learnt from AI)

        Option 1: Foundation Model API (Pay-per-token) -
          - These are models that are kept alive by databricks and are used by all the databricks users around the world.
          - In this case , there is no STARTING OR STOPPING the model .
          - So in the case a centralized model run and maintained by databricks (Kind of like Google facebook and electricity usage) 
            serving all the users . shared by all .
          - You only pay for what you use , tokens wise.

        Option 2: Model Serving Endpoint (Provisioned Throughput) -
          - This is like you have your own electricity generator at home only personal to you .
          - If you spin up a customized model , even if its based on any foundation model , you will be given dedicated serverless GPUs.
          - This Model and its resource are being used by only you or your team , not by the world .

# MOSAIC AI PLATFORM :
    The Databricks Mosaic AI platform is a unified suite of tools designed to help organizations build, deploy, govern, and monitor 
    enterprise-grade AI applications, particularly those using generative AI and large language models (LLMs).

    - Model Training -- A scalable framework for fine-tuning or training open-source LLMs
    - Model Serving
    - AI Gateway
    - Vector Search :
            1) For vector DB , (check about delta sync)
            2) Two main ways tp manage you r vectors
                2.1) Delta sync index 
                2.2) Direct vector access index
    - Agent Framework & Evaluation
    - MLflow Integration


    Note : Each component of MOSAIC AI PLATFORM interacts with MLFLOW to provide observability and lifecycle management (Subject to correction)


# DATABRICKS AI ENDPOINTS :
  ## Goal :
      There is an Databricks AI endpoint being served .
      Now you have to use that end point and connect to your local system .
      GENAI model is in databricks cloud , Talk to it from your local computer .

  ## Setup in your local system :
      - INSTALL OPENAI library :
            - Create a virtual environment for installing these libs , as System level python doesnt allow to install new libs
                > sudo apt install python3.12-venv          ## To install venv into your system
                > python3 -m venv y_AI_ENV                  ## Create an vitual env 
                > cd y_AI_ENV/bin/                          ## Your activate and deactivate files for venv are present here
                > source activate                           ## Activate the venv "my_env" 
                (my_env) > deactivate                       ## This a shell function inside activate file , to comeout of venv
        
            - Install the OPENAI lib :
                > pip install openai
            
            - Install JUPYTER notebook :      
                (y_AI_ENV) > pip install jupyter             ## Install JUPYTER inside your my_venv using pip
                (y_AI_ENV) > jupyter notebook                ## To start Jupyter Notebook server , open "http://localhost:8888/" in any browser
                (y_AI_ENV) > ctrl + c                        ## To stop Jupyter Notebook server
        
            - Setup API key to access served model :
                1) Open databricks wiyh your main account , NOTE : " Only 'PAY PER TOKEN existing FOUNDATION MODELS' are working with non primary account's API" 
                2) Click on your profile icon top right 
                        -->> Click on setting
                            -->> Go to 'USER' Section and click on 'DEVELOPER' tab
                                -->> In 'DEVELOPER' tab near 'Access token' click on 'MANAGE'
                                    -->> Under 'MANAGE" generate new token and use it in your code at 
                                         OpenAI(api_key = "<paste Here>" , ....)
            
            - Get base url for OpenAI() function :
                1) DATABRICKS HOEM -->> Left panel -->> AI?ML section -->> servings endpoint -->>
                    Copy the URL at the top section and use it in 
                    OpenAI(..... , base_url = "<paste here>")

  ## Script for using it as a chatbot :
        from openai import OpenAI
        import os
        var_client = OpenAI(
                                api_key = os.getenv("var_AI_API_sec", "null"),
                                base_url = os.getenv("var_end_point", "null")
                            )
        while True:
            var_user_prompt = input("Your prompt message here: ")
            if var_user_prompt == 'y_done':
                break
            var_response = var_client.chat.completions.create(
                                                                messages = [
                                                                                {
                                                                                    "role": "system",
                                                                                    #"content": "You are 3 year old child who doesnt know much"
                                                                                    "content": "You are a general helpful question answer assistant , answer briefly"
                                                                                },
                                                                                {
                                                                                    "role": "user",
                                                                                    "content": var_user_prompt
                                                                                }
                                                                            ],
                                                                model="databricks-meta-llama-3-1-8b-instruct",
                                                                max_tokens=256
                                                            )
            print(var_response.choices[0].message.content)
        print('Thank you for chatting')

  ## Unity catalog setup :
        (my_env) > pip install databricks-sdk                   ## For running databricks scripts locally
        (my_env) > pip install databricks-vectorsearch          ## For vector database 

  ## Unity catalog script :
        from databricks.sdk import WorkspaceClient
        import os

        w = WorkspaceClient(
                                host  = os.getenv("var_base_url", "null"),
                                token = os.getenv("var_AI_API_mn", "null")
                            )

        display(w.dbutils.fs.ls('/Volumes/y_ws_250705/y_schema_for_ai/y_volume_for_rag/'))

        created_schema = w.schemas.create   ( 
                                                name         = "y_schema_for_AI",
                                                catalog_name = "y_ws_250705",
                                                comment      = "Created schema especially for AI related content"
                                            )

        from databricks.sdk.service.catalog import VolumeType
        created_volume = w.volumes.create  (
                                                catalog_name = "y_ws_250705",
                                                schema_name  = "y_schema_for_AI",
                                                name         = "y_volume_for_RAG",
                                                volume_type  = VolumeType.MANAGED,
                                                comment      = "Volumes to store my RAG source PDFs"
                                            )
                    
  ## Chunking setup : 
        (my_env) > pip install langchain-text-splitters
        (my_env) > pip install langchain

  ## Chunking scripts : Note this script is to be run in databricks notebook . local script gets complicated but doable .
        import pandas as pd
        from pyspark.sql.functions import monotonically_increasing_id, col
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        CATALOG = "y_ws_250705"
        SCHEMA = "y_schema_for_ai"
        VOLUME_NAME = "y_volume_for_rag"
        FILE_NAME = "y_info_for_rag.txt"
        TABLE_NAME = f"{CATALOG}.{SCHEMA}.y_tbl_for_chunking"
        VOLUME_PATH = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME_NAME}/{FILE_NAME}"

        with open(VOLUME_PATH, "r") as f:
            text = f.read()

        splitter = RecursiveCharacterTextSplitter(
                                                    chunk_size=100,
                                                    chunk_overlap=10,
                                                    separators=["\n\n", "\n", " ", ""]
                                                )
        chunks = splitter.split_text(text)
        print(text)
        print(chunks)

        data = [{"id": i, "content": chunk} for i, chunk in enumerate(chunks)]
        df = spark.createDataFrame(data)
        df.display()

        df.write.format("delta")\
                .mode("overwrite")\
                .option("delta.enableChangeDataFeed", "true")\
                .saveAsTable(TABLE_NAME)

        print(f"Success: Data indexed into Delta Table {TABLE_NAME}")


  ## INDEXING Work :

        ### DATABRICKS ENDPOINTS FOR RAG :

            LLM Model End point     --> BRAIN
            Embedding endpoint      --> Translator from TEXT to MATH
            Vector search endpoint  --> Resource for SIMILARITY and SEMANTIC search

        ### Create Vector Search Endpoint : This provides the compute resources needed to host and query vector search indexes
                from databricks.vector_search.client import VectorSearchClient
                import time

                VS_ENDPOINT_NAME = "y_vector_search_endpoint"
                vsc = VectorSearchClient()


                #### 1. Create the Vector Search Endpoint
                #### Check if it exists first to avoid errors
                existing_endpoints = [e['name'] for e in vsc.list_endpoints().get('endpoints', [])]

                if VS_ENDPOINT_NAME not in existing_endpoints:
                    print(f"Creating endpoint {VS_ENDPOINT_NAME}...")
                    vsc.create_endpoint(name=VS_ENDPOINT_NAME, endpoint_type="STANDARD")
                else:
                    print(f"Endpoint {VS_ENDPOINT_NAME} already exists.")

                #### 2. Wait for it to be ready (it takes a few minutes)
                while vsc.get_endpoint(VS_ENDPOINT_NAME).get("endpoint_status", {}).get("state") != "ONLINE":
                    print("Waiting for endpoint to come online...")
                    time.sleep(30)

                print("Endpoint is ONLINE.")
        
        ### Create the Index (The Map) :
                INDEX_NAME = f"{CATALOG}.{SCHEMA}.gwinzol_vsearch_index"

                #### Create the index
                vsc.create_delta_sync_index(
                endpoint_name=VS_ENDPOINT_NAME,
                source_table_name=TABLE_NAME,
                index_name=INDEX_NAME,
                pipeline_type='TRIGGERED', # Use 'CONTINUOUS' if you want real-time updates
                primary_key="id",
                embedding_source_column="content",
                embedding_model_endpoint_name="databricks-bge-large-en" 
                )

                print(f"Index {INDEX_NAME} creation initiated. It will now begin embedding your Gwinzol data.")
        
        ### Similarity search :

                #### 1. Get the index object
                index = vsc.get_index(endpoint_name=VS_ENDPOINT_NAME, index_name=INDEX_NAME)

                #### 2. Ask a question!
                query = "Tell me about the Gwinzol's battery and charging speed."

                #### 3. Perform the similarity search
                results = index.similarity_search   (
                                                        query_text=query,
                                                        columns=["content"], # Return the text chunk
                                                        num_results=2        # Get the top 2 most relevant chunks
                                                    )

                #### 4. Extract the text to pass to an LLM later
                search_results = results.get('result', {}).get('data_array', [])

                for i, res in enumerate(search_results):
                    print(f"Result {i+1}: {res[0]}")
        
        ### Rough knowledge using mlflow :
                import mlflow.deployments

                # Connect to the Databricks Foundation Model API
                client = mlflow.deployments.get_deploy_client("databricks")

                # We will use Llama-3-70b as our "expert"
                LLM_ENDPOINT = "databricks-meta-llama-3-70b-instruct"


                def ask_gwinzol_expert(question):
                    # 1. RETRIEVAL: Find the most relevant facts from your index
                    results = index.similarity_search(
                        query_text=question,
                        columns=["content"],
                        num_results=3
                    )
                    
                    # 2. EXTRACT: Flatten the results into a single string of "Context"
                    data_array = results.get('result', {}).get('data_array', [])
                    context_text = "\n---\n".join([res[0] for res in data_array])
                    
                    # 3. AUGMENT & GENERATE: Build the prompt and call the LLM
                    prompt = f"""You are a luxury automotive expert for Gwinzol. 
                    Use the following pieces of retrieved context to answer the question. 
                    If you don't know the answer based on the context, say you don't know. 
                    Keep the answer professional and exciting.

                    Context:
                    {context_text}

                    Question: 
                    {question}

                    Answer:"""

                    response = client.predict(
                        endpoint=LLM_ENDPOINT,
                        inputs={
                            "messages": [
                                {"role": "user", "content": prompt}
                            ],
                            "max_tokens": 500,
                            "temperature": 0.1 # Low temperature for factual accuracy
                        }
                    )
                    
                    return response.choices[0]['message']['content']

                # Now we ask a complex question
                answer = ask_gwinzol_expert("What makes the Gwinzol's suspension so special?")

                print(f"AI RESPONSE:\n{answer}")















# ################################################################################ ROUGH work / BACKUP ################################################################################
    - Mosaic AI Vector Search is SERVERLESS (End point based) vector database on top of DELTA TABLES.
    - It performs all the VECTOR DB functionalities like STORAGE , INDEXING , SIMILARITY SEARCH.
    - Code :
            client = VectorSearchClient()
            # Or, if outside Databricks:
            # client = VectorSearchClient(
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



        SELECT 
        product_name, 
        ai_similarity(product_name, 'wireless headphones') AS match_score
        FROM products
        WHERE ai_similarity(product_name, 'wireless headphones') > 0.8
        ORDER BY match_score DESC



        ai_analyze_sentiment() -->> Detects if text is positive, negative, or neutral instantly.
        SELECT ai_analyze_sentiment("I love this product!")

        ai_classify() -->> Sorts text into custom categories you define.
        SELECT ai_classify(feedback, ARRAY('billing', 'tech', 'sales'))

        ai_extract() -->> Pulls specific data like dates or IDs out of messy text.
        SELECT ai_extract(email_body, ARRAY('order_number'))

        ai_summarize() -->> Condenses long articles or logs into a few short sentences.
        SELECT ai_summarize(meeting_notes, 2)

        ai_similarity() -->> Scores how closely two sentences match in meaning (0-1).
        SELECT ai_similarity('Apple iPhone', 'iPhone 15 Pro')

        ai_translate() -->> Converts text into any target language automatically.
        SELECT ai_translate(comment, 'es')

        ai_fix_grammar() -->> Polishes user-generated text by fixing typos and syntax.
        SELECT ai_fix_grammar('he do not know nothing')

        ai_gen() -->> Uses a prompt to generate custom content for every row.
        SELECT ai_gen('Write a polite reply to: ' || customer_query)

        ai_query() -->> Calls any custom or external LLM (like GPT-4) via endpoint.
        SELECT ai_query('gpt-4-endpoint', 'Analyze this risk: ' || report)





























PROMPT for learning : 
    Teach me about databricks sql function "ai_analyze_sentiment()" in the below given format ,
    1- What is it and what does it do ?
    2- When was it introduced into databricks sql ?
    3- Which AI model it uses , and is it PAY per token or something else
    4- Any other important points that I should know about this 

ai_analyze_sentiment() -->> Detects if text is positive, negative, or neutral instantly.
SELECT ai_analyze_sentiment("I love this product!")

ai_classify() -->> Sorts text into custom categories you define.
SELECT ai_classify(feedback, ARRAY('billing', 'tech', 'sales'))

ai_extract() -->> Pulls specific data like dates or IDs out of messy text.
SELECT ai_extract(email_body, ARRAY('order_number'))

ai_summarize() -->> Condenses long articles or logs into a few short sentences.
SELECT ai_summarize(meeting_notes, 2)

ai_similarity() -->> Scores how closely two sentences match in meaning (0-1).
SELECT ai_similarity('Apple iPhone', 'iPhone 15 Pro')

ai_translate() -->> Converts text into any target language automatically.
SELECT ai_translate(comment, 'es')

ai_fix_grammar() -->> Polishes user-generated text by fixing typos and syntax.
SELECT ai_fix_grammar('he do not know nothing')

ai_gen() -->> Uses a prompt to generate custom content for every row.
SELECT ai_gen('Write a polite reply to: ' || customer_query)

ai_query() -->> Calls any custom or external LLM (like GPT-4) via endpoint.
SELECT ai_query('gpt-4-endpoint', 'Analyze this risk: ' || report)
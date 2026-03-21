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
    - Vector Search
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

# Databricks VECTOR Database :
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




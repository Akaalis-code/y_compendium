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







# Create a MODEL endpoint :
    DATABRICKS UI -> Left Panel -> Serving -> Right side top "create serving endpoint"


# Cost realted info of endpoint :
    - The input and output DBU s for each foundational models are mentioned .
    - The model that you created runs on "SERVERLESS COMPUTE"  (Subject to verification)
    - If the model endpoint is not prompted for a while the serverless shuts down to least number of machines.
      In case while creating endpoint , if you had choosen option "SCALE TO ZERO" , then all compute shuts down 
      for this model .
      Generally in production you dont select this , so that SERVERLESS always stays live with minimum compute atleast.
    - There is a STOP button for your serverless to stop serving your model , 
      you can use that to incur low cost .

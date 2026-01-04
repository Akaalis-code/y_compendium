---------------------------------------------- Dont run this script , its just for reference ----------------------------------------------
from databricks.sdk import WorkspaceClient
import os

w = WorkspaceClient(
                        host=os.environ.get('var_workspace'),
                        token=os.environ.get('var_pat')
                    )

dbutils = w.dbutils

# Example: List files in a Volume
display(dbutils.fs.ls('/Volumes/y_ws_250705/y_schema_for_ai/y_volume_for_rag/'))


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







#pip install databricks-vectorsearch

from databricks.vector_search.client import VectorSearchClient
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


from databricks_langchain import DatabricksVectorSearch


vector_store = DatabricksVectorSearch(index_name = "<Your Vector Search Index Name>")
retriever    = vector_store.as_retriever(search_kwargs =    {{
                                                                "k": 3,   # Number of chunks that should be retured
                                                                "distance_threshold": 0.5,  # Only return results with a score better than 0.5 (Subject to verification)
                                                                "filters": {"department": "Engineering"} # Metadata filter (Subject to verification)
                                                            }}
                                        )
relavant_document = retriever.invoke("what is Databricks")
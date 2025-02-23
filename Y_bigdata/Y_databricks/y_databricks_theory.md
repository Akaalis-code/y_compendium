# NEW ARCHITECHTURE IMAGE

![New image of Architecture](./y_nontxt_resources/y_images/y_architechture.png)


# OLD ARCHITECHTURE IMAGE
<img src="./y_nontxt_resources/y_images/y_old_architech_of_Azdtbrks.png" alt="Old image of Architecture" width="700"/>





# CONNECTION of DATABRICKS WORKSPACE to ADLS GEN2 :
	WAY 1 :
		- In databricks there is "DBFS" file system 
		- DBFS is a distributed file system for interacting with cloud object storage.
		- You can see that in CATALOG panel top middle
		- If its not visible for first time you have to enable visibility in settings, follow below steps
			1. Go to the settings page.
			2. Click the Advanced tab.
			3. Click the DBFS File Browser toggle to enable or disable the setting.
		- For mounting any cloud object storage to DBFS , you have to use below command
			configs = {.....} #depending on your authentication method used configs gets keys and values accordingly
			dbutils.fs.mount(
								source = "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/",
								mount_point = "/mnt/<mount-name>",
								extra_configs = configs
							)
	
	WAY 2:
		- you can use SPARK config method to set whatever config you want to get authenticated 
		- example :
			spark.conf.set("...","...")
		- Number of configs may change according to your choosen authentication type
		- If these configs are set in cluster level then everyone who has access to cluster can use it (less safe)
		- or in your program alone you can set it (more safe)

# Authentication types to connect to cloud OBJECT storage :
	- ACCESS KEYS :
		spark.conf.set(
						"fs.azure.account.key.<storage-account>.dfs.core.windows.net",
						"<storage-account-access-key>"
						)
	- Shared Access Signature (SAS) :
	- Service principle



# Architecture elements of AZURE DATA BRICKS :
	Contol plane :
	Compute plane :
			Srverless Compute Plane :
			Classic Compute Plane :
	Data plane :



# Unity catalog heirarchy :
	1. Account level : 
			- Each Account (DataBricks or Azure) can contain N number of Workspaces and M number of 
				metastores(but only one metastore per region)
	2. Metastore :
			- Each metastore can contain N number of catalogs
			- "Hive metastore" , "samples" , "system" , "<your workspace named catalog>" these catalogs come by default
	3. Catalog :
	4. Schema / database :
	5. Tables , Views , functions

	When cluster is not started or not attached there is the following behaviour :
		1) Catalog will show tables present in all schemas except hive metastore
		2) DBFS file browser will show "hive metastore tables" but not normal catalog schema tables


# storage areas of DATA bricks elements :
	Notebooks :
	Results displayed in Notebooks :
	Compute resources :
	Workflows :
	Tables :
        

# Checking how different tables behave :
	- Managed tables (Will always maintain data in DELTA LAKE storage)
	- External tables
	- Views
	- Streaming table
	- Delta LIVE table
	- Streaming live table

	- Copy command
	- Autoloader

	- Permissions on objects



	Managed tables (Will always maintain data in DELTA LAKE storage)
			create or replace table y_most_basic_table 
				as
				(
						select 'r1c1' as COL1 ,'r1c2' as COL2 ,'r1c3' as COL3
				)
	External tables
	Streaming table
	Delta LIVE table
	Streaming live table


####################################### Prof certificate ######################################################################

dbutils.jobs.taskValues.get() :
dbutils.jobs.taskValues.set() :
	In a pipline , you can use this to set or get any particular parameters which needs to propogate information acrros 
	the tasks with in  a job 


dbutils.notebook.run("My Other Notebook", 60) :
dbutils.notebook.exit("My exit value")


dbutils.secrets.get(scope="my-scope", key="my-key"):
				.getbytes(..)
				.list(..)
				.listScopes(...)


dbutils.widgets......
dbutils.widgets.get('fruits_combobox')





CDC vs CDF 

microbatch._jdf

mlflow pyfunc spark_udf

.trigger()

All Describe cmds

Ganglia UI

ASSERT

DATABRICKS REST API 

.withWatermark("timestamp", "10 minutes") \
(max event time seen by the engine - late threshold > T)
## Environment info around azure :
    Suppose the root account at AZURE used for login is "azureroot@outlook.com".
    There will already be an "USER PRINCIPLE NAME" in ENTRA ID as "azureroot_outlook.com#EXT#@azurerootoutlook.onmicrosoft.com"



## New User setup :
    1) Create New user in Microsoft entra id , lets say for "user1" , it will be created as "user1@azurerootoutlook.onmicrosoft.com".

    2) If you directly go and login to ADB workspace with new user you will get below error :
            The workspace you are trying to access does not exist in this Azure region, 
            or your account user1@azurerootoutlook.onmicrosoft.com does not belong to any Databricks workspace 
            in the region. Please ask your administrator to add you as a user, or click here to 
            logout of Microsoft Entra ID and login with a different user.

    3) You need to work on giving some permissions to "user1@azurerootoutlook.onmicrosoft.com".
        3.1)    log into accounts.azuredatabricks.net with "azureroot_outlook.com#EXT#@azurerootoutlook.onmicrosoft.com"
                Note : "azureroot@outlook.com" will not work to login to accounts.azuredatabricks.net
        3.2)    Add new user into the databricks workspace account :
                    left panel -> User management -> Users -> Add user 
                    Search for "user1@azurerootoutlook.onmicrosoft.com" and add the user 
        3.3)    Give that user "user1@azurerootoutlook.onmicrosoft.com" permissions on workspace :
                    left panel -> workspaces -> select your workspace -> Top middle panel -> Permissions 
                    -> Add permissions -> Search your user -> add him either as ADMIN or USER.

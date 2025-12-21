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
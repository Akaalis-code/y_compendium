1) Whole Policing the ACCESES revolves around two concepts :
        Authentication: Any PERSON , APPLICATION or OBJECT will be given an "userid" and "password" 
                        to recognize them later with those things 
        Authorization:  Once AUTHENTICATION is done , What that AUTHENTICATED individual can or allowed
                        to do is goverened by this 

2) In Azure We have below terminology :
        Azure Account: Your overall account to start you Azure journey. Also your billing account

        Azure AD: Your directory for authentication and authorization

        Azure Subscription: The container where your created resources are created. Billing is per subscription

        (multiple subscription can have the same Azure AD). You can also set specific Azure policies on subscription level.

        
        USER 
        TENANT / Directory : I think its related to DOMAIN or ORAGANIZATION level you can create users with domain name after @ symbol
        SUBSCRIPTION
        LICESENCE


## Experiment 1 
    I have Azure Root account lets say ACC1 , I created another user from Microsoft ENTRA ID lets say ACC2 
    To be able to see all ACC1 resources from ACC2 Azure portal , From SUBSCRIPTION of Azure 1 READ ROLE has been assigned 
    to ACC2 from ACC1


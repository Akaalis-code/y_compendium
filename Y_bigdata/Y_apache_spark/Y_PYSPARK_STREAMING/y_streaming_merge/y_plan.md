1) Bronze table will be created and continuously updated through STRUCTURED STREAMING from a folder location
    Bronze schema :
        brnz_primary_key_col string,
        brnz_column_2        string,
        brnz_updt_date_time  Datetime
    
    Bronze data load understanding :
        Bronze data might have late records under a primary key section

2) Silver table :
    Silver schema :
        slvr_primary_key_col string,
        slvr_column_2        string,
        slvr_updt_date_time  Datetime
    
    Silver data load understanding :
        Silver should be Upserted with latest records only , from bronze
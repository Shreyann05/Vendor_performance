    # install the package if it isn’t already available
# %pip install sqlalchemy

import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename= "logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


engine = create_engine('sqlite:///data.db')

def ingest_db(df, table_name, engine):
    '''
    this function takes a dataframe, table name and engine as input and ingests the data into the database

    '''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():  
    ''' 
    this function loads the raw data from the data folder and returns a list of dataframes and ingest into db
    '''
    start = time.time()  
    for file in os.listdir('data'):
            if '.csv' in file:
                df = pd.read_csv('data/' + file)
                logging.info(f"Loaded {file} successfully.")
                ingest_db(df, file[:-4], engine)
    end = time.time()
    Total_time = (end - start)/60
    logging.info(f"Total time taken: {Total_time} seconds")
    logging.info("All files have been loaded and ingested into the database.")            


if __name__ == "__main__":
    load_raw_data()    
import psycopg2 as p2
import pandas as pd
from typing import List, Tuple, Union

import Project_errors as err


class MyDB():
    def __init__(self, user: str = "PgSany0", password: str = "DamnSQL", db_name: str = "FourthML"):
        self.__user = user
        self.__password = password
        self.__db_name = db_name
        self.__is_active = False
        
    def connect_to_db(self):
        try:
            self.__connect = p2.connect(
                dbname = self.__db_name,
                user = self.__user,
                password = self.__password,
                host = "localhost",
                port = "5432"   
            )
        
            self.__cursor = self.__connect.cursor()
            
            self.__is_active = True
        except Exception:
            raise err.NOT_SUCCESSFUL_CONNECT()
    
    def insert_query(self, query: str, values: Union[List, Tuple] = None):
        if not self.__is_active:
            raise err.NOT_ACTIVE_DB()
        elif query is None:
            raise err.VOID_QUERY()
        elif "insert " not in query.lower():
            raise err.BAD_INSERT_QUERY()
        
        try:
            self.__cursor.executemany(query=query, vars_list=values)
            self.__connect.commit()
            
        except p2.DatabaseError as DE:
           self.__connect.rollback()
           
           raise err.BAD_INSERT_QUERY()      
    
    def select_query(self, query: str, values: Union[List, Tuple] = None, chunk_size: int = 100) -> pd.DataFrame:
        if not self.__is_active:
            raise err.NOT_ACTIVE_DB()
        elif query is None:
            raise err.VOID_QUERY()
        elif "select " not in query.lower():
            raise err.BAD_SELECT_QUERY()
        
        try:
            self.__cursor.execute(query=query, vars=values)
            
            columns = [desc[0] for desc in self.__cursor.description]
            
            chunks = []

            while True:
                rows = self.__cursor.fetchmany(chunk_size)
                
                if not rows:
                    break

                chunks.append(pd.DataFrame(rows, columns=columns))

            if chunks:
                df_main = pd.concat(chunks, ignore_index=True)
            else:
                df_main = pd.DataFrame(columns=columns)
                   
        except p2.DatabaseError as DE:
           self.__connect.rollback()
           
           raise err.BAD_INSERT_QUERY()
        
        return df_main
    
    def close_db(self):
        self.__connect.close()
        self.__cursor.close()
        self.__is_active = False
        
    def __del__(self):
        self.close_db()
    
    @property
    def is_active(self):
        return self.__is_active
    
if __name__ == "__main__":
    db = MyDB()
    db.connect_to_db()
    df = db.select_query(query="""
                    SELECT * FROM salaries
                    LIMIT 100;""")
    db.close_db()

    with open("D:\\Salary-prediction\\job_salary_prediction_dataset.csv") as file:
        batch_size = 100
        container = []
        head = file.readline()
        query = """INSERT INTO salaries (job_title,experience_years,education_level,
                                        skills_count,industry,company_size,
                                        location,remote_work,certifications,
                                        salary)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    
        for row in file:
            row = row.rstrip('\n')
            row_ = row.split(',')

            row_[1] = int(row_[1])
            row_[3] = int(row_[3])
            row_[8] = int(row_[8])
            row_[9] = int(row_[9])
            
            container.append(row_)
            
            if len(container) == batch_size:
                db.insert_query(query=query, values=container)
                container.clear()
                
        if len(container) != 0:
            db.insert_query(query=query, values=container)


        
        
        
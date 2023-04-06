import sys
import json
import psycopg2
from datetime import datetime

class Database:
    def __init__(self, db_config_file_name:str) -> None:
        self.file_name = db_config_file_name
        self.content = dict()
        self.GetDbInfo()
        self.CreateDbConnection()
        self.GetTableContents()

    def GetDbInfo(self):
        try:
            with open("database/db_config/config_files/"+self.file_name, 'r') as f:
                self.db_info = json.load(f)
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def CreateDbConnection(self):
        print(self.db_info)
        try:
            self.connection = psycopg2.connect(host=self.db_info["host"], user=self.db_info["user"], password=self.db_info["password"], database=self.db_info["database"],
                                     port=int(self.db_info["port"]))
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def GetTableContents(self):
        for table in self.db_info["tables"]:
            query = "select * from " + table
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    res = cursor.fetchall()
            except Exception() as ex:
                print(ex)
                continue
            finally:
                self.content[self.file_name[:-5]+"_"+(table+"_".join(str(datetime.now()).split()))] = res
        self.CloseConnection()

    def CloseConnection(self):
        try:
            self.connection.close()
        except Exception as ex:
            print(ex)
            sys.exit(1)
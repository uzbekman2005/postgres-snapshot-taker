from database.db_config.db_config import Database
import csv
import os

class DbController:
    def __init__(self, db_config_file_name, path_to_save):
        self.file_name = db_config_file_name
        self.path = path_to_save
        self.res_files = []

    def GetDatabaseSnapshot(self):
        if not os.path.exists("files"):
            os.makedirs("files")

        db = Database(self.file_name)
        for k, v in db.content.items():
            fname = k+".csv"
            with open(self.path+fname, "w", newline="") as f:
                writer = csv.writer(f)
                for one_v in v:
                    try: 
                        writer.writerow(one_v)
                    except Exception as ex:
                        print(ex)
                        break
                self.res_files.append(fname)

    def DeleteSnapshotFiles(self):
        for fn in self.res_files:
            if os.path.exists(self.path+fn):
                os.remove(self.path+fn)
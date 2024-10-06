import os
import json
from project import config

def load_map_data(path):
    work_path = config.WORK_PATH
    res_path = os.path.join(work_path, "src/table/json/map", path)
    file_ins = open(res_path, "rb")
    data = json.load(file_ins)
    return data
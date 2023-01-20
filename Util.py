import datetime
import os

username = os.path.expanduser("~")
errorlogPath = os.path.join(username, "Documents", "LuaCreator", "Errorlog")
errorlogFile = "_errorlog.txt"

class Util():
    def __init__(self):
        super().__init__()
    
    def getDateNow(self):
        now_file_creation_date = datetime.datetime.now()
        creation_day = now_file_creation_date.day
        creation_month = now_file_creation_date.month
        creation_year = now_file_creation_date.year
        creation_hour = now_file_creation_date.hour
        creation_hour = "{:02d}".format(creation_hour)
        creation_minute = now_file_creation_date.minute
        creation_minute = "{:02d}".format(creation_minute)
        creation_second = now_file_creation_date.second
        creation_second = "{:02d}".format(creation_second)
        creation_date = str(f"{creation_day}-{creation_month}-{creation_year}_{creation_hour}-{creation_minute}-{creation_second}")
        return creation_date

    def errorHandling(self, error_file, error, prefix):
        if not os.path.exists(errorlogPath):
            os.makedirs(errorlogPath)
        if not os.access(errorlogPath, os.W_OK):
            os.chmod(errorlogPath, 0o700)
        with open(errorlogPath + "/" + prefix + errorlogFile, "a") as f:
            if error == "xml-error":
                f.write(f"{self.getDateNow()} XML error in file: {error_file}.\n")
            elif error == "not-found":
                f.write(f"{self.getDateNow()} File not found error for: {error_file}\n")
    
    def print_vehicle_array(self, path, vehicle_array, price, shop):
        for vehicle in vehicle_array:
            with open(path, "a") as f:
                f.writelines([
                    f"   ['{vehicle['model_name']}'] = {{\n",
                    f"       ['name'] = '{vehicle['game_name']}',\n",
                    f"       ['brand'] = '{vehicle['brand']}',\n",
                    f"       ['model'] = '{vehicle['model_name']}',\n",
                    f"       ['price'] = {price},\n",
                    f"       ['catagory'] = '{vehicle['catagory']}',\n",
                    f"       ['hash'] = `{vehicle['hash']}`,\n",
                    f"       ['shop'] = '{shop}',\n",
                    f"  }},\n",
                ])
    
    def print_vehicle_array_esx_list(self, path, vehicle_array, price):
        for vehicle in vehicle_array:
            with open(path, "a") as f:
                f.writelines([
                    f"            {{ model = '{vehicle['model_name']}', label = '{vehicle['game_name']}', price = {price}}},\n"
                ])
    
    def print_vehicle_array_qubus_list(self, path, vehicle_array):
        for vehicle in vehicle_array:
            with open(path, "a") as f:
                f.writelines([
                    f'    ["{vehicle["game_name"]}"] = "{vehicle["model_name"]}",\n'
                ])
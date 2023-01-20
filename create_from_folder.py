import os
import xml.etree.ElementTree as ET
from open_close import Open_close as oc
from Util import Util
username = os.path.expanduser("~")
luaOutputPath = os.path.join(username, "Documents", "LuaCreator", "luaOutput")
luaFile = "_vehicles.lua"
U = Util()

TYPE_CAR = "VEHICLE_TYPE_CAR"
TYPE_BIKE = "VEHICLE_TYPE_BIKE"
TYPE_HELI = "VEHICLE_TYPE_HELI"
TYPE_BOAT = "VEHICLE_TYPE_BOAT"
TYPE_TRAILER = "VEHICLE_TYPE_TRAILER"
TYPE_PLANE = "VEHICLE_TYPE_PLANE"
TYPE_SUBMARINE = "VEHICLE_TYPE_SUBMARINE"
TYPE_BICICLE = "VEHICLE_TYPE_BICYCLE"
TYPE_BLIMP = "VEHICLE_TYPE_BLIMP"
TYPE_QUADS = "VEHICLE_TYPE_QUADBIKE"
TYPE_AMPHIBIOUS = "VEHICLE_TYPE_AMPHIBIOUS_AUTOMOBILE"
TYPE_TRAIN = "VEHICLE_TYPE_TRAIN"
cars = []
bikes = []
helicopters = []
trailers = []
boats = []
planes = []
submarines = []
bicicles = []
blimps = []
quads = []
amphibiouses = []
trains = []
type_unkown = []

class Create_from_folder():
    def __init__(self):
        super().__init__()

    def create_lua_from_folder_structure(self, xml_file, luaCreation_date, shop, price):
        tree = None
        try:
            tree = ET.parse(xml_file)
        except ET.ParseError as e:
            U.errorHandling(xml_file, "xml-error", luaCreation_date) 

        if tree is not None:
            root = tree.getroot()
            init_datas = root.find("InitDatas")
            for item in init_datas.findall("Item"):
                #collecting the data
                catagory = "compacts"
                vehicle_type = item.find("type").text
                model_name = item.find("modelName").text
                game_name = item.find("gameName").text
                brand = item.find("vehicleMakeName").text
                vehicleHash = model_name
                #put in repectif array
                if vehicle_type == TYPE_CAR:
                    cars.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_BIKE:
                    bikes.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_HELI:
                    helicopters.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_BOAT:
                    boats.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_TRAILER:
                    trailers.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_PLANE:
                    planes.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_SUBMARINE:
                    submarines.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_BICICLE:
                    bicicles.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_BLIMP:
                    blimps.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_QUADS:
                    quads.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_AMPHIBIOUS:
                    amphibiouses.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                elif vehicle_type == TYPE_TRAIN:
                    trains.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory})
                else:
                    type_unkown.append({"model_name" : model_name, "game_name" : game_name, "brand" : brand, "hash" : vehicleHash, "catagory" : catagory, "type" : vehicle_type})

    def get_brand_paths(self, cars_dir):
        dirs = os.listdir(cars_dir)
        dirs=[os.path.join(cars_dir, d) for d in dirs if os.path.isdir(os.path.join(cars_dir, d))]
        brandPaths = {}
        i=1
        for dir in dirs:
            brandPaths[i] = str(dir)
            i += 1
        return brandPaths

    def get_model_paths(self, brandPaths):
        modelPaths = []
        k=1
        for path in brandPaths:
            dirs = os.listdir(brandPaths[k])
            for dir in dirs:
                modelPaths.append(str(brandPaths[k]) + str("/") + str(dir))
            k +=1
        return modelPaths

    def create_lua_from_folder_collection(self, dirs, prefix, shop, price, lua_type):
        print(f"dirs is: {dirs}\nprefix is: {prefix}\nshop is: {shop}\nprice is: {price}")
        modelPaths = self.get_model_paths(self.get_brand_paths(dirs))
        for path in modelPaths:  
            if os.path.exists(path + '/vehicles.meta') and os.path.isfile(path + '/vehicles.meta'):
                self.create_lua_from_folder_structure(path + '/vehicles.meta', prefix, shop, price)
            else:
                U.errorHandling(path + '/vehicles.meta', "not-found", prefix)
        lua_file_path = luaOutputPath + prefix + luaFile
        if lua_type == "normal lua":
            oc.print_start_lua_script(prefix) 
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE CAR\n\n")
            U.print_vehicle_array(lua_file_path, cars, shop, price)
            cars.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BIKE\n\n")
            U.print_vehicle_array(lua_file_path, bikes, shop, price)
            bikes.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE HELI\n\n")
            U.print_vehicle_array(lua_file_path, helicopters, shop, price)
            helicopters.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BOAT\n\n")
            U.print_vehicle_array(lua_file_path, boats, shop, price)
            boats.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE TRAILER\n\n")
            U.print_vehicle_array(lua_file_path, trailers, shop, price)
            trailers.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE PLANE\n\n")
            U.print_vehicle_array(lua_file_path, planes, shop, price)
            planes.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE SUBMARINE\n\n")
            U.print_vehicle_array(lua_file_path, submarines, shop, price)
            submarines.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BICICLE\n\n")
            U.print_vehicle_array(lua_file_path, bicicles, shop, price)
            bicicles.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BLIMP\n\n")
            U.print_vehicle_array(lua_file_path, blimps, shop, price)
            blimps.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE QUADBIKE\n\n")
            U.print_vehicle_array(lua_file_path, quads, shop, price)
            quads.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE AMPHIBIOUS AUTOMOBILE\n\n")
            U.print_vehicle_array(lua_file_path, amphibiouses, shop, price)
            amphibiouses.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE TRAIN\n\n")
            U.print_vehicle_array(lua_file_path, trains, shop, price)
            trains.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE UNKOWN\n\n")
            U.print_vehicle_array(lua_file_path, type_unkown, shop, price)
            type_unkown.clear()
            oc.print_close_lua_script(prefix)
        elif lua_type == "esx list":
            oc.print_open_esx_script(prefix) 
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE CAR\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, cars, price)
            cars.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BIKE\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, bikes, price)
            bikes.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE HELI\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, helicopters, price)
            helicopters.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BOAT\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, boats, price)
            boats.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE TRAILER\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, trailers, price)
            trailers.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE PLANE\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, planes, price)
            planes.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE SUBMARINE\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, submarines, price)
            submarines.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BICICLE\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, bicicles, price)
            bicicles.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BLIMP\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, blimps, price)
            blimps.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE QUADBIKE\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, quads, price)
            quads.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE AMPHIBIOUS AUTOMOBILE\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, amphibiouses, price)
            amphibiouses.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE TRAIN\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, trains, price)
            trains.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE UNKOWN\n\n")
            U.print_vehicle_array_esx_list(lua_file_path, type_unkown, price)
            type_unkown.clear()
            oc.close_esx_script(prefix)
        elif lua_type == "qubus list":
            oc.print_open_qubus_script(prefix) 
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE CAR\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, cars)
            cars.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BIKE\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, bikes)
            bikes.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE HELI\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, helicopters)
            helicopters.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BOAT\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, boats)
            boats.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE TRAILER\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, trailers)
            trailers.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE PLANE\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, planes)
            planes.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE SUBMARINE\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, submarines)
            submarines.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BICICLE\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, bicicles)
            bicicles.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE BLIMP\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, blimps)
            blimps.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE QUADBIKE\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, quads)
            quads.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE AMPHIBIOUS AUTOMOBILE\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, amphibiouses)
            amphibiouses.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE TRAIN\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, trains)
            trains.clear()
            with open(lua_file_path, "a") as f:
                f.write("--VEHICLE TYPE UNKOWN\n\n")
            U.print_vehicle_array_qubus_list(lua_file_path, type_unkown)
            type_unkown.clear()
            oc.print_close_qubus_script(prefix)
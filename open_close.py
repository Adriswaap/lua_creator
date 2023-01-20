import os
username = os.path.expanduser("~")
luaOutputPath = os.path.join(username, "Documents", "LuaCreator", "luaOutput")
luaFile = "_vehicles.lua"
class Open_close():
    def print_start_lua_script(luaCreation_date):
        if not os.path.exists(luaOutputPath):
            os.makedirs(luaOutputPath)
        if not os.access(luaOutputPath, os.W_OK):
            os.chmod(luaOutputPath, 0o700)
        with open(luaOutputPath + luaCreation_date + luaFile, "a") as f:
            f.writelines([
                """QBShared = QBShared or {}\n""",
                """QBShared.VehicleHashes = {}\n""",
                "\n",
                "QBShared.Vehicles = {\n" 
            ])

    def print_close_lua_script(luaCreation_date):
        if not os.access(luaOutputPath, os.W_OK):
            os.chmod(luaOutputPath, 0o700)
        with open(luaOutputPath + luaCreation_date + luaFile, "a") as f:
            f.writelines([
                "}\n",
                "\n",
                "for _, v in pairs(QBShared.Vehicles) do\n",
                "   QBShared.VehicleHashes[v.hash] = v\n",
                "end",
            ])
    
    def print_open_esx_script(luaCreation_date):
        if not os.path.exists(luaOutputPath):
            os.makedirs(luaOutputPath)
        if not os.access(luaOutputPath, os.W_OK):
            os.chmod(luaOutputPath, 0o700)
        with open(luaOutputPath + luaCreation_date + luaFile, "a") as f:
            f.writelines([
                "Config.AuthorizedVehicles = {\n",
                "    Shared = {\n"
            ])
    
    def close_esx_script(luaCreation_date):
        if not os.access(luaOutputPath, os.W_OK):
            os.chmod(luaOutputPath, 0o700)
        with open(luaOutputPath + luaCreation_date + luaFile, "a") as f:
            f.writelines([
                "\n",
                "},"
            ])

    def print_open_qubus_script(luaCreation_date):
        if not os.path.exists(luaOutputPath):
            os.makedirs(luaOutputPath)
        if not os.access(luaOutputPath, os.W_OK):
            os.chmod(luaOutputPath, 0o700)
        with open(luaOutputPath + luaCreation_date + luaFile, "a") as f:
            f.writelines([
                "Config.Vehicles = {\n"
            ])
    
    def print_close_qubus_script(luaCreation_date):
        if not os.access(luaOutputPath, os.W_OK):
            os.chmod(luaOutputPath, 0o700)
        with open(luaOutputPath + luaCreation_date + luaFile, "a") as f:
            f.writelines([
                "}"
            ])
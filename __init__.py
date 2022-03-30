import os

root_path = os.path.dirname(__file__) #.../scriptsInTools/
ui_folder = os.path.join(root_path,"ui")

maya_folder = os.path.join(root_path,"maya")
maya_settings_folder = os.path.join(maya_folder,"_settings")
maya_data_folder = os.path.join(maya_folder,"data")
maya_execute_folder = os.path.join(maya_folder,"execute")
maya_library_folder = os.path.join(maya_folder,"library")
maya_manager_folder = os.path.join(maya_folder,"manager")

mgear_folder = os.path.join(root_path,"mgear")
mgear_settings_folder = os.path.join(mgear_folder,"_settings")
mgear_data_folder = os.path.join(mgear_folder,"data")
mgear_execute_folder = os.path.join(mgear_folder,"execute")
mgear_library_folder = os.path.join(mgear_folder,"library")
mgear_manager_folder = os.path.join(mgear_folder,"manager")
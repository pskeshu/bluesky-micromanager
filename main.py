import pymmcore
import ophyd

def create_mmc_obj(mm_dir, config_path):
    mmc = pymmcore.CMMCore()
    mmc.setDeviceAdapterSearchPaths([mm_dir])
    mmc.loadSystemConfiguration(config_path)
    return mmc

def make_ophyd_objects_from_mmc(mmc):
    o = MMC_Interface(mmc)
    return o


def ophyd_mm_interface(mm_dir, mm_config_file):
    mmc = create_mmc_obj(mm_dir, mm_config_file)
    ophyd_objects = make_ophyd_objects_from_mmc(mmc)
    return ophyd_objects


class MMDevice:
    def __init__(self, name):
        self.name = name
        self.properties = {}

    def get_properties(self, mmc):
        props = mmc.getDevicePropertyNames(self.name)

        for prop in props:
            self.properties[prop] = mmc.getProperty(self.name, prop)
        

class MMC_Interface:
    def __init__(self, mmc):
        self.mmc = mmc
        self.devices = {}

    def init_devices(self):
        list_of_devices = self.mmc.getLoadedDevices()
        for device in list_of_devices:
            dev = MMDevice(device)
            dev.get_properties(self.mmc)
            self.devices[device] = dev
            

mm_dir = "/usr/local/lib/micro-manager"
mm_config_file = "./demo.cfg"

o = ophyd_mm_interface(mm_dir, mm_config_file)

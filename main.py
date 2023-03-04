import pymmcore
import ophyd

def create_mmc_obj(mm_dir, config_path):
    mmc = pymmcore.CMMCore()
    mmc.setDeviceAdapterSearchPaths([mm_dir])
    mmc.loadSystemConfiguration(config_path)
    return mmc

def make_ophyd_objects_from_mmc(mmc):
    pass


def ophyd_mm_interface(mm_dir, mm_config_file):
    mmc = create_mmc_obj(mm_dir, mm_config_file)
    ophyd_objects = make_ophyd_objects_from_mmc(mmc)
    return ophyd_objects

ophyd_objects = ophyd_mm_interface(mm_dir, mm_config_file)

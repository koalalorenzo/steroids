import os


def create_directories(basepath, name, directiores):
    """
        Create the directories
    """
    for path in directiores:
        path = path.replace("[base]", basepath)
        path = path.replace("[name]", name)
        
        if not os.path.exists(path):
            os.mkdir(path)

def touch_files(basepath, name, files):
    """
        Touch the files
    """
    for path in files:
        path = path.replace("[base]", basepath)
        path = path.replace("[name]", name)
        
        if not os.path.exists(path):
            open(path, 'w').close()
            
def install_module(module, basepath, name, examples=False):
    create_directories(basepath, name, module.directories)
    touch_files(basepath, name, module.files)
    module.install(basepath, name)
    if examples:
        module.install_examples(basepath, name)
    
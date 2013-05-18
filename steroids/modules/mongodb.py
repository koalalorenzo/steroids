requirements = [
    "pymongo"
]

directories = [
    "[base]/[name]",
    "[base]/[name]/objects",
]

files = [
    "[base]/[name]/__init__.py",
    "[base]/[name]/objects/__init__.py",
    "[base]/[name]/objects/Master.py",
]

def install(basepath, name):
    """
        Install Flask Module
    """
    
    objectMaster_file = open(os.path.join(basepath,"%s/objects/Master.py"), "w")
    objectMaster_file.write("\n")
    objectMaster_file.close()
    
    return
    
def install_examples(basepath, name):
    """
        Install Flask Module
    """
    return
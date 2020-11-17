import os, json

class SysTools(object):
    def get_conf_from_files(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                jsFile = json.loads(f.read())
                return jsFile
        else:
            print("ERROR: file {} not exist!!!".format(filename))
            return -1
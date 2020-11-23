import os, json

class SysTools(object):
    def get_conf_from_files(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                try:
                    jsFile = json.loads(f.read())
                    return jsFile
                except json.JSONDecodeError as err:
                    # print("------------------------------------\n"
                    #       "filepath:{} \nerr:{}\n"
                    #       "------------------------------------\n".format(filename, err))
                    return -1
        else:
            print("ERROR: file {} not exist!!!".format(filename))
            return -1
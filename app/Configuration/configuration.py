import yaml


class Configuration:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__init_configuration_with_file(filepath=filepath)

    def __init_configuration_with_file(self, filepath):
        if filepath.endswith('/'):
            filepath = filepath.rstrip('/')

        with open(filepath) as configuration_file:
            self.loaded = yaml.full_load(configuration_file)

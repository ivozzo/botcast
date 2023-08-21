import yaml


class Configuration:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.__init_configuration_with_file(path=path, filename=filename)

    def __init_configuration_with_file(self, path, filename):
        if path.endswith('/'):
            path = path.rstrip('/')

        with open(f'{path}/{filename}') as configuration_file:
            self.loaded = yaml.full_load(configuration_file)

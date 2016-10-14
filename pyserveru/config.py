from configparser import NoOptionError, NoSectionError, RawConfigParser


class EnvConfig:

    def __init__(self, config_path):
        self._webapp_config = RawConfigParser()
        self._webapp_config.read(config_path)

    def _get_key(self, type, section, key, default):
        """
            Read key in a configuration file, avoiding key reading errors
        """
        try:
            if type == 'string':
                return self._webapp_config.get(section, key).strip("'")
            elif type == 'int':
                return self._webapp_config.getint(section, key)
            elif type == 'bool':
                return self._webapp_config.getboolean(section, key)
            else:
                raise Exception('Unknown type %s' % type)
        except (NoOptionError, NoSectionError):
            return default

    def get_str_key(self, section, key, default=""):
        return self._get_key('string', section, key, default)

    def get_int_key(self, section, key, default=0):
        return self._get_key('int', section, key, default)

    def get_bool_key(self, section, key, default=False):
        return self._get_key('bool', section, key, default)

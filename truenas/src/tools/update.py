import configparser

config = configparser.ConfigParser()
config.read(r'\\TRUENAS\suporte\SUPORTE\CentralSuporte\settings.cfg')

settings = config.defaults()
print(settings['users'].split(', '))
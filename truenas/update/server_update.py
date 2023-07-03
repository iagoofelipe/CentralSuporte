""" 
Informações para atualização
"""

SERVER_ADDRESS = r'\\TRUENAS\suporte\SUPORTE\CentralSuporte'
__version__ = '1.0.2'

#-----------------------------------------------------------------------------------------------
""" gerando arquivo settings.cfg """
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {

  'SERVER_ADDRESS': SERVER_ADDRESS,
  '__version__': __version__,
  'users': 'IAGO, HEVERTON, SAMUEL, JOAO, PEDRO'

  }

with open(r'\\TRUENAS\suporte\SUPORTE\CentralSuporte\settings.cfg', 'w') as configfile:
  config.write(configfile)
#-----------------------------------------------------------------------------------------------
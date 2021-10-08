import configparser

config = configparser.ConfigParser()

config['General'] = {'chrome' : 'C:\driverChrome\chromedriver.exe'}
config['Pages'] = {'page' : 'https://www.google.com.mx'}

with open('configuration.ini', 'w') as configfile:
    config.write(configfile)
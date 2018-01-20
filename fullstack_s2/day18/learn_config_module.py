#__author:  "Jing Xu"
#date:  2018/1/20

import configparser

config = configparser.ConfigParser()

config["DEFAULT"] = {'ServerAliveInter':{'45':666},
					 'Compression':'Yes',
					 'CompressinLevel':'9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'Yes'

with open('example.ini','w') as configfile:
	config.write(configfile)

config.read('example.ini')
print(config.sections())
print(config.defaults())
config.set('bitbucket.org','user','alex')
print(config['bitbucket.org']['User'])
for key in config['bitbucket.org']:
	print(key)

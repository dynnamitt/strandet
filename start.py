
from game import data
print(data)

# husk pip3 install yaml
import yaml


with open(r'game.dat.yaml') as file:
	dict1 = yaml.load(file, Loader=yaml.FullLoader)
	print(dict1)
	print(type(dict1))


with open(r'liste.yaml') as file:
	x = yaml.load(file, Loader=yaml.FullLoader)
	print(x)
	print(type(x))

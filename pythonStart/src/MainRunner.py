from Modules.WebModule import ModuleFunc
from Modules.WebModule import userMapping

ModuleFunc()

print(userMapping)

mappingCopy = dict(userMapping)

printedMappingCopy = str(mappingCopy)

print('The copy is ' + printedMappingCopy)
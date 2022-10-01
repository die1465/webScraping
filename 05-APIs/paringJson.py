import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)
print(jsonObj.get('arrayOfNums'))
print(jsonObj.get('arrayOfNums')[1]) 
print(jsonObj.get('arrayOfNums')[1].get('number') +
jsonObj.get('arrayOfNums')[2].get('number')) 
print(jsonObj.get('arrayOfFruits')[2].get('fruit'))

"""
to find undocumented APIs monitor the network and look
for api calls
they usually have .json or .xml at the end of it
usually of the type xhr
"""

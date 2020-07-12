from datetime import date

d = ['one', 'two']

import json

json_obj = json.dumps(d)
print(json_obj)

dd = json.loads(json_obj)
print(type(dd))
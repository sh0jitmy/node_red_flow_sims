import json
import base64
#import bytes 

msg = {}
msg["payload"] = open('reginfo.json','r')
json_load = json.load(msg["payload"])
payload = bytearray(b'\x00\x00\x00\x00')

#print(json_load)
for  v in json_load :
	address = v['address'].replace('0x','')
	value = v['value'].replace('0x','')
	addr_byte = bytes.fromhex(address)
	value_byte = bytes.fromhex(value)
	payload+=addr_byte
	payload+=value_byte
base64 = base64.b64encode(payload)
print(base64)
#return base64

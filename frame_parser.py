import json

exported_packets = "/path/to/your/exported.json"

with open(exported_packets, 'r') as F:
	frames = json.loads(F.read())

for i, f in enumerate(frames):
	frame = f['_source']['layers']

	print("{0}. At {1}, {2} sent data to {3}".format(i, frame['frame']['frame.time'],
		frame['ip']['ip.src_host'], frame['ip']['ip.dst_host']))
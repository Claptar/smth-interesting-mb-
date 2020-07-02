import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if args.key and args.val:
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            data = json.loads(f.read())
        if args.key in data:
            data[args.key].append(args.val)
        else:
            data[args.key] = [args.val]
    else:
        data = {args.key: [args.val]}
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))
elif args.key:
    if os.path.exists(storage_path):
        with open(storage_path, 'r') as f:
            data = json.loads(f.read())
            print(', '.join(data[args.key]) if args.key in data else '')

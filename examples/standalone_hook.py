#!/usr/bin/env python3.6
"""
This is an example bare-bone script that you can use as an argument for
setting up an output hook.

>>> $ detect-secrets-server scan yelp/detect-secrets
...     --output-hook examples/standalone_hook.py
"""
import json
import sys


def main():
    print('repo:', sys.argv[1])
    print(json.dumps(json.loads(sys.argv[2]), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

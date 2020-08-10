#!/usr/bin/env python3

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', required=True)
parser.add_argument('-m', '--model', required=True)
parser.add_argument('-i', '--image', required=False, default='')
args = parser.parse_args()

MODEL_MAP = {
    "C9300": [
        {
            "image": "cat9k_iosxe.16.12.03a.SPA.bin",
            "version": "16.12.03a",
            "license": None
        }
    ],
    "C2960X": [
        {
            "image": "c2960x-universalk9-mz.152-7.E2.bin",
            "version": "15.2(7)E2",
            "license": None
        }
    ],
    "C3560CX": [
        {
            "image": "c3560cx-universalk9-mz.152-7.E2.bin",
            "version": "15.2(7)E2",
            "license": None
        }
    ],
    "C2960": [
        {
            "image": "c2960-lanbasek9-mz.150-2.SE11.bin",
            "version": "15.0(2)SE11",
            "license": "lanbase"
        },
        {
            "image": "c2960-lanlitek9-mz.150-2.SE11.bin",
            "version": "15.0(2)SE11",
            "license": "lanlite"
        }
    ],
    "C3560": [
        {
            "image": "c3560-ipbasek9-mz.150-2.SE11.bin",
            "version": "15.0(2)SE11",
            "license": "ipbase"
        },
        {
            "image": "c3560-ipservicesk9-mz.150-2.SE11",
            "version": "15.0(2)SE11",
            "license": "ipservices"
        }
    ],
    "C3560C": [
        {
            "image": "c3560-ipbasek9-mz.150-2.SE11.bin",
            "version": "15.0(2)SE11",
            "license": "ipbase"
        },
        {
            "image": "c3560-ipservicesk9-mz.150-2.SE11",
            "version": "15.0(2)SE11",
            "license": "ipservices"
        }
    ],
    "C3750": [
        {
            "image": "c3750-ipbasek9-mz.150-2.SE11.bin",
            "version": "15.0(2)SE11",
            "license": "ipbase"
        },
        {
            "image": "c3750-ipservicesk9-mz.150-2.SE11",
            "version": "15.0(2)SE11",
            "license": "ipservices"
        }
    ]   
}

if "lanlite" in args.image:
    lic = "lanlite"
elif "lanbase" in args.image:
    lic = "lanbase"
elif "ipbase" in args.image:
    lic = "ipbase"
elif "ipservices" in args.image:
    lic = "ipservices"
else:
    lic = None

model = args.model.split('-')

if model[0] == "WS":
    model.pop(0)

target = MODEL_MAP.get(model[0])

results = {}

if not target:
    results = {
        "success": False,
        "msg": "Unable to map model to a target firmware version"
    }
    print(json.dumps(results))
    exit()

if len(target) > 1:
    for image in target:
        if image['license'] == lic:
            target_os = image['version']
            target_file = image['image']
            break
    else:
        results = {
        "success": False,
        "msg": "Unable to map model to a target firmware version"
        }
        print(json.dumps(results))
        exit()

else:
    target_os = target[0]['version']
    target_file = target[0]['image']

if target_os == args.version:
    results = {
        "success": True,
        "update_required": False,
        "msg": "Currently running target firmware version",
        "target_os": target_os,
        "target_file": target_file
    }
    print(json.dumps(results))
    exit()

results = {
    "success": True,
    "update_required": True,
    "msg": "Successfully mapped model to target firmware version",
    "target_os": target_os,
    "target_file": target_file
}
print(json.dumps(results))
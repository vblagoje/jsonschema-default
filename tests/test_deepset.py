import json
import re

import requests

import jsonschema_default as js

HAYSTACK_SCHEMA = "https://raw.githubusercontent.com/deepset-ai/haystack/master/haystack/" \
                  "json-schemas/haystack-pipeline-1.6.0.schema.json"


def camel2snake(name):
    return name[0].lower() + re.sub(r'(?!^)[A-Z]', lambda x: '_' + x.group(0).lower(), name[1:])


def scrub(obj, scrub_fn):
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if scrub_fn(obj[key]):
                del obj[key]
            else:
                scrub(obj[key], scrub_fn)


def test_all_component_creation():
    haystack_schema = requests.get(HAYSTACK_SCHEMA).json()

    for component in haystack_schema['definitions']:
        component_schema = haystack_schema['definitions'][component]
        # print(component_schema)
        obj = js.create_from(component_schema)
        override_dict = {"name": camel2snake(component),
                         "type": component}
        obj = {**obj, **override_dict}
        scrub(obj, scrub_fn=lambda x: x == "" or x == {} or x == [])
        print(json.dumps(obj))

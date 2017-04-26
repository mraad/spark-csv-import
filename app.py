#!/usr/bin/env python


import json

import os
import pystache
from pyjavaproperties import Properties


def read_json(json_filename):
    with open(json_filename) as app_json:
        return json.load(app_json)


def main():
    es2sql = {
        "string": "StringType",
        "float": "FloatType",
        "double": "DoubleType",
        "integer": "IntegerType",
        "int": "IntegerType",
        "date-iso": "DateType",
        "date": "DateType"
    }
    config = read_json("app.json")

    p = Properties()
    p.load(open("dmat.properties"))

    fields = []
    index = 0
    for field in p['fields'].split(';'):
        # print(field)
        tokens = field.split(',')
        if tokens[0] == 'geo':
            continue
        else:
            sql_type = es2sql[tokens[0]]
            fields.append({
                "name": tokens[1],
                "type": sql_type,
                "index": index,
                "delimiter": ","
            })
            index += 1

    fields[-1]["delimiter"] = ""
    config["fields"] = fields

    with open(os.path.join(os.path.dirname(__file__), "app.mustache")) as r:
        content = pystache.render(r.read(), config)
        with open("src/main/scala/com/esri/MainApp.scala", "wb") as w:
            w.write(content)


if __name__ == '__main__':
    main()

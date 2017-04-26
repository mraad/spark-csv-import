import json

import os
import pystache


def read_json(json_filename):
    with open(json_filename) as app_json:
        return json.load(app_json)


def main():
    es2sql = {
        "geo_point": "StringType",
        "string": "StringType",
        "float": "FloatType",
        "double": "DoubleType",
        "integer": "IntegerType",
        "date": "DateType"
    }
    config = read_json("app.json")

    fields = []
    dmat = read_json("dmat.json")
    properties = dmat["mappings"]["geo"]["properties"]
    index = 0
    for name, value in properties.iteritems():
        sql_type = es2sql[value["type"]]
        fields.append({
            "name": name,
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

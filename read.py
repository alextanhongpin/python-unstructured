from unstructured.staging.base import elements_from_json, convert_to_dict


elements = elements_from_json(filename="output.json")

elements = convert_to_dict(elements)
for element in elements:
    print(f"{element['type']}: {element['text']}")

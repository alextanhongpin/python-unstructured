from unstructured.partition.auto import partition
from unstructured.staging.base import elements_to_json
from time import perf_counter as pc

t0 = pc()


elements = partition(filename="./resume.pdf")
for element in elements:
    print(elements)
    print("\n")


elements_to_json(elements, filename="output.json")

print(pc() - t0)

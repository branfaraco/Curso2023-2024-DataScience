from rdflib import Graph
# g = Graph()
# try:
#     g.parse("./CareCenter.nt", format="nt")
#     print("El archivo es válido.")
# except Exception as e:
#     print(f"Error de validación: {e}")
from rdflib import Graph
file_path = "./DrinkingFountains.nt"
g = Graph()
line_number = 1  # Inicializa el número de línea
try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            g.parse(data=line, format="nt")
            line_number += 1
    print("El archivo es válido.")
except Exception as e:
    print(f"Error de validación en la línea {line_number}: {e}")
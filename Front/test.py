import xml.etree.ElementTree as ET
from xml.dom import minidom

# Crear el elemento raíz
raiz = ET.Element("Libros")

# Crear elementos secundarios
libro1 = ET.SubElement(raiz, "Libro")
titulo1 = ET.SubElement(libro1, "Titulo")
titulo1.text = "Python para Principiantes"
autor1 = ET.SubElement(libro1, "Autor")
autor1.text = "John Doe"

libro2 = ET.SubElement(raiz, "Libro")
titulo2 = ET.SubElement(libro2, "Titulo")
titulo2.text = "Programación Avanzada en Python"
autor2 = ET.SubElement(libro2, "Autor")
autor2.text = "Jane Smith"

# Crear el árbol XML
arbol = ET.ElementTree(raiz)

# Generar una cadena XML con formato
xml_con_formato = minidom.parseString(ET.tostring(raiz)).toprettyxml(indent="  ")

# Guardar el XML en un archivo
with open("libros_con_formato.xml", "w", encoding="utf-8") as archivo:
    archivo.write(xml_con_formato)

print("Archivo XML con formato creado.")

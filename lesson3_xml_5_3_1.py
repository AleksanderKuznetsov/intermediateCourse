"""
Выведите на консоль содержание каждого узла как первого,
так и второго уровня, включая название тега, список атрибутов и значение.
"""
import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()

for i in range(3, 5):
    print(root[i].tag)
    for z in range(len(root[i])):
        print(root[i][z].tag, root[i][z].get("name"), root[i][z].text)

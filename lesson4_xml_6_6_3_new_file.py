import xml.etree.ElementTree as ETree


def new_file():
    data = ETree.Element('data')
    itm_name = ETree.SubElement(data, 'name')
    itm_sex = ETree.SubElement(data, 'sex')
    itm_age = ETree.SubElement(data, 'age')
    itm_langs = ETree.SubElement(data, 'languages')
    itm_pc = ETree.SubElement(data, 'pc')
    itm_name.text = 'Petya'
    itm_sex.text = 'true'
    itm_age.text = '23'
    itm_l1 = ETree.SubElement(itm_langs, 'language')
    itm_l1.text = '9'
    itm_l1.set('name', 'Python')
    itm_l1 = ETree.SubElement(itm_langs, 'language')
    itm_l1.text = '7'
    itm_l1.set('name', 'Java')
    itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
    itm_pc1.text = 'Linux'
    itm_pc1.set('name', 'os')
    itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
    itm_pc1.text = 'ram'
    itm_pc1.set('name', '64')

    serialze = ETree.tostring(data, encoding='utf8', method='xml').decode()
    fil = open("demo2.xml", "w")
    fil.write(serialze)
    return


new_file()


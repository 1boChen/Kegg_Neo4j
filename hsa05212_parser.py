import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('kgml/hsa05212.xml')
root = tree.getroot()

id_list = []
name_list = []
starter_id = []
receiver_id = []
relation_type = []

blank_index = []
starter = []
receiver = []

for child in root:
    if child.attrib['type'] == 'gene':
        id_list.append(child.attrib['id'])

        names = child[0].attrib['name']
        comma_index = len(names)
        for i in range(len(names)):
            if names[i] == ',':
                comma_index = i
                break
        main_name = names[0 : comma_index]

        name_list.append(main_name)

    elif child.tag == 'relation':
        # from
        for j in range(len(id_list)):
            if child.attrib['entry1'] == id_list[j]:
                starter.append(name_list[j])
                # to
                for k in range(len(id_list)):
                    if child.attrib['entry2'] == id_list[k]:
                        receiver.append(name_list[k])

                        # relationship
                        relations = ''
                        if len(child) > 1:
                            for i in range(len(child)):
                                if i == 0:
                                    relations = child[0].attrib['name']
                                else:
                                    relations += ', ' + child[i].attrib['name']
                        else:
                            relations = child[0].attrib['name']
                        relation_type.append(relations)

                        break
                    if k == (len(id_list) - 1):
                        starter.pop()

                break

#gene_dict = {
#    'gene_id': id_list,
#    'gene_name': name_list
#}

#relation_dict = {
#    'starter_id': starter_id,
#    'receiver_id': receiver_id,
#    'relation_type': relation_type
#}

gene_relation_dict = {
    'from': starter,
    'to': receiver,
    'relationship': relation_type
}

gene_relation_df = pd.DataFrame(gene_relation_dict)
gene_relation_df.to_csv('kegg_pathway/hsa05212_pathway.csv', index = False)

#gene_df = pd.DataFrame(gene_dict)
#gene_df.to_csv('gene_name/hsa05210.csv', index = False)

#relation_df = pd.DataFrame(relation_dict)
#relation_df.to_csv('relation/hsa05210_relation.csv', index = False)
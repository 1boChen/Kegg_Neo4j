import os.path
import urllib.request
import xml.etree.ElementTree as ET

import pandas as pd
import glob


def get_pathway_list():
    webUrl = urllib.request.urlopen('http://rest.kegg.jp/list/pathway/hsa')
    data = webUrl.read().decode()
    pathway_list = []
    title_list = []
    for i in range(len(data)):
        if data[i] == ':':
            pathway_list.append(data[i + 1: i + 9])
            for j in range(i + 10, len(data)):
                if data[j] == '-':
                    title_list.append(data[i + 10: j - 1])
                    break
    return pathway_list, title_list


def get_hsa_entries():
    webUrl = urllib.request.urlopen('http://rest.kegg.jp/list/hsa')
    entry_data = webUrl.read().decode()
    return entry_data


def get_pathway(list):
    kgml_root = 'kgml/'
    destination_root = 'general_pathway/'
    for pathway in list:
        kgml_file = kgml_root + pathway + '.xml'
        tree = ET.parse(kgml_file)
        root = tree.getroot()

        tag_list = []
        for child in root:
            tag_list.append(child.tag)
        if tag_list.count('relation') < 1:
            continue
        id_list = []
        kegg_Names = []
        name_list = []
        link_list = []
        alias_list = []
        type_list = []

        relation_name = []
        relation_type = []
        starter = []
        starter_kegg_Names = []
        starter_link_list = []
        starter_alias_list = []
        starter_type_list = []
        receiver = []
        receiver_kegg_Names = []
        receiver_link_list = []
        receiver_alias_list = []
        receiver_type_list = []

        for child in root:
            if child.tag == 'entry':
                if 'name' in child.attrib and child.attrib['name'] == 'undefined':
                    continue
                else:
                    if 'id' in child.attrib:
                        id_list.append(child.attrib['id'])
                    else:
                        id_list.append('none')

                    if 'name' in child.attrib:
                        temp_name = child.attrib['name']
                        kegg_Names.append(temp_name)

                        try:
                            alias = get_compound(temp_name)
                            alias_list.append(alias)
                        except:
                            if 'name' in child[0].attrib:
                                names = child[0].attrib['name']
                                alias_list.append(names)
                            else:
                                alias_list.append('NA')
                    else:
                        kegg_Names.append('none')
                        alias_list.append('none')

                    if 'type' in child.attrib:
                        type_list.append(child.attrib['type'])
                    else:
                        type_list.append('none')

                    if 'link' in child.attrib:
                        link_list.append(child.attrib['link'])
                    else:
                        link_list.append('none')

                    if len(child) < 1:
                        name_list.append('none')
                    else:
                        if 'name' in child[0].attrib:
                            names = child[0].attrib['name']
                            comma_index = len(names)
                            for i in range(len(names)):
                                if names[i] == ',':
                                    comma_index = i
                                    break
                            main_name = names[0: comma_index]

                            name_list.append(main_name)
                        else:
                            name_list.append('none')

            elif child.tag == 'relation':
                # from
                for j in range(len(id_list)):
                    if child.attrib['entry1'] == id_list[j]:
                        starter.append(name_list[j])
                        starter_kegg_Names.append(kegg_Names[j])
                        starter_link_list.append(link_list[j])
                        starter_alias_list.append(alias_list[j])
                        starter_type_list.append(type_list[j])

                        # to
                        for k in range(len(id_list)):
                            if child.attrib['entry2'] == id_list[k]:
                                receiver.append(name_list[k])
                                receiver_kegg_Names.append(kegg_Names[k])
                                receiver_link_list.append(link_list[k])
                                receiver_alias_list.append(alias_list[k])
                                receiver_type_list.append(type_list[k])

                                # relationship
                                relations = ''
                                if len(child) >= 1:
                                    for i in range(len(child)):
                                        if i == 0:
                                            if 'name' in child[0].attrib:
                                                relations = child[0].attrib['name']
                                                relation_name.append(relations)
                                            else:
                                                relation_name.append('NA')
                                            if 'type' in child.attrib:
                                                relation_type_append(relation_type, child.attrib['type'])
                                            else:
                                                relation_type.append('NA')
                                        else:
                                            if 'name' in child[i].attrib:
                                                relations = child[i].attrib['name']
                                                relation_name.append(relations)
                                            else:
                                                relation_name.append('NA')
                                            if 'type' in child.attrib:
                                                relation_type_append(relation_type, child.attrib['type'])
                                            else:
                                                relation_type.append('NA')
                                            # relation_name.append(child[i].attrib['name'])
                                            # relation_type_append(relation_type, child[i].attrib['type'])
                                            starter.append(name_list[j])
                                            starter_kegg_Names.append(kegg_Names[j])
                                            starter_link_list.append(link_list[j])
                                            starter_alias_list.append(alias_list[j])
                                            starter_type_list.append(type_list[j])
                                            receiver.append(name_list[k])
                                            receiver_kegg_Names.append(kegg_Names[k])
                                            receiver_link_list.append(link_list[k])
                                            receiver_alias_list.append(alias_list[k])
                                            receiver_type_list.append(type_list[k])

                                else:
                                    starter.pop()
                                    starter_kegg_Names.pop()
                                    starter_link_list.pop()
                                    starter_alias_list.pop()
                                    starter_type_list.pop()
                                    receiver.pop()
                                    receiver_kegg_Names.pop()
                                    receiver_link_list.pop()
                                    receiver_alias_list.pop()
                                    receiver_type_list.pop()

                                break

                            if k == (len(id_list) - 1):
                                starter.pop()
                                starter_kegg_Names.pop()
                                starter_link_list.pop()
                                starter_alias_list.pop()
                                starter_type_list.pop()
                        break

        gene_relation_dict = {
            'starter': starter,
            'starter type': starter_type_list,
            'starter link': starter_link_list,
            'starter Kegg ID': starter_kegg_Names,
            'starter alias': starter_alias_list,
            'receiver': receiver,
            'receiver type': receiver_type_list,
            'receiver link': receiver_link_list,
            'receiver Kegg ID': receiver_kegg_Names,
            'receiver alias': receiver_alias_list,
            'relationship': relation_name,
            'relation type': relation_type
        }

        des_root = destination_root + pathway + '.csv'
        gene_relation_df = pd.DataFrame(gene_relation_dict)
        gene_relation_df.to_csv(des_root, index=False)


def get_compound(id):
    new_id = id.replace(' ', '+')
    root = 'http://rest.kegg.jp/list/'
    compound_root = root + new_id
    webUrl = urllib.request.urlopen(compound_root)
    data = webUrl.read().decode()

    return data
    # print(data)


# def starter_append_list(i, kegg_Names, name_list, link_list, alias_list, type_list):
# starter_kegg_Names.append(kegg_Names[i])
# starter_link_list = []
# starter_alias_list = []
# starter_type_list = []

def relation_type_append(relation_type, type):
    if type == 'ECrel':
        relation_type.append(type + ': enzyme-enzyme relation, indicating two enzymes catalyzing successive reaction '
                                    'steps')
    if type == 'maplink':
        relation_type.append(type + ': link to another map')
    if type == 'PPrel':
        relation_type.append(type + ': protein-protein interaction, such as binding and modification')
    if type == 'GErel':
        relation_type.append(type + ': gene expression interaction, indicating relation of transcription factor and '
                                    'target gene product')
    if type == 'PCrel':
        relation_type.append(type + ': protein-compound interaction')


def get_overall_pathway(pathway_list, title_list):
    csv_root = 'general_pathway/'
    starter = []
    starter_type_list = []
    starter_link_list = []
    starter_kegg_Names = []
    starter_alias_list = []
    receiver = []
    receiver_type_list = []
    receiver_link_list = []
    receiver_kegg_Names = []
    receiver_alias_list = []
    relation_name = []
    relation_type = []
    source = []
    length = len(pathway_list)
    for i in range(length):
        csv_file = csv_root + pathway_list[i] + '.csv'
        try:
            csv_data = pd.read_csv(csv_file)
            for a in range(len(csv_data['starter'])):
                starter.append(csv_data['starter'][a])
                starter_type_list.append(csv_data['starter type'][a])
                starter_link_list.append(csv_data['starter link'][a])
                starter_kegg_Names.append(csv_data['starter Kegg ID'][a])
                starter_alias_list.append(csv_data['starter alias'][a])
                receiver.append(csv_data['receiver'][a])
                receiver_type_list.append(csv_data['receiver type'][a])
                receiver_link_list.append(csv_data['receiver link'][a])
                receiver_kegg_Names.append(csv_data['receiver Kegg ID'][a])
                receiver_alias_list.append(csv_data['receiver alias'][a])
                relation_name.append(csv_data['relationship'][a])
                relation_type.append(csv_data['relation type'][a])
                source.append(pathway_list[i] + ' ' + title_list[i])
        except FileNotFoundError:
            print(pathway_list[i])
            continue
        finally:
            print(i / length)

    gene_relation_dict = {
        'starter': starter,
        'starter type': starter_type_list,
        'starter link': starter_link_list,
        'starter Kegg ID': starter_kegg_Names,
        'starter alias': starter_alias_list,
        'receiver': receiver,
        'receiver type': receiver_type_list,
        'receiver link': receiver_link_list,
        'receiver Kegg ID': receiver_kegg_Names,
        'receiver alias': receiver_alias_list,
        'relation name': relation_name,
        'relation type': relation_type,
        'source': source,
    }

    gene_relation_df = pd.DataFrame(gene_relation_dict)
    gene_relation_df.to_csv('pathway_v2_new.csv', index=False)


def check_entry_length():
    webUrl = urllib.request.urlopen('http://rest.kegg.jp/info/hsa')
    length = webUrl.read().decode()
    print(length)
    # print(len(lines))


def get_entry_dict():
    with open('entry_data.txt') as f:
        lines = f.readlines()

    hsa_ids = []
    names = []
    for line in lines:
        for i in range(5, len(line)):
            if 48 <= ord(line[i]) <= 57:
                continue
            else:
                hsa_id = line[: i]
                hsa_ids.append(hsa_id)
                name = line[i + 1:]
                names.append(name)
                break
    entry_dict = dict(zip(hsa_ids, names))

    return entry_dict
    # check
    # count = 0
    # for name in names:
    # if name[0].isdigit():
    # count += 1
    # print(name)
    # print(names.index(name))
    # print(count)


if __name__ == '__main__':
    pathway_list, title_list = get_pathway_list()

    get_overall_pathway(pathway_list, title_list)

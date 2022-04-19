import urllib.request
import wget
import xml.etree.ElementTree as ET
import pandas as pd

def get_pathway_list():
    webUrl = urllib.request.urlopen('http://rest.kegg.jp/list/pathway/hsa')
    data = webUrl.read().decode()
    pathway_list = []
    title_list = []
    for i in range(len(data)):
        if data[i] == ':' :
            pathway_list.append(data[i+1 : i + 9])
            for j in range(len(data)):
            title_list = []
    return pathway_list

def get_kgml(kgml_list):
    get_root = 'http://rest.kegg.jp/get/'
    download_dir = 'kgml/'
    for pathway in kgml_list:
        kgml_root = get_root + pathway + '/kgml'
        this_dir = download_dir + '/' + pathway + '.xml'
        wget.download(kgml_root, this_dir)

def get_pathway(list):
    kgml_root = 'kgml/'
    destination_root = 'pathway/'
    for pathway in list:
        kgml_file = kgml_root + pathway + '.xml'
        tree = ET.parse(kgml_file)
        root = tree.getroot()
        id_list = []
        name_list = []
        ailias_list = []
        relation_type = []
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
                main_name = names[0: comma_index]

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
                                    relation_type.append(relations)
                                elif len(child) != 1:
                                    starter.pop()
                                    receiver.pop()
                                else:
                                    relations = child[0].attrib['name']
                                    relation_type.append(relations)

                                break
                            if k == (len(id_list) - 1):
                                starter.pop()

                        break

        gene_relation_dict = {
            'from': starter,
            'to': receiver,
            'relationship': relation_type
        }

        des_root = destination_root + pathway + '.csv'
        gene_relation_df = pd.DataFrame(gene_relation_dict)
        gene_relation_df.to_csv(des_root, index=False)

def general_csv(list) :
    csv_root = 'pathway/'
    starter = []
    receiver = []
    relation = []
    source = []
    for pathway in list:
        csv_file = csv_root + pathway + '.csv'
        csv_data = pd.read_csv(csv_file)
        for i in range(len(csv_data['from'])):
            starter.append(csv_data['from'][i])
            receiver.append(csv_data['to'][i])
            relation.append(csv_data['relationship'][i])
            source.append(pathway)

    gene_relation_dict = {
        'from': starter,
        'to': receiver,
        'relationship': relation,
        'source': source
    }

    gene_relation_df = pd.DataFrame(gene_relation_dict)
    gene_relation_df.to_csv('general_pathway.csv', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = get_pathway_list()
    general_csv(data)
    #get_pathway(data)
    #get_kgml(data)


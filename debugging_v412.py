import urllib.request
import pandas as pd


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


def reformat_lines(data):
    for i in range(len(data['starter'])):
        reformat_line(data, i)

        if i % 1000 == 0:
            print(i / len(data['starter']))


def reformat_line(data, i):
    starter_Kegg_ID = data['starter Kegg ID'][i]
    starter_last_space_index = starter_Kegg_ID.find(' ')
    if starter_last_space_index != -1:
        temp_IDs = []
        s_index = 0
        for j in range(5, len(starter_Kegg_ID)):
            if starter_Kegg_ID[j] == ' ':
                if s_index == 0:
                    temp_IDs.append(starter_Kegg_ID[: j])
                else:
                    temp_IDs.append(starter_Kegg_ID[s_index + 1: j])
                s_index = j

                if ' ' in starter_Kegg_ID[j + 1:]:
                    continue
                else:
                    temp_IDs.append(starter_Kegg_ID[j + 1:])
                    break

        for id in temp_IDs:
            starter_append(id, data, i)
    else:
        starter_append(starter_Kegg_ID, data, i)


def reformat_receiver():
    for c in range(len(starter)):
        receiver_Kegg_ID = receiver_kegg_IDs[c]
        receiver_last_space_index = receiver_Kegg_ID.find(' ')

        # if receiver refers to multiple genes
        if receiver_last_space_index != -1:
            temp_IDs = []
            s_index = 0
            for j in range(5, len(receiver_Kegg_ID)):
                if receiver_Kegg_ID[j] == ' ':
                    if s_index == 0:
                        temp_IDs.append(receiver_Kegg_ID[: j])
                    else:
                        temp_IDs.append(receiver_Kegg_ID[s_index + 1: j])
                    s_index = j
                    if ' ' in receiver_Kegg_ID[j + 1:]:
                        continue
                    else:
                        temp_IDs.append(receiver_Kegg_ID[j + 1:])
                        break

            for id in temp_IDs:
                receiver_append(id, c)

            k_pop(c)

        else:
            continue


def get_compound(id):
    new_id = id.replace(' ', '+')
    root = 'http://rest.kegg.jp/list/'
    compound_root = root + new_id
    webUrl = urllib.request.urlopen(compound_root)
    data = webUrl.read().decode()

    if ' ' in data:
        for i in range(len(data)):
            if data[i] == ' ':
                return data[i + 1:]
    else:
        return data


def get_starter_alias(id, i):
    try:
        starter_alias = data['starter alias'][i]
        first_index = starter_alias.index(id)
        last_index = first_index + len(id)
        for j in range(last_index + 1, len(starter_alias)):
            if starter_alias[j] == ':':
                return starter_alias[last_index + 1 : j - 4]
        return starter_alias[last_index + 1 : ]
    except:
        print(id + 'not found in data')
        try:
            return entry_dict[id]
        except:
            print(id + 'not found in entry')
            try:
                return get_compound(id)
            except:
                print(id + 'not found in website')
                return 'no name found'
            return "no name found"
        return "no name found"


def get_first_name(alias):
    for i in range(len(alias)):
        if ',' in alias:
            if alias[i] == ',':
                return alias[: i]
        else:
            return alias

def get_receiver_alias(id, k):
    receiver_alias = receiver_alias_list[k]
    try:
        first_index = receiver_alias.index(id)
        last_index = first_index + len(id)
        for j in range(last_index + 1, len(receiver_alias)):
            if receiver_alias[j] == ':':
                return receiver_alias[last_index + 1: j - 4]
        return receiver_alias[last_index + 1:]
    except:
        print(id + 'not found in data')
        try:
            return entry_dict[id]
        except:
            print(id + 'not found in entry')
            try:
                return get_compound(id)
            except:
                print(id + 'no found in website')
                return 'no name found'
            return "no name found"
        return "no name found"

def get_link(id):
    return 'https://www.kegg.jp/dbget-bin/www_bget?' + id


def starter_append(id, data, i):
    alias = get_starter_alias(id, i)
    name = get_first_name(alias)
    link = get_link(id)

    starter.append(name)
    starter_kegg_IDs.append(id)
    starter_link_list.append(link)
    starter_alias_list.append(alias)
    starter_type_list.append(data['starter type'][i])

    receiver.append(data['receiver'][i])
    receiver_type_list.append(data['receiver type'][i])
    receiver_link_list.append(data['receiver link'][i])
    receiver_kegg_IDs.append(data['receiver Kegg ID'][i])
    receiver_alias_list.append(data['receiver alias'][i])

    relation_name.append(data['relation name'][i])
    relation_type.append(data['relation type'][i])
    source.append(data['source'][i])


def receiver_append(id, k):
    alias = get_receiver_alias(id, k)
    name = get_first_name(alias)
    link = get_link(id)

    receiver.append(name)
    receiver_kegg_IDs.append(id)
    receiver_link_list.append(link)
    receiver_alias_list.append(alias)
    receiver_type_list.append(receiver_type_list[k])

    starter.append(starter[k])
    starter_type_list.append(starter_type_list[k])
    starter_link_list.append(starter_link_list[k])
    starter_kegg_IDs.append(starter_kegg_IDs[k])
    starter_alias_list.append(starter_alias_list[k])

    relation_name.append(relation_name[k])
    relation_type.append(relation_type[k])
    source.append(source[k])


def k_pop(k):
    receiver.pop(k)
    receiver_kegg_IDs.pop(k)
    receiver_link_list.pop(k)
    receiver_alias_list.pop(k)
    receiver_type_list.pop(k)

    starter.pop(k)
    starter_type_list.pop(k)
    starter_link_list.pop(k)
    starter_kegg_IDs.pop(k)
    starter_alias_list.pop(k)

    relation_name.pop(k)
    relation_type.pop(k)
    source.pop(k)


def write_to_csv():
    gene_relation_dict = {
        'starter': starter,
        'starter type': starter_type_list,
        'starter link': starter_link_list,
        'starter Kegg ID': starter_kegg_IDs,
        'starter alias': starter_alias_list,
        'receiver': receiver,
        'receiver type': receiver_type_list,
        'receiver link': receiver_link_list,
        'receiver Kegg ID': receiver_kegg_IDs,
        'receiver alias': receiver_alias_list,
        'relation name': relation_name,
        'relation type': relation_type,
        'source': source
    }

    gene_relation_df = pd.DataFrame(gene_relation_dict)
    gene_relation_df.to_csv('pathway_v3_starter.csv', index=False)


def reformat_alias():
    for a in range(len(receiver_alias_list)):
        receiver_kegg_ID = receiver_kegg_IDs[a]
        if receiver_alias_list[a][3] == ':':
            receiver_alias_list[a] = receiver_alias_list[a][len(receiver_kegg_ID) + 1: ]


if __name__ == '__main__':
    starter = []
    starter_kegg_IDs = []
    starter_link_list = []
    starter_alias_list = []
    starter_type_list = []
    receiver = []
    receiver_kegg_IDs = []
    receiver_link_list = []
    receiver_alias_list = []
    receiver_type_list = []
    relation_name = []
    relation_type = []
    source = []

    entry_dict = get_entry_dict()
    data = pd.read_csv('pathway_v2_new.csv')
    reformat_lines(data)
    #reformat_receiver()
    #reformat_alias()
    write_to_csv()

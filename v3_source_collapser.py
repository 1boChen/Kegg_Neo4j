import pandas as pd


def source_collapse(data):
    for i in range(len(data['source'])):
        source = data['source'][i]
        temp_source = []

        if ',' in source:
            l_index = 0
            for j in range(5, len(source)):
                if source[j] == ',':
                    if l_index == 0:
                        temp_source.append(source[: j])
                    else:
                        temp_source.append(source[l_index + 2: j])
                    l_index = j + 1

                    if ',' in source[j + 1 : ]:
                        continue
                    else:
                        temp_source.append(source[j + 2 : ])
                        break

            new_source.append(remove_duplicate(temp_source))

        else:
            new_source.append(source)

    write_to_csv()

def remove_duplicate(temp_source):
    ac = []
    for i in range(len(temp_source)):
        ac.append(1)

    temp_temp_source = []
    temp_temp_source.append(temp_source[0])
    for i in range(len(temp_source) - 1):
        if temp_source[i].strip() == temp_source[i + 1].strip():
            temp_temp_source.append(temp_source[i + 1].strip())
            ac[i + 1] = ac[i] + 1
        else:
            temp_temp_source.append(temp_source[i + 1].strip())


    this_source = ''
    for i in range(len(temp_temp_source) - 1):
        if ac[i + 1] > ac[i]:
            continue
        else:
            this_source += temp_temp_source[i] + '(' + str(ac[i]) + '),\n'

    this_source += temp_temp_source[len(temp_temp_source) - 1] + '(' + str(ac[len(ac) - 1]) + ')'
    return this_source


def write_to_csv():
    gene_relation_dict = {
        'starter': data['starter'],
        'starter_type': data['starter_type'],
        'starter_link': data['starter_link'],
        'starter_Kegg_ID': data['starter_Kegg_ID'],
        'starter_alias': data['starter_alias'],
        'receiver': data['receiver'],
        'receiver_type': data['receiver_type'],
        'receiver_link': data['receiver_link'],
        'receiver_Kegg_ID': data['receiver_Kegg_ID'],
        'receiver_alias': data['receiver_alias'],
        'relation_name': data['relation_name'],
        'relation_type': data['relation_type'],
        'source': new_source,
        'credibility': data['credibility'],
        'singleton': data['singleton']
    }

    gene_relation_df = pd.DataFrame(gene_relation_dict)
    gene_relation_df.to_csv('pathway_v3_collapsed_v2.csv', index=False)


if __name__ == '__main__':
    data = pd.read_csv('pathway_v3_collapsed.csv')
    new_source = []
    source_collapse(data)
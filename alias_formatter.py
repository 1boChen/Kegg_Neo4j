import pandas as pd

def read_alias():
    for i in range(len(data['starter'])):
        if data['starter_Kegg_ID'][i] in kegg_id:
            continue
        else:
            starter_alias = data['starter_alias'][i]
            receiver_alias = data['receiver_alias'][i]
            temp_starter_alias = []
            temp_receiver_alias = []

            if ',' in starter_alias:
                ss_index = 0
                for j in range(len(starter_alias)):
                    if starter_alias[j] == ',' or starter_alias[j] == ';':
                        if ss_index == 0:
                            temp_starter_alias.append(starter_alias[: j])
                        else:
                            temp_starter_alias.append(starter_alias[ss_index + 1: j])
                        ss_index = j + 1

                        if ',' in starter_alias[j + 1:] or ';' in starter_alias[j + 1:]:
                            continue
                        else:
                            temp_starter_alias.append(starter_alias[j + 2:])
                            break

                for k in range(len(temp_starter_alias)):
                    if temp_starter_alias[k] == data['starter'][i]:
                        continue
                    else:
                        kegg_id.append(data['starter_Kegg_ID'][i])
                        gene.append(data['starter'][i])
                        alia.append(temp_starter_alias[k].strip())

        if data['receiver_Kegg_ID'][i] in kegg_id:
            continue
        else:
            if ',' in data['receiver_alias'][i]:
                rs_index = 0
                for a in range(len(receiver_alias)):
                    if receiver_alias[a] == ',' or receiver_alias[a] == ';':
                        if rs_index == 0:
                            temp_receiver_alias.append(receiver_alias[: a])
                        else:
                            temp_receiver_alias.append(receiver_alias[rs_index + 1: a])
                        rs_index = a + 1

                        if ',' in receiver_alias[a + 1:] or ';' in receiver_alias[a + 1:]:
                            continue
                        else:
                            temp_receiver_alias.append(receiver_alias[a + 2:])
                            break

                for b in range(len(temp_receiver_alias)):
                    if temp_receiver_alias[b] == data['receiver'][i]:
                        continue
                    else:
                        kegg_id.append(data['receiver_Kegg_ID'][i])
                        gene.append(data['receiver'][i])
                        alia.append(temp_receiver_alias[b].strip())


def wrtie_to_csv():
    alias_dict = {
        'gene': gene,
        'kegg_id': kegg_id,
        'alia': alia
    }

    alias_df = pd.DataFrame(alias_dict)
    alias_df.to_csv('alias.csv', index = False)


if __name__ == '__main__':
    data = pd.read_csv('pathway_v3_collapsed_v2.csv')

    kegg_id = []
    gene = []
    alia = []

    read_alias()
    wrtie_to_csv()
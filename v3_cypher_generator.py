import pandas as pd

def write_to_text():
    for i in range(30000, len(data['starter'])):
        starter_id = starter_Kegg_ID[i].replace(':', '')
        receiver_id = receiver_Kegg_ID[i].replace(':', '')
        new_g1_line = 'MERGE (' + starter_id + ' :' + starter_type[i] + ' {name: "' + starter[i] + '", type: "' + starter_type[i] + '", link: "' + starter_link[i] + '", KEGG_ID: "' + starter_Kegg_ID[i] + '", alias: "' + starter_alias[i].strip() + '"}) ' + '\n'
        new_g2_line = 'MERGE (' + receiver_id + ' :' + receiver_type[i] + ' {name: "' + receiver[i] + '", type: "' + receiver_type[i] + '", link: "' + receiver_link[i] + '", KEGG_ID: "' + receiver_Kegg_ID[i] + '", alias: "' + receiver_alias[i].strip() + '"}) ' + '\n'
        new_r_line = 'MERGE (' + starter_id + ')-[:' + relation_name[i] + ' {relation_name: "' + relation_name[i] + '", type: "' + relation_type[i] + '", credibility: "' + str(credibility[i]) + '", singleton: "' + str(singleton[i]) + '", source: "' + source[i] + '"}]->(' + receiver_id +');'
        new_line = new_g1_line + new_g2_line + new_r_line + '\n'
        lines.append(new_line)

        if i % 1000 == 0:
            print(i/len(starter))

    with open('load_v3_2.cypher', 'w') as f:
        for line in lines:
            f.write(line)


if __name__ == '__main__':
    data = pd.read_csv('pathway_v3_collapsed_v2_sc.csv')

    starter = data['starter']
    starter_type = data['starter_type']
    starter_link = data['starter_link']
    starter_Kegg_ID = data['starter_Kegg_ID']
    starter_alias = data['starter_alias']
    receiver = data['receiver']
    receiver_type = data['receiver_type']
    receiver_link = data['receiver_link']
    receiver_Kegg_ID = data['receiver_Kegg_ID']
    receiver_alias = data['receiver_alias']
    relation_name = data['realtion_name']
    relation_type = data['relation_type']
    source = data['source']
    credibility = data['credibility']
    singleton = data['singleton']

    lines = []

    write_to_text()
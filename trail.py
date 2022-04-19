import pandas as pd

if __name__ == '__main__':
    collapsed = pd.read_csv('pathway_v2_collapsed.csv')
    count = []
    for n in collapsed['count']:
        count.append(int(n) + 1)

    gene_relation_dict = {
        'starter': collapsed['starter'],
        'starter_type': collapsed['starter type'],
        'starter_link': collapsed['starter link'],
        'starter_Kegg ID': collapsed['starter Kegg ID'],
        'starter_alias': collapsed['starter alias'],
        'receiver': collapsed['receiver'],
        'receiver_type': collapsed['receiver type'],
        'receiver_link': collapsed['receiver link'],
        'receiver_Kegg_ID': collapsed['receiver Kegg ID'],
        'receiver_alias': collapsed['receiver alias'],
        'relation_name': collapsed['relation name'],
        'relation_type': collapsed['relation type'],
        'source': collapsed['source'],
        'credibility': count,
        'singleton': collapsed['singleton']
    }

    gene_relation_df = pd.DataFrame(gene_relation_dict)
    gene_relation_df.to_csv('pathway_v2_collapsed.csv', index=False)
    print(sum(count))

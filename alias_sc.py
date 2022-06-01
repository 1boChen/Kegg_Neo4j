import pandas as pd


def read_alias():
    for i in range(len(data['gene'])):
        temp_gene = data['gene'][i]

        for j in range(len(temp_gene)):
            if temp_gene[j] == ';':
                new_gene.append(temp_gene[:j])
                break
            if j == len(temp_gene) - 1:
                new_gene.append(temp_gene)


def wrtie_to_csv():
    alias_dict = {
        'gene': new_gene,
        'kegg_id': data['kegg_id'],
        'alia': data['alia']
    }

    alias_df = pd.DataFrame(alias_dict).dropna(how='any', axis=0)
    alias_df.to_csv('alias_v1.csv', index=False)


if __name__ == '__main__':
    data = pd.read_csv('alias.csv')

    new_gene = []

    read_alias()
    wrtie_to_csv()

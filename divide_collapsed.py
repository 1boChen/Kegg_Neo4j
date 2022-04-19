import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('pathway_v2_collapsed.csv')
    length = len(data['starter'])

    gene_name = []
    gene_link = []
    gene_Kegg_ID = []
    gene_alias = []

    compound_name = []
    compound_link = []
    compound_Kegg_ID = []
    compound_alias = []

    map_name = []
    map_link = []
    map_Kegg_ID = []
    map_alias = []

    #gene gene compound
    ggc_starter = []
    ggc_starter_type = []
    ggc_starter_link = []
    ggc_starter_Kegg_ID = []
    ggc_starter_alias = []
    ggc_receiver = []
    ggc_receiver_type = []
    ggc_receiver_link = []
    ggc_receiver_Kegg_ID = []
    ggc_receiver_alias = []
    ggc_relation_name = []
    ggc_relation_type = []
    ggc_relation_source = []
    ggc_credibility = []
    ggc_singleton = []

    #gene compound compound
    gcc_starter = []
    gcc_starter_type = []
    gcc_starter_link = []
    gcc_starter_Kegg_ID = []
    gcc_starter_alias = []
    gcc_receiver = []
    gcc_receiver_type = []
    gcc_receiver_link = []
    gcc_receiver_Kegg_ID = []
    gcc_receiver_alias = []
    gcc_relation_name = []
    gcc_relation_type = []
    gcc_relation_source = []
    gcc_credibility = []
    gcc_singleton = []

    #gene map compound
    gmc_starter = []
    gmc_starter_type = []
    gmc_starter_link = []
    gmc_starter_Kegg_ID = []
    gmc_starter_alias = []
    gmc_receiver = []
    gmc_receiver_type = []
    gmc_receiver_link = []
    gmc_receiver_Kegg_ID = []
    gmc_receiver_alias = []
    gmc_relation_name = []
    gmc_relation_type = []
    gmc_relation_source = []
    gmc_credibility = []
    gmc_singleton = []
    
    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound


    #gene gene compound

    #gene compound compound

    #gene map compound

    #compound gene compound

    #map gene compound

    for i in length:

        if data['starter_type'][i] == 'gene':
            gene_name.append(data['starter'][i])
            gene_link.append(data['starter_link'][i])
            gene_Kegg_ID.append(data['starter_Kegg_ID'][i])
            gene_alias.append(data['starter_alias'][i])

        if data['starter_type'][i] == 'compound':
            compound_name.append(data['starter'][i])
            compound_link.append(data['starter_link'][i])
            compound_Kegg_ID.append(data['starter_Kegg_ID'][i])
            compound_alias.append(data['starter_alias'][i])

        if data['starter_type'][i] == 'map':
            map_name.append(data['starter'][i])
            map_link.append(data['starter_link'][i])
            map_Kegg_ID.append(data['starter_Kegg_ID'][i])
            map_alias.append(data['starter_alias'][i])

        if data['receiver_type'][i] == 'gene':
            gene_name.append(data['receiver'][i])
            gene_link.append(data['receiver_link'][i])
            gene_Kegg_ID.append(data['receiver_Kegg_ID'][i])
            gene_alias.append(data['receiver_alias'][i])

        if data['receiver_type'][i] == 'compound':
            compound_name.append(data['receiver'][i])
            compound_link.append(data['receiver_link'][i])
            compound_Kegg_ID.append(data['receiver_Kegg_ID'][i])
            compound_alias.append(data['receiver_alias'][i])

        if data['receiver_type'][i] == 'map':
            map_name.append(data['receiver'][i])
            map_link.append(data['receiver_link'][i])
            map_Kegg_ID.append(data['receiver_Kegg_ID'][i])
            map_alias.append(data['receiver_alias'][i])
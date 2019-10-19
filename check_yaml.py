# import json
import yaml
import pprint

with open('cards.yaml', 'r') as f:
    # pprint.pprint(yaml.load(f))

    x = yaml.load(f)
    monster = x['card']['door']['monster']
    for i in monster:
        print(i['name'])

    pprint.pprint(x['card']['treasure']['equipment'])


# # import pandas as pd


# def convert_to_yaml(file_name, card_type, table_name):

#     yaml_file = 'cards.yaml'
#     header = f'--- # Project Eris Cards\n'
#     header += f'card:\n'
#     header += f'    {card_type}:\n'
#     header += f'        {table_name}:\n'
#     footer = '\n...'

#     body = 'test'
#     write_string = header + body + footer

#     with open(yaml_file, 'w') as f:
#         f.write(write_string)


# # if __name__ == '__main__':
# #     convert_to_yaml('test', 'door', 'monster')


# filename = 'ProjectEris - monsters.csv'

# df = pd.read_csv(filename)
# df_json = df.to_json()

# # with open('ping.json', 'w') as f:
# #     json.dump(df_json, f)

# # with open('cards.yaml', 'w') as f:
# # f.write(yaml.dump(df_json))

# with open('ping.json', 'r') as f:
#     pprint.pprint(json.load(f))

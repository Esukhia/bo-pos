import yaml

filepath = './rc/MGD-dict.yml'
# filepath = './tests/mgd.yml'

with open(filepath, mode='r', encoding='utf-8') as f:
    d = yaml.load(f)
    # print(len(d))
    # print(my_config_dict.values())

with open('./rc/mgd-lexicon.txt', 'w', encoding='utf-8') as f:
    for k, v in d.items():
        f.writelines("{} : {}\n".format(k, [*v]))

# yo = list(filter(lambda x:'རྒྱན་ཚིག' in d.get(x),d))

# print(yo)
# def myprint(dd):
#     for k, v in dd.items():
#         print(k)
#         if isinstance(v, dict):
#             myprint(v)
#     else:
#         # print("ya")
#         print("{0} : {1}".format(k, v))

# myprint(d)
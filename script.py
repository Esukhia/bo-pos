import yaml
import pickle

filepath = './tests/mgd.yml'

with open(filepath, mode='r', encoding='utf-8') as f:
    source_file = f.read()

def load_in_single_dict(nested_yaml):
    out = {}
    for entry in yaml.load_all(nested_yaml):
        for k in entry.keys():
            out[k] = entry[k]
    return out


total_dict = load_in_single_dict(source_file)
# print(yaml.dump(total_dict))

with open('dict.pickled', 'wb') as f:
    pickle.dump(total_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('dict.pickled', 'rb') as g:
    unpickled = pickle.load(g, encoding='UTF-8')
    print(unpickled)


# for entry, meanings in d.items():
#     for pos, acceptions in meanings.items():
#         for num, acception in acceptions.items():
#             print(acception['type'])
#             print(acceptions['definition'])





# import yaml

# filepath = './rc/mgd-full.yml'
# # filepath = './tests/mgd.yml'

# with open(filepath, mode='r', encoding='utf-8') as f:
#     d = yaml.load(f)
#     # print(len(d))

# with open('./rc/mgd-lexicon.txt', 'w', encoding='utf-8') as f:
#     for k, v in d.items():
#         f.writelines("{} : {}\n".format(k, [*v]))


# yo = list(filter(lambda x:'རྒྱན་ཚིག' in d.get(x),d))
# print(yo)



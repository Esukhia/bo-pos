import yaml
import pickle

source_file = """a:
    pos:
        1:
            def: བཀྲ་ཤིས་བདེ་ལེགས།
            ex: cccc
---
aa:
    pos:
        1:
            def: bbbbb
            ex: cccc
---
aaa:
    pos:
        1:
            def: bbbbb
            ex: cccc
"""


def load_in_single_dict(nested_yaml):
    out = {}
    for entry in yaml.load_all(nested_yaml):
        for k in entry.keys():
            out[k] = entry[k]
    return out


total_dict = load_in_single_dict(source_file)
print(yaml.dump(total_dict))

with open('dict.pickled', 'wb') as f:
    pickle.dump(total_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

with open('dict.pickled', 'rb') as g:
    unpickled = pickle.load(g, encoding='UTF-8')
    print(unpickled)


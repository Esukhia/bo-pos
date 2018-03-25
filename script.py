import os
import yaml
import pickle

# filepath = './tests/mgd.yml'
filepath = './rc/mgd-full.yml'

build = False

def load_in_single_dict(nested_yaml):
# yaml to python nested dicts
    out = {}
    for entry in yaml.load_all(nested_yaml):
        for k in entry.keys():
            out[k] = entry[k]
    return out


# only load and pickle if needed
if build or not os.path.isfile("dict.pickled"):
    with open(filepath, mode='r', encoding='utf-8') as f:
        source_file = f.read()
    full_dict = load_in_single_dict(source_file)
    # closes the file as soon as load() is executed (see https://stackoverflow.com/a/17985226/6027621)
    pickle.dump(full_dict, open("dict.pickled", "wb"), -1)

# unpickle
d = pickle.load(open("dict.pickled", "rb"))
print(len(d))

content = []
for entry, meanings in d.items():
    content.append(entry)

with open('entries.txt', mode='w') as f:
    f.write('\n'.join(content))

# for entry, meanings in d.items():
#     for pos, acceptions in meanings.items():
#         for num, acception in acceptions.items():
#             # print(acception)
#             print(acception.setdefault('definition', 'example'))


# yo = list(filter(lambda x:'རྒྱན་ཚིག' in d.get(x),d))
# print(yo)

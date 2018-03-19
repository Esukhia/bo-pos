# bo-pos
This repo contains various resources related to Tibetan part of speech.

## Resources
**ACTib-one-tag.txt** -- tokens from the [ACTIBII annotated corpus](https://zenodo.org/record/822537#.Wq6b35NuZ24) with the most frequent tag for each token. The corpus was [segmented](https://zenodo.org/record/823707#.Wq6ckJNuZ24) and tagged with the TiMBL Memory Based Tagger trained on the [SOAS corpus](https://zenodo.org/record/574878#.Wq6c7ZNuZ24) (1,463,920 types) 

**SOAS-lexicon.txt** -- [tokens from the SOAS corpus](https://zenodo.org/record/574876#.Wq6eDZNuZ24) with multiple tags per token. (15,643 types)

**SOAS-one-tag.txt** -- [tokens from the SOAS corpus](https://zenodo.org/record/574876#.Wq6eDZNuZ24) with the most frequent tag for each token. (14,983 types)

**MGD-dict.yml** -- [Monlam Grand Dictionary](http://monlamit.com/node/156) data normalized and re-organized into a structured .yml file. (107,064 types)

## To Do - prep
* convert mgd POS to UD with attributes
    * find POS attributes in mgd definitions
    * extract tokens with less than 5 syllables
    * extract POS + attributes when available
    * convert mgd pos to UD
    * give priority to tags from ACTib-one-tag when available
* revise the mapping of SOAS to UD

## To Do - Segmentation
* convert segmentation and vocabularies to XYZ
* train a RDR model
* convert model into pybo matcher syntax

## To Do - Tagging
* plug pybo to spacy with the init file
* train spacy models
* ...

## To Do - Suggestions
* train a 3-gram model on mgd
* plug to pybo
* plug bopho to pybo
* ...



import json


with open("data/mobile_raw_data.txt") as f, open("data/train_file_new.json", "w") as f2:
    train_set = {}
    train_set["rasa_nlu_data"] = {}
    train_set["rasa_nlu_data"]["common_examples"] = []
    train_set["rasa_nlu_data"]["regex_features"] = []
    train_set["rasa_nlu_data"]["entity_synonyms"] = []
    dict_set = []
    entitiys_name = []
    for line in f:
        if line.strip() == "":
            continue
        elif "text" in line:
            entitiys_name = []
            cols = line.strip().split(",")
            for name in cols[2:]:
                entitiys_name.append(name)
            continue
        tokens = line.strip().split("|")
        common_example = {}
        common_example["text"] = tokens[0]
        common_example["intent"] = tokens[1]
        common_example["entities"] = []
        if len(tokens) < 3:
            train_set["rasa_nlu_data"]["common_examples"].append(common_example)
            continue
        entitiys = tokens[2].split("，")
        for i, e in enumerate(entitiys):
            try:
                start = tokens[0].index(e)
                end = tokens[0].index(e) + len(e)
                entity = {}
                entity["start"] = start
                entity["end"] = end
                entity["value"] = e
                entity["entity"] = entitiys_name[i]
                common_example["entities"].append(entity)
                dict_set.append(e)
                # print start, end,  tokens[0][start:end]
            except:
                # print line
                pass

        train_set["rasa_nlu_data"]["common_examples"].append(common_example)
    # print(train_set)
    f2.write(json.dumps(train_set, ensure_ascii=False, indent=2))
    dict_set = set(dict_set)
    for e in dict_set:
        print(e)

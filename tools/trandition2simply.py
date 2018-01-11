import io
from glob import glob

from tools.langconv import Converter

file_list = sorted(glob("../data/tchinese/*.yml"))
save_path = "../data/chinese_dialogs/"
if __name__=="__main__":

    converter = Converter('zh-hans')
    for file in file_list:
        with io.open(save_path + file.split("/")[3], "w") as f_w:
            with io.open(file) as f:
                for line in f:
                    simplified_sentence = converter.convert(line)
                    print(simplified_sentence,)
                    f_w.write(simplified_sentence)


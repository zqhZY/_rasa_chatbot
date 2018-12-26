# note:
This project now is updated, some rasa new features will be added soon.(项目已跟进到rasa新版本，一些新特性后面尝试后补充。)

# rasa_chatbot
A Chinese task oriented chatbot in  IVR(Interactive Voice Response) domain， Implement by rasa nlu and rasa core. This is a demo with toy dataset.

### install dependency:

#### python3
install or update to python 3

#### install rasa_core, this will install rasa nlu too, and now support chinese.
```
pip install rasa_core==0.9.0
```
this command will install rasa nlu too.

#### install sklearn and MITIE

```
pip install -U scikit-learn sklearn-crfsuite
pip install git+https://github.com/mit-nlp/MITIE.git
```

### dir tree
```
_rasa_chatbot/
├── bot.py
├── chat_detection
├── data
│   ├── mobile_nlu_data.json # train data json format
│   ├── mobile_raw_data.txt # train data raw
│   ├── mobile_story.md # toy dialogue train data 
│   └── total_word_feature_extractor.dat # pretrained mitie word vector
├── httpserver.py # rasa nlu httpserver
├── __init__.py
├── INSTALL.md
├── ivr_chatbot.yml # rasa nlu config file
├── mobile_domain.yml # rasa core config file
├── projects # pretrained models
│   ├── dialogue
│   └── ivr_nlu
├── README.md
├── tools # tools of data process
└── train.sh # train script of rasa nlu

```

### train nlu model
```bash
sh train.sh
```
命令运行耗时较长，模型训练完毕生成：
```
projects/
└── ivr_nlu
    └── demo
        ├── entity_extractor.dat
        ├── entity_synonyms.json
        ├── intent_classifier_sklearn.pkl
        ├── metadata.json
        └── training_data.json

```
### test rasa nlu
```
$ python httpserver.py
$ curl -X POST localhost:1235/parse -d '{"q":"我的流量还剩多少"}' | python -m json.tool
{
    'q': '我的流量还剩多少', 
    'intent': 'request_search', 
    'entities': {
        'item': '流量'
    }
}

```

### train dialogue
```bash
python bot.py train-dialogue
```
模型训练完毕生成：

```
projects
├── dialogue
│   ├── domain.json
│   ├── domain.yml
│   ├── policy_0_MemoizationPolicy
│   │   ├── featurizer.json
│   │   └── memorized_turns.json
│   ├── policy_1_KerasPolicy
│   │   ├── featurizer.json
│   │   ├── keras_arch.json
│   │   ├── keras_policy.json
│   │   └── keras_weights.h5
│   ├── policy_metadata.json
│   └── stories.md
└── ivr_nlu
```

### train dialogue in online mode
```
python bot.py online_train
```

### test
Run command below:
```bash
python bot.py run
```
Example1:
```
Bot loaded. Type a message and press enter : 
YOU：你是谁
BOT：您好!，我是机器人小热，很高兴为您服务。
YOU：我想看一下消费情况
BOT：您想查询哪个月的消费？
YOU：十月份的
BOT：好，请稍等
BOT：您好，您十月份共消费二十八元。
YOU：好谢谢
BOT：您开心我就开心
BOT：您还想干什么
YOU：没什么了
BOT：Bye， 下次再见

```
Example2:
```
Bot loaded. Type a message and press enter : 
YOU：给我看看我上月用了多少话费
BOT：好，请稍等
BOT：您好，您上月共消费二十八元。
BOT：您还想干什么

```

### train word vector

You can train your own MITIE model using following method:
```
$ git clone https://github.com/mit-nlp/MITIE.git
$ cd MITIE/tools/wordrep
$ mkdir build
$ cd build
$ cmake ..
$ cmake --build . --config Release
$ ./wordrep -e /path/to/your/folder_of_cutted_text_files
```
/path/to/your/folder_of_cutted_text_files above is a directory path in which has word cutted data files to train. This process may cost one or two days.

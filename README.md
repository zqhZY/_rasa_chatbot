# note:
This project is too old to run directly and will be updated soon.(由于rasa版本更新比较大，该项目比较老，以至于无法直接运行，稍后根据最新api调试后更新。)

# rasa_chatbot
A Chinese task oriented chatbot in  IVR(Interactive Voice Response) domain， Implement by rasa nlu and rasa core. This is a demo with toy dataset.

### install dependency:
- [follow here](https://github.com/zqhZY/rasa_chatbot/blob/master/INSTALL.md)

### dir tree
```
rasa_chatbot/
├── data
│   ├── mobile_nlu_data.json  # rasa nlu train data
│   ├── mobile_story.md       # rasa core train data
│   └── total_word_feature_extractor.dat  # mitie word vector feature
├── __init__.py               # init file
├── httpserver.py             # rasa nlu httpserver
├── bot.py                    # ivr bot main script.
├── mobile_domain.yml         # rasa core domain file
├── mobile_nlu_model_config.json  # rasa nlu config file
├── models                    # directory to save trained models
└── README.md                 # readme file

```

### train nlu model
```bash
python -m rasa_nlu.train --config  mobile_nlu_model_config.json --data data/mobile_nlu_data.json  --path models
```
### test rasa nlu
```
$python -m rasa_nlu.server --path projects
$ curl -X POST localhost:5000/parse -d '{"q":"hello"}' | python -m json.tool
{
    "intent": {
        "name": "greet",
        "confidence": 1.0
    },
    "entities": [],
    "text": "hello",
    "project": "default",
    "model": "fallback"
}

```

### train dialogue
```bash
python bot.py train-dialogue
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

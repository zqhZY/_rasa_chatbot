# Code of this project has been deleted, because it will be used for product. Welcome to disscuss or get the start code in Email if you are interested.

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
python bot.py train-nlu
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

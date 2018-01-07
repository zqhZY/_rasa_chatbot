# rasa_chatbot
A Chinese task oriented chatbot in  IVR(Interactive Voice Response) domain(电信ivr领域， 中文)， Implement by rasa nlu and rasa core. This is a demo with toy dataset.

### requirements:
- python3
- [rasa_nlu_chi](https://github.com/crownpku/rasa_nlu_chi)
- [rasa_core](https://github.com/RasaHQ/rasa_core)
- stklearn
- mitie [(you can install follow here)](https://nlu.rasa.ai/installation.html#section-backends)

### train nlu model
```bash
python bot.py train-nlu
```

### train dialogue
```bash
python bot.py train-dialogue
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

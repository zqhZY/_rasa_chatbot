import json


from klein import Klein
# from rasa_nlu.config import RasaNLUConfig


class ItemStore(object):
    app = Klein()

    def __init__(self, ivr_model, chat_detection_model, ivr_config, chat_detection_config, enable_chat_detection):
        from rasa_nlu.model import Interpreter
        self.interpreter = Interpreter.load(ivr_model)
        self.enable_chat_detection = enable_chat_detection
        if enable_chat_detection:
            self.chat_detection = Interpreter.load(chat_detection_model)
        self._items = {}

    @app.route('/')
    def items(self, request):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(self._items)

    @app.route('/parse', methods=['POST'])
    def save_item(self, request):
        data_string = request.content.read().decode('utf-8', 'strict')
        request.setHeader('Content-Type', 'application/json')
        data = json.loads(data_string)
        print(data)
        request.setResponseCode(200)

        """
            check if input is task or non_task first
        """
        if self.enable_chat_detection:
            chat_detection_pred = self.chat_detection.parse(data["text"])
            print("chat_detection_pred--->{}".format(chat_detection_pred))
            intent = chat_detection_pred.get("intent").get("name")
            if intent == "non_task":
                data["intent"] = intent
                data["entities"] = {}
                return json.dumps(data, ensure_ascii=False)

        """
            if text is mobile ivr domain, pred using ivr model
        """
        pred = self.interpreter.parse(data["q"])

        print(pred)
        #reg_res = pred.get("regulation_result")
        data["intent"] = pred.get("intent").get("name")
        #if reg_res != None:
        #    data["intent"] = reg_res

        entities = pred.get("entities")
        entities_res = {}
        for entitie in entities:
            name = entitie.get("entity")
            value = entitie.get("value")
            if name == "item":
                if "消费" in value or "话费" in value:
                    value = "消费"
                elif "余额" in value:
                    value = "余额"
                elif "流量" in value:
                    value = "流量"
                elif "宽带" in value:
                    value = "宽带"
            entities_res.setdefault(name, value)
        data["entities"] = entities_res

        print(data)
        return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    ivr_model = "projects/ivr_nlu/demo"
    chat_detection_model = "models/ivr/demo_chat_detection"
    ivr_config = "ivr_chatbot.yml"
    chat_detection_config = "chat_detection/mobile_chat_detection_model_config.json"
    store = ItemStore(ivr_model, chat_detection_model, ivr_config, chat_detection_config, enable_chat_detection=False)
    store.app.run('127.0.0.1', 1235)

import json


from klein import Klein
from rasa_nlu.config import RasaNLUConfig


class ItemStore(object):
    app = Klein()

    def __init__(self, model_dir):
        from rasa_nlu.model import Metadata, Interpreter
        self.interpreter = Interpreter.load(model_dir, RasaNLUConfig("mobile_nlu_model_config.json"))
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

        pred = self.interpreter.parse(data["text"])
        data["intent"] = pred.get("intent").get("name")

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
    model_dir = "models/ivr/demo"
    store = ItemStore(model_dir)
    store.app.run('127.0.0.1', 1235)

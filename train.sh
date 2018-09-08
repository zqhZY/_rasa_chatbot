#!/usr/bin/env bash
python -m rasa_nlu.train --data ./data/mobile_nlu_data.json \
    --config ivr_chatbot.yml \
    --path projects \
    --fixed_model_name demo \
    --project ivr_nlu

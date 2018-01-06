## story_0
* greet
 - utter_greet
* request_search{"item": "消费", "time": "九月"}
 - action_search_consume
 - utter_ask_morehelp
* thanks
 - utter_thanks
 - utter_ask_morehelp
* deny
 - utter_goodbye

## story_1
* greet
 - utter_greet
* request_search
 - action_search_consume
* request_search{"item": "消费"}
 - action_search_consume
* inform_time
 - action_search_consume
* thanks
 - utter_thanks
 - utter_ask_morehelp
* deny
 - utter_goodbye

## story_2
* greet
 - utter_greet
* request_search{"item": "消费"}
 - action_search_consume
* inform_time
 - action_search_consume
* thanks
 - utter_thanks
 - utter_ask_morehelp
* deny
 - utter_goodbye
 
## story_3
* request_search{"item": "消费"}
 - action_search_consume
* inform_time
 - action_search_consume
* thanks
 - utter_thanks
 - utter_ask_morehelp
* deny
 - utter_goodbye
 
## story_4
* greet
 - utter_greet
* request_search{"item": "消费"}
 - action_search_consume
* inform_time
 - action_search_consume
* thanks
 - utter_thanks
 - utter_ask_morehelp
* deny
 - utter_goodbye
* request_search{"item": "消费"}
 - action_search_consume
* inform_time
 - action_search_consume

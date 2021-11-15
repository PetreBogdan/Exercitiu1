from json_methods import *
import json


if __name__ == '__main__':

    with open('demo_response_capic.json', 'r') as json_file:
        json_dict = json.load(json_file)

    instante = read_from_json(json_dict)
    # show_instances_by_health(instante)
    # print(display_nr_instances(json_dict))
    # show_instances_by_lastMod(instante)


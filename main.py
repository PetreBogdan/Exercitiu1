from json_methods import read_from_json
import json


if __name__ == '__main__':

    with open('demo_response_capic.json', 'r') as json_file:
        json_dict = json.load(json_file)

    instante = read_from_json(json_dict)

    for index, i in enumerate(instante):
        print(f"hcloudCtx number {index+1}")
        i.display_info()
        i.health.display_health()
        print()

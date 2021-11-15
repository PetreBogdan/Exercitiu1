from json_methods import *
import json
import argparse


parser = argparse.ArgumentParser(description="Displays instances from a json file")
parser.add_argument('Path', type=str, metavar='Path',
                    help='Path of the specified json file')
group = parser.add_mutually_exclusive_group()
group.add_argument('-H', '--health', action='store_true',
                   help='Displays instances from json file ordered by health')
group.add_argument('-d', '--date', action='store_true',
                   help='Displays instances from json file ordered by last modified')
args = parser.parse_args()

if __name__ == '__main__':

    with open(args.Path, 'r') as json_file:
        json_dict = json.load(json_file)

    instante = read_from_json(json_dict)
    if args.health:
        show_instances_by_health(instante)
    elif args.date:
        show_instances_by_lastMod(instante)
    else:
        show_instances(instante)

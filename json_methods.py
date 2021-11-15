from cloudctx import ClassCtx
from datetime import datetime


data_dict = {'name': 'name', 'tenantName': 'tenant_name',
             'description': 'description', 'nameAlias': 'name_alias',
             'ctxProfileName': 'ctx_profile_name', 'modTs': 'modTs'}

health_dict = {'cur': 'cur', 'maxSev': 'maxSev'}


def check_for_empty(string):
    """
    Checks if the var is empty
    :param string: the variable
    :return: the variable if not empty else "-"
    """

    if string == "":
        return "-"
    else:
        return string


def read_from_json(json_dict):
    """
    Reads data from json file
    :param json_dict: dictionary containing json data
    :return: a list with all hcloud instances
    """

    lista_instante = []
    nr_ctx = len(json_dict['imdata'])
    for element in range(nr_ctx):
        atributes = json_dict['imdata'][element]['hcloudCtx']['attributes']
        for key in data_dict.keys():
            if key not in atributes.keys():
                raise Exception(f'Missing attribute: {key}')
            else:
                if key == 'modTs':
                    data_dict[key] = format_date(atributes[key])
                else:
                    data_dict[key] = check_for_empty(atributes[key])
        try:
            atributes_health = json_dict['imdata'][element]['hcloudCtx']['children'][0]['healthInst']['attributes']
            for key in health_dict.keys():
                if key not in atributes_health.keys():
                    raise Exception(f"Missing attribute: {key}")
                else:
                    health_dict[key] = check_for_empty(atributes_health[key])
        except IndexError:
            health_dict['cur'] = "0"
            health_dict['maxSev'] = "Missing healthInst"

        mo = ClassCtx(data_dict['name'], data_dict['tenantName'], data_dict['description'],
                      data_dict['nameAlias'], data_dict['ctxProfileName'], data_dict['modTs'],
                      int(health_dict['cur']), health_dict['maxSev'])
        lista_instante.append(mo)
    return lista_instante


def show_instances_by_health(instante):
    """
    Shows information about hcloud instances ordered by health
    :param instante: a list with all instances
    :return: displays the information about each instance ordered by health
    """

    instante = sorted(instante, key=lambda x: x.health.current_health)
    for index, i in enumerate(instante):
        print(f"hcloudCtx number {index+1}")
        i.display_info()
        i.health.display_health()
        print()


def display_nr_instances(json_dict):
    """
    Returns the number of hcloud instances in json
    :param json_dict: the json dictionary
    :return: integer containing the length
    """

    return f"The number of instances in json file is {len(json_dict['imdata'])}"


def format_date(string):
    """
    Formatting the string in modTs attribute in hcloud instance
    :param string: string containing time
    :return: nice formatted datetime object
    """

    dateobj = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f%z')
    dateobj = dateobj.strftime('%d-%m-%Y %I:%M:%S %p')
    return dateobj


def show_instances_by_lastmod(instante):
    """
    Shows information about hcloud instances ordered by last modified
    :param instante: list containing all instances
    :return: displays the information about each instance ordered by date and time modified
    """
    instante = sorted(instante, key=lambda x: datetime.strptime(x.mod_ts, '%d-%m-%Y %I:%M:%S %p'), reverse=True)
    for index, i in enumerate(instante):
        print(f"hcloudCtx number {index + 1}")
        i.display_info()
        i.health.display_health()
        print()


def show_instances(instante):
    """
    Shows information about hcloud instances unordered
    :param instante: list containing all instances
    :return: displays the information about each instance unordered
    """
    for index, i in enumerate(instante):
        print(f"hcloudCtx number {index + 1}")
        i.display_info()
        i.health.display_health()
        print()

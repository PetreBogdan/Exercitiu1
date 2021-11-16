from cloudctx import ClassCtx
from datetime import datetime


data_dict = {'name': 'name', 'tenantName': 'tenant_name',
             'description': 'description', 'nameAlias': 'name_alias',
             'ctxProfileName': 'ctx_profile_name', 'modTs': 'modTs'}

health_dict = {'cur': 'cur', 'maxSev': 'maxSev'}


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
            data_dict[key] = ClassCtx.check_for_empty(atributes[key])
        try:
            atributes_health = json_dict['imdata'][element]['hcloudCtx']['children'][0]['healthInst']['attributes']
        except IndexError:
            health_dict['cur'] = "0"
            health_dict['maxSev'] = "Missing healthInst"
        else:
            for key in health_dict.keys():
                health_dict[key] = ClassCtx.check_for_empty(atributes_health[key])

        mo = ClassCtx(data_dict,health_dict)

        lista_instante.append(mo)
    return lista_instante


def displays_instances_by_health(instante):
    """
    Shows information about hcloud instances ordered by health
    :param instante: a list with all instances
    :return: displays the information about each instance ordered by health
    """

    instante = sorted(instante, key=lambda x: x.health.current_health)
    displays_instances(instante)


def displays_instances_by_lastmod(instante):
    """
    Shows information about hcloud instances ordered by last modified
    :param instante: list containing all instances
    :return: displays the information about each instance ordered by date and time modified
    """
    instante = sorted(instante, key=lambda x: datetime.strptime(x.mod_ts, '%d-%m-%Y %I:%M:%S %p'), reverse=True)
    displays_instances(instante)


def displays_instances(instante):
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

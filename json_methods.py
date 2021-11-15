from cloudctx import ClassCtx


data_dict = {'name': 'name', 'tenantName': 'tenant_name',
             'description': 'description', 'nameAlias': 'name_alias',
             'ctxProfileName': 'ctx_profile_name'}

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
                data_dict[key] = check_for_empty(atributes[key])

        atributes_health = json_dict['imdata'][element]['hcloudCtx']['children'][0]['healthInst']['attributes']
        for key in health_dict.keys():
            if key not in atributes_health.keys():
                raise Exception(f"Missing attribute: {key}")
            else:
                health_dict[key] = check_for_empty(atributes_health[key])

        mo = ClassCtx(data_dict['name'], data_dict['tenantName'], data_dict['description'],
                      data_dict['nameAlias'], data_dict['ctxProfileName'],
                      int(health_dict['cur']), health_dict['maxSev'])
        lista_instante.append(mo)
    return lista_instante

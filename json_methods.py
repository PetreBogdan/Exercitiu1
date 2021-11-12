from cloudctx import ClassCtx


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
        for i in atributes.keys():
            if i == 'name':
                name = check_for_empty(atributes[i])
            elif i == 'tenantName':
                tenant_name = check_for_empty(atributes[i])
            elif i == 'description':
                description = check_for_empty(atributes[i])
            elif i == 'nameAlias':
                name_alias = check_for_empty(atributes[i])
            elif i == 'ctxProfileName':
                ctx_profile_name = check_for_empty(atributes[i])

        atributes_health = json_dict['imdata'][element]['hcloudCtx']['children'][0]['healthInst']['attributes']
        for i in atributes_health.keys():
            if i == 'cur':
                current_health = int(atributes_health[i])
            elif i == 'maxSev':
                max_sev = atributes_health[i]

        mo = ClassCtx(name, tenant_name, description,
                      name_alias, ctx_profile_name,
                      current_health, max_sev)
        lista_instante.append(mo)
    return lista_instante

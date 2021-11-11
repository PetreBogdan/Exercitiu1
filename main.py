import json
from cloudctx import ClassCtx

with open('demo_response_capic.json', 'r') as json_file:
    json_dict = json.load(json_file)


def check_for_empty(string):
    if string == "":
        return "-"
    else:
        return string


if __name__ == '__main__':

    atributes = json_dict['imdata'][0]['hcloudCtx']['attributes']
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

    atributes_health = json_dict['imdata'][0]['hcloudCtx']['children'][0]['healthInst']['attributes']
    for i in atributes_health.keys():
        if i == 'cur':
            current_health = int(atributes_health[i])
        elif i == 'maxSev':
            max_sev = atributes_health[i]

    MO = ClassCtx(name, tenant_name, description,
                  name_alias, ctx_profile_name,
                  current_health, max_sev)

    MO.display_info()
    MO.health.display_health()

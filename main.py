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

    MO = ClassCtx(name, tenant_name, description,
                  name_alias, ctx_profile_name)
    MO.display_info()

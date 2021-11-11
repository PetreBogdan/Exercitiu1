import json
from cloudctx import ClassCtx

with open('demo_response_capic.json','r') as json_file:
    json_dict = json.load(json_file)

# print(json_dict)


if __name__=='__main__':

    # for i in json_dict.keys():
    #     if i == 'imdata':
    #         hcloud_data = json_dict['imdata'][0]
    #         # print(hcloud_data['hcloudCtx'])

    atributes = json_dict['imdata'][0]['hcloudCtx']['attributes']
    for i in atributes.keys():
        if i == 'name':
            if atributes[i] == "":
                name = '-'
            else:
                name = atributes[i]
        elif i == 'tenantName':
            if atributes[i] == "":
                tenant_name = '-'
            else:
                tenant_name = atributes[i]
        elif i == 'description':
            if atributes[i] == "":
                description = '-'
            else:
                description = atributes[i]
        elif i == 'nameAlias':
            if atributes[i] == "":
                name_alias = '-'
            else:
                name_alias = atributes[i]
        elif i == 'ctxProfileName':
            if atributes[i] == "":
                ctx_profile_name = '-'
            else:
                ctx_profile_name = atributes[i]


    MO = ClassCtx(name,tenant_name,description,name_alias,ctx_profile_name)
    MO.display_info()

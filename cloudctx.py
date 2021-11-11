class ClassCtx():

    def __init__(self,name,tenant_name,description,
                 name_alias, ctx_profile_name):
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name

    def display_info(self):
        print(self.name)
        print(self.tenant_name)
        print(self.description)
        print(self.name_alias)
        print(self.ctx_profile_name)


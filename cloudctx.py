from healthinst import HealthInst


class ClassCtx:

    def __init__(self, name, tenant_name, description,
                 name_alias, ctx_profile_name,
                 current_health, max_sev):
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name
        self.health = HealthInst(current_health, max_sev)

    def display_info(self):
        print("Name: ", self.name)
        print("Tenant Name: ", self.tenant_name)
        print("Description: ", self.description)
        print("Name Alias: ", self.name_alias)
        print("Ctx Profile Name: ", self.ctx_profile_name)

from healthinst import HealthInst


class ClassCtx:

    def __init__(self, name, tenant_name, description,
                 name_alias, ctx_profile_name, mod_ts,
                 current_health, max_sev):
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name
        self.mod_ts = mod_ts
        self.health = HealthInst(current_health, max_sev)

    def display_info(self):
        print(f"Name: {self.name} \n"
              f"Tenant Name: {self.tenant_name}\n"
              f"Description: {self.description}\n"
              f"Name Alias: {self.name_alias}\n"
              f"Ctx Profile Name: {self.ctx_profile_name}\n"
              f"Last Modified: {self.mod_ts}\n"
              f"Current Health: {self.health.current_health}\n"
              f"Max Sev: {self.health.max_sev}")

from healthinst import HealthInst
import textwrap
from datetime import datetime


class ClassCtx:

    cloud_obj = 0

    def __init__(self, data_dict, health_dict):
        self.name = data_dict['name']
        self.tenant_name = data_dict['tenantName']
        self.description = data_dict['description']
        self.name_alias = data_dict['nameAlias']
        self.ctx_profile_name = data_dict['ctxProfileName']
        self.mod_ts = data_dict['modTs']
        self.health = HealthInst(health_dict)
        ClassCtx.cloud_obj += 1

    def display_info(self):

        print(textwrap.dedent(f"""\
            Name: {self.name} 
            Tenant Name: {self.tenant_name} 
            Description: {self.description} 
            Name Alias: {self.name_alias} 
            Ctx Profile Name: {self.ctx_profile_name} 
            Last Modified: {self.mod_ts} 
            Current Health: {self.health.current_health} 
            Max Sev: {self.health.max_sev}"""))

    @property
    def mod_ts(self):
        return self._mod_ts

    @mod_ts.setter
    def mod_ts(self, string):
        dateobj = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f%z')
        dateobj = dateobj.strftime('%d-%m-%Y %I:%M:%S %p')
        self._mod_ts = dateobj

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, string):
        self._name = ClassCtx.check_for_empty(string)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, string):
        self._description = ClassCtx.check_for_empty(string)

    @property
    def tenant_name(self):
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, string):
        self._tenant_name = ClassCtx.check_for_empty(string)

    @property
    def name_alias(self):
        return self._name_alias

    @name_alias.setter
    def name_alias(self, string):
        self._name_alias = ClassCtx.check_for_empty(string)

    @property
    def ctx_profile_name(self):
        return self._ctx_profile_name

    @ctx_profile_name.setter
    def ctx_profile_name(self, string):
        self._ctx_profile_name = ClassCtx.check_for_empty(string)

    @staticmethod
    def check_for_empty(string):
        if string == "":
            return "-"
        else:
            return string

    @classmethod
    def returns_nr_instances(cls):
        return f"Number of cloudCtx instances created are: {cls.cloud_obj}"

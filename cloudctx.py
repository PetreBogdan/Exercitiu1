from healthinst import HealthInst
import textwrap
from datetime import datetime


class ClassCtx:

    cloud_obj = 0

    def __init__(self, dict, health_dict):
        self.name = dict['name']
        self.tenant_name = dict['tenantName']
        self.description = dict['description']
        self.name_alias = dict['nameAlias']
        self.ctx_profile_name = dict['ctxProfileName']
        self.mod_ts = dict['modTs']
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

    @staticmethod
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

    @staticmethod
    def returns_nr_instances():
        return f"Number of cloudCtx instances created are: {ClassCtx.cloud_obj}"

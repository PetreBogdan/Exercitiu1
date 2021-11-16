from healthinst import HealthInst
import textwrap
from datetime import datetime


class ClassCtx:

    cloud_obj = 0

    def __init__(self, name, tenant_name, description,
                 name_alias, ctx_profile_name, mod_ts,
                 current_health, max_sev):
        self.name = name
        self.tenant_name = tenant_name
        self.description = description
        self.name_alias = name_alias
        self.ctx_profile_name = ctx_profile_name
        self.mod_ts = ClassCtx.format_date(mod_ts)
        self.health = HealthInst(current_health, max_sev)
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

    @staticmethod
    def format_date(string):
        """
        Formatting the string in modTs attribute in hcloud instance
        :param string: string containing time
        :return: nice formatted datetime object
        """
        dateobj = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f%z')
        dateobj = dateobj.strftime('%d-%m-%Y %I:%M:%S %p')
        return dateobj

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

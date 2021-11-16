class HealthInst:

    def __init__(self, health_dict):
        self.current_health = int(health_dict['cur'])
        self.max_sev = health_dict['maxSev']

    def display_health(self):
        if self.current_health < 100:
            print("Unhealthy")
        else:
            print("Healthy")

class HealthInst:

    def __init__(self, current_health, max_sev):
        self.current_health = current_health
        self.max_sev = max_sev

    def display_health(self):
        if self.current_health < 100:
            print("Unhealthy")
        else:
            print("Healthy")

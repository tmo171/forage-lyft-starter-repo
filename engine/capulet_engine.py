class CapuletEngine(Engine):

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) > 5000
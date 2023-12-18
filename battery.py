class Battery(Serviceable):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self):
        pass
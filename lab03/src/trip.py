class Trip:

    def __init__(self, destination, duration):
        self.participants = []
        self.destination = destination
        self.duration = duration

    def calculate_cost(self):
        return 100 * self.duration

    def add_participant(self, param):
        if param == "":
            raise ValueError("Participant name cannot be empty")

        self.participants.append(param)




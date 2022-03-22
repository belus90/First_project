class Member:

    def __init__(self, first_name, last_name,  email_address, date_of_birth, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.date_of_birth = date_of_birth
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

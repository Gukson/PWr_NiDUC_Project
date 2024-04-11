class Pack:
    def __init__(self, name, postal_code, city):
        self.name = name
        self.postal_code = postal_code
        self.city = city

    def get_post_code(self):
        return self.postal_code


class Role:
    def __init__(self, data):
        self.id = data["roles_id"]
        self.name = data["name"]
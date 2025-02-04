class BackendDeveloper:
    def develop(self):
        return "Writing backend code..."

class FrontendDeveloper:
    def develop(self):
        return "Writing frontend code..."

class Project:
    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()

    def develop(self):
        return f"{self.backend.develop()} {self.frontend.develop()}"


class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass  # Sparrow can fly

class Penguin(Bird):
    def fly(self):
        raise Exception("I cannot fly!")  # ❌ Violates LSP


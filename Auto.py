class Auto:
    def __init__(self, sor):
        self.tipus = sor[0]
        self.datum = int(sor[1])

    def __str__(self):
        return f"{self.tipus}, {self.datum}"

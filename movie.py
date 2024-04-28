class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

        self.verbose = False

    def __str__(self):
        return f"{self.title} ({self.year})
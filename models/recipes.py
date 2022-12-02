class Recipe:
    def __init__(self, name, cooking_time, description, instructions, diet, image, id = None):
        self.name = name
        self.cooking_time = cooking_time
        self.description = description
        self.instructions = instructions
        self.diet = diet
        self.image = image
        self.id = id

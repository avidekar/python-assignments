from collections import deque

class Veterinarian:

    def __init__(self):
        self.pet_queue = deque()

    def accept(self, petName):
        self.pet_queue.append(petName)

    def heal(self):
        return self.pet_queue.popleft()

if __name__ == "__main__":
    veterinarian = Veterinarian()
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal())
    print(veterinarian.heal())
class Save:
    def __init__(self):
        self.characterName = ""
        # TODO: Search a way to handle time operations for the time played counter
        self.timePlayed = [0, 0, 0]

    def load_file(self, data: dict):
        self.characterName = data["character_name"]
        self.timePlayed = data["time_played"]

    def save_file(self):
        print(self.__dict__)


class SaveManager:
    slots = [1, 2, 3]

    def saludos_peludos(self):
        self.slots[0] = 4
        self.slots[1] = 5
        self.slots[2] = 6
        self.slots = [1,5,8]


    def get_slot(self, slot: int):
        return self.slots[slot - 1]

    def update(self):
        self.slots[0] += 1


if __name__ == '__main__':
    saveManager1 = SaveManager()
    saveManager2 = SaveManager()

    # saveManager1.init()
    # saveManager1.update()

    saveManager1.saludos_peludos()

    # saveManager1.update()
    # saveManager1.update()
    # saveManager1.update()

    print(saveManager2.slots[0])

class Player:

    job = 'Pemain Bola'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    @staticmethod
    def retiredIn(age):
        return 40-age
    
    @classmethod
    def generalInfo(cls):
        return cls.job + ' akan pensiun dalam 40 tahun.'

    @property
    def infoPlayer(self):
        return self.name +' berumur ' + self.age
    
    @infoPlayer.setter
    def infoPlayer(self, data):
        name, age = data.split(', ')
        self.name = name
        self.age = age
    
# print('Pensiun dalam', Player.retiredIn(25), 'tahun')
# print(Player.generalInfo())
player = Player('Fikky', '17')
player.infoPlayer = 'Fikky Ardianto, 20 tahun'  

print(player.infoPlayer)
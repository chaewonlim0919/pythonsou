class ElecProduct:
    volume = 0

    def volumeControl(self, volume):
        self.volume = volume
        # print('볼륨을 조절한다.')
        pass

class ELecTv(ElecProduct):
    def volumeControl(self, volume):
        self.volume = volume
        print(f'ELecTv 볼륨을 조절한다 : {volume}')

class ElecRadio(ElecProduct):
    def volumeControl(self, volume):
        sori = volume
        print(f'ElecRadio 소리를 조절한다: {sori}')

print('\n다형성 ---')
sub1 = ELecTv()
sub2 = ElecRadio()
elec = ElecProduct()
elec = sub1
elec.volumeControl(5)
print()
elec = sub2
elec.volumeControl(5)  



class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = '개'
    def move(self):
        print('강아지는 귀여워')

class Cat(Animal):
    name = '고양이'
    def move(self):
        pass

class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        pass
    def foxMethod(self):
        pass

wolf = Wolf()
wolf.move()


print()
animal = [Dog(), Cat(), Wolf(), Fox()]
for a in animal:
    a.move()
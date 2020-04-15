from Person import Person

class Pasien(Person):

    def __init__(self, nama, alamat, jenisKelamin, noTelp, noKK, noKtp):
        self.__nama = nama
        self.__alamat = alamat
        self.__jenisKelamin = jenisKelamin
        self.__noTelp = noTelp
        self.__noKK = noKK
        self.__noKtp = noKtp
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama):
        self.__nama = nama
        
    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, alamat):
        self.__alamat = alamat
    
    @property
    def jenisKelamin(self):
        return self.__jenisKelamin

    @jenisKelamin.setter
    def jenisKelamin(self, jenisKelamin):
        self.__jenisKelamin = jenisKelamin

    @property
    def noTelp(self):
        return self.__noTelp
    
    @noTelp.setter
    def noTelp(self, noTelp):
        self.__noTelp = noTelp

    @property
    def noKK(self):
        return self.__noKK

    @noKK.setter
    def noKK(self, noKK):
        self.__noKK = noKK
    
    @property
    def noKtp(self):
        return self.__noKtp

    @noKtp.setter
    def noKtp(self, noKtp):
        self.__noKtp = noKtp
    
    def cetakKartu(self):
        return self.nama

# p = Pasien("nama","alamat","laki","08123123","12312313","123123123")
# print(p.nama)


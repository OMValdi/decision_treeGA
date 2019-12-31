import random
import pandas 
import numpy

data_latih = pandas.read_csv('data_latih.csv')
data_test  = pandas.read_csv('data_test.txt')




gen_size = 15


list_data_latih = data_latih.values.tolist()
new_data_latih = []
for data_train in list_data_latih:
    temp =[]
    for index in range(0, len(data_train)):
        if index == 0:
            if "Rendah" in data_train[index]:
                temp.append('100')
            elif "Normal" in data_train[index]:
                temp.append('010')
            elif "Tinggi" in data_train[index]:
                    temp.append('001')
        elif index == 1 :
            if "Pagi" in data_train[index]:
                temp.append('1000')
            elif "Siang" in data_train[index]:
                temp.append('0100')
            elif "Sore" in data_train[index]:
                temp.append('0010')
            elif "Malam" in data_train[index]:
                temp.append('0001')
        elif index == 2 :
            if "Hujan" in data_train[index]:
                temp.append('1000')
            elif "Rintik" in data_train[index]:
                temp.append('0100')
            elif "Berawan" in data_train[index]:
                temp.append('0010')
            elif "Cerah" in data_train[index]:
                temp.append('0001')
        elif index == 3 :
            if "Rendah" in data_train[index]:
                temp.append('100')
            elif "Normal" in data_train[index]:
                temp.append('010')
            elif "Tinggi" in data_train[index]:
                temp.append('001')
        elif index == 4 :
            if "Ya" in data_train[index]:
                temp.append('1')
            elif "Tidak" in data_train[index]:
                temp.append('0')
    new_data_latih.append(temp)
nilai_data_latih = []
for idx in new_data_latih:
    nilai_data_latih.append("".join(idx))
#print(nilai_data_latih) 
     
list_data_test = data_test.values.tolist()
new_data_test = []
for data in list_data_test:
    temp =[]
    for index in range(0, len(data)):
        if index == 0:
            if "Rendah" in data[index]:
                temp.append('100')
            elif "Normal" in data[index]:
                temp.append('010')
            elif "Tinggi" in data[index]:
                    temp.append('001')
        elif index == 1 :
            if "Pagi" in data[index]:
                temp.append('1000')
            elif "Siang" in data[index]:
                temp.append('0100')
            elif "Sore" in data[index]:
                temp.append('0010')
            elif "Malam" in data[index]:
                temp.append('0001')
        elif index == 2 :
            if "Hujan" in data[index]:
                temp.append('1000')
            elif "Rintik" in data[index]:
                temp.append('0100')
            elif "Berawan" in data[index]:
                temp.append('0010')
            elif "Cerah" in data[index]:
                temp.append('0001')
        elif index == 3 :
            if "Rendah" in data[index]:
                temp.append('100')
            elif "Normal" in data[index]:
                temp.append('010')
            elif "Tinggi" in data[index]:
                temp.append('001')
       
    new_data_test.append(temp)
nilai_data_test = []
for idx in new_data_test:
    nilai_data_test.append("".join(idx))
#print(nilai_data_test) 

class models(object):
    kromosom = []
    aturan = []
    prediksi = []
    fitness = None
    def __init__(self, gen):
        self.kromosom = gen
        self.inisialisasi()

    def inisialisasi(self):
        aturan = []
        for i  in range(0, int(len(self.kromosom)/gen_size)):
            temp = []
            for j in range(i*15, 15*(i+1)):
                temp.append(self.kromosom[j])
            aturan.append(temp)
        self.aturan = aturan

#modelss = models(list("101010101010101101010101010101101010101010101"))
#print(modelss.aturan)
    def prediksi_list(self, data_string):
       
        list_prediksi = []
        for aturan in self.aturan :
            temp = []
            for data in data_string :
                tmp = []
                for index_dt in range(0,len(data)-1) :
                    if data[index_dt] == '1' :
                        if aturan[index_dt] == '1':
                            tmp.append(True)
                        else:
                            tmp.append(False)
                if False in tmp:
                    if aturan[-1] == '1':
                        temp.append(False)
                    else :
                        temp.append(True)
                else:
                    if aturan[-1] == '1' :
                        temp.append(True)
                    else:
                        temp.append(False)

            
            list_prediksi.append(temp)
        prediksi_aturan = []
        for y in range(0, len(list_prediksi[0])) :
            temp_list = []
            for x in range(0, len(list_prediksi)) :
                #print(type(list_prediksi[x][y]))
                temp_list.append(list_prediksi[x][y])
            #print(temp_list)
            prediksi_aturan.append(temp_list)
        list_fin = []
        for prediksi in prediksi_aturan:
            if True in prediksi :
                list_fin.append(True)
            else:
                list_fin.append(False)
        return list_fin
#modelss = models(list("111111111111111000111111111111"))
#print((modelss.prediksi_list(nilai_data_latih)))
#print((modelss.prediksi_list(nilai_data_test)))

    def hitung_fitness(self, data_string):

        self.prediksi = self.prediksi_list(data_string)
        temp = []
        for index in range(0, len(data_string)) :
            if data_string[index][-1] == '1' :
                if self.prediksi[index] == True:
                    temp.append(True)
                else:
                    temp.append(False)
            else:
                if self.prediksi[index] == False:
                    temp.append(True)
                else: 
                    temp.append(False)
        self.fitness = temp.count(True) / len(data_string)
#modelss = models(list("111111111111111"))
#modelss.hitung_fitness(nilai_data_latih)
#print(modelss.fitness)
    
class populasi(object):
    list_individu = []
    ukuran_populasi = None
    kelipatan =[1, 2, 3]
    
    

    def __init__(self, ukuran_populasi):
        self.ukuran_populasi = ukuran_populasi
        for hitung in range(0, ukuran_populasi):
            gen = random.choice(self.kelipatan)
            temp = []
            for i in range(0, gen*gen_size):
                temp.append(random.choice(['0', '1']))
            
            self.list_individu.append(models(temp))
            
        print('Populasi : ',self.list_individu.__len__())
    def aturan_string(self) :
        temp = ''
        for i in self.list_individu[0].aturan :
            temp = temp + ''.join(i)
        return temp

    def akurasi_pop(self, data_string):
        for acc in self.list_individu :
            acc.hitung_fitness(data_string)

    def parent_selection(self):
              
        parent_select = []
        for id in range(0, int((self.ukuran_populasi)* 0.25)):            
            parent_select.append(self.list_individu[id]) 
        return parent_select

    def sorting(self):
        list_sorting = []
        while self.list_individu != [] :
            idx = 0 
            for i in range(0, len(self.list_individu)):
                if i == 0 :
                    idx = 0
                else : 
                    if self.list_individu[idx].fitness < self.list_individu[i].fitness :
                        idx = i
            list_sorting.append(self.list_individu.pop(idx))
        self.list_individu = list_sorting

       
    def mutasi(self, list_gen):
        
        temp = []
        for gen in list_gen:
            tmp = gen[:]
            for idx in range(0, len(tmp)):
                 angka = random.randint(0, self.ukuran_populasi)
                 if angka == 0:
                     if tmp[idx] == '0' :
                         tmp[idx] = '1'
                     else : 
                        tmp[idx] = '0'
            temp.append(tmp)
        return temp
    
    def list_gen(self,gen_list):
        temp = []
        for gen in gen_list :
            temp.append(models(gen))
            
        return temp



    
    def crossover(self, data_string):
        ortu_terpilih = self.parent_selection()
        if len(ortu_terpilih)%2 == 1 :
            ortu_terpilih = ortu_terpilih[:-1]
        list_child = []
        j = 0
        i = 0
        while i < int(len(ortu_terpilih)* 0.5):
            j += 1
            gen_ortu= []
            gen_ortu.append(ortu_terpilih[i].kromosom)
            gen_ortu.append(ortu_terpilih[i+1].kromosom)
            i += 2
            if len(gen_ortu[0])< len(gen_ortu[1]):
                gen_terkecil = 0
                hitung_terkecil = len(gen_ortu[0])
            else :
                gen_terkecil = 1
                hitung_terkecil = len(gen_ortu[1])

            angka_random = []
            angka_random.append(random.randint(0, hitung_terkecil))
            nilai = random.randint(0, hitung_terkecil)
            while nilai == angka_random[0]:
                nilai = random.randint(0, hitung_terkecil)
            angka_random.append(nilai)

            anak_1 = gen_ortu[0][0:angka_random[0]]+gen_ortu[1][angka_random[0]:angka_random[1]]+gen_ortu[0][angka_random[1]:]
            anak_2 = gen_ortu[1][0:angka_random[0]]+gen_ortu[0][angka_random[0]:angka_random[1]]+gen_ortu[1][angka_random[1]:]
            list_child.append(anak_1)
            list_child.append(anak_2)
        bermutasi = self.mutasi(list_child)
        for idx in range(0, len(bermutasi)):
            if type(len(bermutasi[idx])/ gen_size) == type(0.1):
                 jumlah_1 = int(len(bermutasi[idx])/ gen_size)
                 jumlah_2 = jumlah_1 + 1 
                 if(len(bermutasi[idx]) - (jumlah_1*gen_size) <((jumlah_2*gen_size)) - len(bermutasi[idx])):
                    bermutasi[idx] = bermutasi[idx][:jumlah_1*gen_size]
                 else :
                     gen = []
                     for i in range(0, (jumlah_2*gen_size)- len(bermutasi[idx])):
                         gen.append(random.choice(['0','1'])) 
                     bermutasi[idx] = bermutasi[idx] + gen
        hasil_gen = self.list_gen(bermutasi)
        self.list_individu = self.list_individu + hasil_gen
        self.akurasi_pop(data_string)
        self.sorting()
        self.list_individu = self.list_individu[:self.ukuran_populasi]
                
    def print_gen(self, data_string, akurasi):
        self.akurasi_pop(data_string)
        dapat_akurasi = True
        while dapat_akurasi :
            
            self.crossover(data_string)
            if akurasi < self.list_individu[0].fitness :
                dapat_akurasi = False

if __name__ == '__main__':
    
    pop = populasi(16)
    pop.akurasi_pop(nilai_data_latih)
    pop.sorting()
    print('Akurasi Awal : ',pop.list_individu[0].fitness)
    akurasi = 0.75
    pop.print_gen(nilai_data_latih,akurasi)

    print('Gen Terbaik : ', pop.aturan_string())
    #print('Akurasi Terbaik :',pop.list_individu[0].fitness)
    test_prediksi = pop.list_individu[0].prediksi_list(nilai_data_test)
    

    with open('hasil.txt', 'w+') as f :
        for idx in test_prediksi :
            hasil = str(int(idx)) + '\n'
            f.write(hasil)



        
            

                    
        




       





    
        

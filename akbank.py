import heapq

metro_hatti = {
    'AŞTİ':{'Kızılay': 5},
    'Kızılay':{'AŞTİ': 5,'Ulus': 3,'Sıhhiye':2},
    'Sıhhiye':{'Kızılay': 2,'Ulus': 2},
    'Ulus':{'Sıhhiye': 2,'Kızılay': 3,'Kurtuluş': 4},
    'Kurtuluş':{'Ulus': 4,'Dikimevi': 3},
    'Dikimevi':{'Kurtuluş': 3}
}

def en_kisa_mesafe(metro_hatti, baslangic, hedef):
    mesafeler = {durak: float('inf') for durak in metro_hatti}
    mesafeler[baslangic] = 0
    oncelik_kuyrugu = [(0, baslangic)]
    onceki_durak = {}
    
    while oncelik_kuyrugu:
        mevcut_mesafe, mevcut_durak = heapq.heappop(oncelik_kuyrugu)
        
        if mevcut_durak == hedef
           rota = []
           while mevcut_durak in onceki_durak:
               rota.append(mevcut_durak)
               mevcut_durak = onceki_durak[mevcut_durak]
           rota.append(baslangic)
           return rota[::-1], mesafeler[hedef]
        
        for komsu, mesafe in metro_hatti[mevcut_durak].items():
            yeni_mesafe = mevcut_mesafe + mesafe
            if yeni_mesafe < mesafeler[komsu]:
                mesafeler[komsu] = yeni_mesafe
                heapq.heappush(oncelik_kuyrugu, (yeni_mesafe, komsu))
                onceki_durak[komsu] = mevcut_durak
                
        return None, float('inf')
    
    if_name_ == ''_main_'':
        baslangic_durak = input(''Baslangıç durağını girin:'')
        hedef_durak = input(''Hedef durağını girin:'')
        
        if baslangic_durak in metro_hatti and hedef_durak in metro_hatti:
            rota, toplam_mesafe = en_kisa_mesafe(metro_hatti, baslangic_durak, hedef_durak)
            if rota:
                print(f''En kısa rota:{rota}, Toplam Mesafe: {toplam_mesafe} dakika'')
                else:
                    print:(''Gidilecek rota bulunamadı:'')
                else:
                    print:(''Hatalı giriş! Lütfen geçerli durak isimleri girin.'')
# Metro Rota Hesaplayıcı

Bu proje, verilen bir metro hattı haritasındaki iki durak arasındaki en kısa rotayı ve toplam seyahat süresini hesaplar.

## Açıklama

Bu Python uygulaması, Dijkstra algoritmasını kullanarak, kullanıcının girdiği başlangıç ve hedef durakları arasındaki en kısa rotayı bulur. Metro hatları ve duraklar arasındaki mesafeler, bir Python sözlüğü (dictionary) yapısında saklanır.

## Kullanılan Teknolojiler ve Kütüphaneler

*Python 3.x
*heapq (Python'ın standart kütüphanesi)

## Algoritma Çalışma Mantığı

Bu proje, metro hatları arasındaki en kısa mesafeyi bulmak için Dijkstra algoritması, başlangıç noktasından diğer tüm noktalara olan en kısa yolları bulmak için kullanılan bir graf teorisi algoritmasıdır.

## BFS Algoritmasının Nasıl Çalıştığı

Bu projede kullanılan Dijkstra algoritması genişlik öncelikli arama (BFS) algoritmasının varyasyonudur. BFS, bir graf içinde bir başlangıç noktasından diğer tüm noktalara olan en kısa yolları bulmak için kullanılan bir arama algoritmasıdır. BFS, grafı katman katman dolaşarak en kısa yolları bulur.

## A* Algoritmasının Nasıl Çalıştığı

A\* algoritması, Dijkstra algoritmasına benzer şekilde, bir graf içinde başka bir başlangıç noktasından diğer tüm noktalara olan en kısa yolları bulmak için kullanılan bir arama algoritmasıdır. A\* algoritması, Dijkstra algoritmasından farklı olarak, hedef noktaya olan uzaklığı tahmin eden bir sezgisel (heuristic) fonksiyon kullanır. Bu sayede, A\* algoritması, Dijkstra algoritmasına göre daha hızlı bir şekilde en kısa yolu bulabilir. Bu projede A\* algoritması kullanımamaktadır, ancak gelecekte geliştirmelerde eklenebilir.

## Neden Bu Algoritmaları Kullandık?

Dijkstra algoritması, metro hatları arasındaki en kısa mesafeyi bulmak için en uygun algoritmalardan biridir. Dijkstra algoritması, her zaman en kısa yolu bulmayı garanti eder ve verimli bir şekilde çalışır.

## Örnek Kullanım ve Test Sonuçları


Başlangıç durağını girin: AŞTİ
Hedef durağını girin: Dikimevi
En kısa rota: ['AŞTİ','Kızılay','Ulus','Kurtuluş','Dikimevi'], Toplam Mesafe: 14 dakika

## Projeyi Geliştirme Fikirleri

*A\* algoritmasını ekleyerek performansı artırmak.
*Farklı metro hatları ve durakları için destek eklemek.
*Kullanıcı arayüzü (GUI) veya web arayüzü ekleyerek kullanımı kolaylaştırmak.
*Gerçek zamanlı metro verilerini kullanarak dinamik rota hesaplama özelliği eklemek.
*Alternatif ulaşım yöntemlerini 8otobüs, tramvay vb.) de hesaba katarak çok modlu rota planlama özelliği eklemek.

## Gereksinimler

*Python 3.x
*heapq kütüphanesi( Python'ın standart kütüphanesinde yer alır, ek kurulum gerektirmez.)

## Kurulum

Proje için herhangi bir ek kurulum gerektirmemektedir. Sadece Python 3'ün bilgisayarınızda yüklü olması yeterlidir.

## Katkıda Bulunma

Katkılarınız memnuniyetle karşılanır! Hata düzeltmeleri, yeni özellikler veya iyileştirmeler için çekinmeyin. GitHub üzerinden ''pull request'' göndererek katkıda bulunabilirsiniz.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## İletişim

Proje ile ilgili sorularınız veya geri bildirimleriniz için tugce.kkrks@gmail.com ile iletişime geçebilirsiniz.


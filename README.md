# Opydoviz-Kurları

opydoviz-kurlari, T.C. Merkez Bankası ve çeşitli döviz kuru yayıncılarının API sistemleri kullanılarak, anlık kur bilgilerinin bu sistemler üzerinden alınabilmesini ve geliştiriciye çeşitli formatlarda sunabilmesini sağlayan, açık kaynak kodlu Python3 kütüphanesidir.


## Kurulum / Kullanım
opydoviz-kurlari kullanım detayları ve kurulumu için Wiki sayfasını incelemelisiniz. Size en iyi bilgiyi Wiki sunar!


## 1.x Özellikler
1.x sürümü T.C. Merkez Bankası API ve Truncgil API baz alınarak yayınlanmıştır.

T.C. Merkez Bankası tarafından yayınlanan döviz kurlarının tamamını çıktı olarak verebilmekle birlikte, Truncgil API sayesinde altın kurlarını da görüntülemenize imkan sağlar.

Çeşitli özellikler listelenmiştir.
* Tüm Python3 sürümlerini destekler.
* Kur çıktıları için  3 farklı format destekler. (clear, text, json)
* Türkiye Cumhuriyeti Merkez Bankası ve Truncgil v3 API destekler.
* opy-logger ile geliştirildi ve opy-logger özelliklerini kullanmanıza imkan verir, çıktılar için loglama yapılabilir.
* Şu an yalnızca Türkçe dil seçeneği ile geliştirilmiştir. 2. veya 3. sürümde İngilizce desteği planlanmaktadır.
* Django, Flask gibi Framework'larla birlikte çalışabilir.

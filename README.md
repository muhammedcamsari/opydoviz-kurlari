# Python3 Döviz Kuru (Opydoviz-Kurlari)

opydoviz-kurlari, T.C. Merkez Bankası ve çeşitli döviz kuru yayıncılarının API sistemleri kullanılarak, anlık kur bilgilerinin bu sistemler üzerinden alınabilmesini ve geliştiriciye çeşitli formatlarda sunabilmesini sağlayan, açık kaynak kodlu Python3 kütüphanesidir.


## Kurulum
opydoviz-kurlari, PIP aracı ile kolay kurulum imkanı sağlar.

```
pip install opydoviz-kurlari
```

## Kullanım Örnekleri

```python

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import opydoviz
kur = opydoviz.kur()

# TCMB
tcmb = kur.tcmb('USD', 'SATIS', 'json')
print (tcmb)

# Truncgil API
truncgil = kur.truncgil('USD', 'ALIS', 'clear', verbose=True)
print (truncgil)

```


## Gelişmiş Kullanım ve Parametreler

Detaylı kullanım belgeleri için Wiki sayfasını incelemelisiniz. Size en iyi bilgiyi [Wiki](https://github.com/muhammedcamsari/opydoviz-kurlari/wiki/Giriş) sunar!


## 1.x Özellikler
1.x sürümü T.C. Merkez Bankası API ve Truncgil API baz alınarak yayınlanmıştır.

T.C. Merkez Bankası tarafından yayınlanan döviz kurlarının tamamını çıktı olarak verebilmekle birlikte, Truncgil API sayesinde altın kurlarını da görüntülemenize imkan sağlar.

Çeşitli özellikler listelenmiştir.
* Tüm Python3 sürümlerini destekler.
* Kur çıktıları için 3 farklı format desteğiyle gelir. (clear, text, json)
* Türkiye Cumhuriyeti Merkez Bankası ve Truncgil v3 API 1.0 sürümü itibariyle eklenmiştir.
* Çıktı yönetimi için opy-logger kullanıldı. opy-logger özelliklerini kullanmanıza imkan verir, çıktılar için loglama yapılabilir.
* Şu an yalnızca Türkçe dil seçeneğiyle geliştirilmiştir. 2.x veya 3.x sürümünde İngilizce desteği planlanmaktadır.
* Django, Flask gibi Framework'larla birlikte çalışabilir.
* Custom API servisi olarak kullanılabilir.

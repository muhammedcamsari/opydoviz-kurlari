#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import opylogger
import requests
import json
from bs4 import BeautifulSoup


__author__ = "Muhammed Çamsarı"
__appname__ = "opydoviz-kurlari"
__definition__ = "Python ile guncel doviz kurlarini goruntuleyin."
__copyright__ = "Copyright (c) 2022 " + __author__
__license__ = "MIT"
__version__ = "1.0"
__email__ = "muhammedcamsari@icloud.com"
__pgp__ = 'F294 1D36 A8C8 101B EEB0 16A7 B260 DBA5 2DAA 962A'

log = opylogger.log()


class kur():

	# TCMB
	def tcmb(self, parabirimi, islem, outformat='clear', verbose=False):

		if parabirimi:
			pass

		if islem == 'ALIS' or islem == 'SATIS':
			pass
		else:
			log.error('Gecersiz deger.')
			log.error('"islem" degeri "[ALIS | SATIS]" degerlerinden biri olmalidir.')
			exit()


		if outformat == 'clear' or outformat == 'text' or outformat == 'json':
			pass
		else:
			log.error('Gecersiz deger.')
			log.error('"outformat" degeri "[clear | text | json]" degerlerinden biri olmalidir.')
			exit()


		if verbose:
			log.debug('TC Merkez bankasi doviz kurlari fonksiyonu calistirildi.')
			log.debug('{} / {}'.format(__appname__, __version__))
			log.debug('"https://www.tcmb.gov.tr/kurlar/today.xml" baglantisi bekleniyor.')

		header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
		x = requests.get('https://www.tcmb.gov.tr/kurlar/today.xml', headers=header)

		if x.status_code == 200:
			if verbose == True:
				log.info('requests.status_code: 200')
				log.info('"https://www.tcmb.gov.tr/kurlar/today.xml" adresine baglanildi.')

				log.debug('Xml ciktisi ekrana yazdiriliyor.')
				log.output(x.text)

			if verbose == True:	
				log.debug('"BeautifulSoup()" ayiklaniyor..')
			source = BeautifulSoup(x.content, 'lxml',  from_encoding='UTF-8')
		
			if verbose == True:
				log.debug('"currency" degerleri ayiklaniyor..')
			xmldata = source.find_all('currency', {'kod': parabirimi})

			if verbose == True:
				log.output(xmldata)
				log.debug('"currency" degerleri ayiklandi, veriler isleniyor..')
			
			for i in xmldata:
				if verbose == True:
					log.debug(i)
				forexbuying = i.find_all('forexbuying')
				forexselling =  i.find_all('forexselling')

				unit = i.find_all('unit')
				isim = i.find_all('isim')

			if verbose == True:
				log.debug('"forexbuying" ve "forexselling" degerleri ayiklandi.')
				log.debug('"forexbuying" degeri {}'.format(forexbuying))
				log.debug('"forexselling" degeri {}'.format(forexselling))
				log.debug('"unit" degeri {}'.format(unit))
				log.debug('"isim" degeri {}'.format(isim))


			if verbose == True:
				log.debug('Veriler temizleniyor..')

			# STR
			satis_kur = str(forexselling)
			alis_kur = str(forexbuying)
			deger = str(unit)
			doviz = str(isim)

			# NENEW
			satis_kur = satis_kur.replace('[<forexselling>', '')
			satis_kur = satis_kur.replace('</forexselling>]', '')

			alis_kur = alis_kur.replace('[<forexbuying>', '')
			alis_kur = alis_kur.replace('</forexbuying>]', '')

			deger = deger.replace('[<unit>', '')
			deger = deger.replace('</unit>]', '')

			doviz = doviz.replace('[<isim>', '')
			doviz = doviz.replace('</isim>]', '')
		
			if verbose == True:
				log.debug('Veriler temizlendi. Cikti icin hazirlaniyor..')
		
			if outformat == 'clear':
				if islem == 'SATIS':
					return (satis_kur)

				elif islem == 'ALIS':
					return (alis_kur)

			elif outformat == 'text':
				if islem == 'SATIS':
					return ('{} {} ({}) şuan {} olarak satış işlemi görmektedir. '.format(deger, doviz, parabirimi, satis_kur))

				elif islem == 'ALIS':
					return ('{} {} ({}) şuan {} olarak alış işlemi görmektedir. '.format(deger, doviz, parabirimi, alis_kur))

			elif outformat == 'json':
				if islem == 'SATIS':
					value = 'Satis'
					tutar = satis_kur

				elif islem == 'ALIS':
					value = 'Alis'
					tutar = alis_kur

				data = {
					'deger': deger,
					'doviz': parabirimi,
					'doviz_adi': doviz,
					'islem': value,
					'tutar': tutar
				}
				return (data)

			if verbose == True:
				log.debug('Tum islemler tamamlandi.')

		else:
			return (x.status_code)



	def truncgil(self, parabirimi, islem, outformat='clear', verbose=False):

		if parabirimi:
			pass

		if islem == 'ALIS' or islem == 'SATIS':
			pass
		else:
			log.error('Gecersiz deger.')
			log.error('"islem" degeri "[ALIS | SATIS]" degerlerinden biri olmalidir.')
			exit()


		if outformat == 'clear' or outformat == 'text' or outformat == 'json':
			pass
		else:
			log.error('Gecersiz deger.')
			log.error('"outformat" degeri "[clear | text | json]" degerlerinden biri olmalidir.')
			exit()


		if verbose:
			log.debug('truncgil v3 doviz kurlari fonksiyonu calistirildi.')
			log.debug('{} / {}'.format(__appname__, __version__))
			log.debug('"https://finans.truncgil.com/v3/today.json" baglantisi bekleniyor.')

		header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
		y = requests.get('https://finans.truncgil.com/v3/today.json', headers=header)


		if y.status_code == 200:
			if verbose == True:
				log.info('requests.status_code: 200')
				log.info('"https://finans.truncgil.com/v3/today.json" adresine baglanildi.')

				log.debug('JSON ciktisi ekrana yazdiriliyor.')
				log.output(y.text)

			if verbose == True:	
				log.debug('JSON ayiklaniyor..')

			y = json.loads(y.text)

			if verbose == True:	
				log.debug('Veriler cikti icin hazirlaniyor..')
	
			if outformat == 'clear':
				if islem == 'ALIS':
					print (y[parabirimi]['Buying'])
				elif islem == 'SATIS':
					print (y[parabirimi]['Selling'])

			elif outformat == 'text':
				if islem == 'ALIS':
					return ('1 {} şuan {} olarak alış işlemi görmektedir. '.format(parabirimi, y[parabirimi]['Buying']))
				elif islem == 'SATIS':
					return ('1 {} şuan {} olarak satış işlemi görmektedir. '.format(parabirimi, y[parabirimi]['Selling']))

			elif outformat == 'json':
				if islem == 'ALIS':
					value = 'Alis'
					tutar = y[parabirimi]['Buying']

				elif islem == 'SATIS':
					value = 'Satis'
					tutar = y[parabirimi]['Selling']

				data = {
					'deger': '1',
					'doviz': parabirimi,
					'islem': value,
					'tutar': tutar,
				}
				return (data)

			if verbose == True:
				log.debug('Tum islemler tamamlandi.')

		else:
			return (y.status_code)


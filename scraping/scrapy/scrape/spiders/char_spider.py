# from tutorial.items import MyItem
# import scrapy
# import time
#
# char_line1 = ['大','小','一','二','三','十','百','千','多','不']
# char_line2 = ['人','夫','子','男','女','王','主','我','你','他']
# char_line3 = ['口','說','目','見','耳','聞','手','工','腳','行']
# char_line4 = ['來','入','出','上','下','中','在','左','右','有']
# char_line5 = ['吃','飯','菜','豆','肉','牛','豬','雞','魚','茶']
# char_line6 = ['國','家','校','文','學','狗','貓','馬','鳥','虫']
# char_line7 = ['日','月','天','地','海','木','火','土','金','水']
# char_line8 = ['氣','幹','雨','山','川','米','田','花','石','玉']
# char_line9 = ['村','店','車','衣','白','黑','紅','藍','藍','黃']
# char_line10= ['是','心','好','愛','喜','幸','生','死','力','疾']
# old_set = '大小一二三十百千多不人夫子男女王主我你他口說目見耳聞手工腳行來入出上下中在左右有吃飯菜豆肉牛豬雞魚茶國家校文學狗貓馬鳥虫日月天地海木火土金水氣幹雨山川米田花石玉村店車衣白黑紅藍藍黃是心好愛喜幸生死力疾'
# new_set = '军軍者意无無它与與长長把机機民第公此已使情明性知全又关關点點正业業外将將两兩高间間由问問很最重并並併物应應战戰向嚮头頭体體政美相见被利什等产産或新己制製身果加西斯话話合回特代内信表錶化老给給世位次度门門任常先通教儿兒原东東声聲提立及比员員的了这个们来为和国到以说时要就会可也对能而那得于着自之年过发后作里用道所然种事成方经么去法学如都同现当没动面起看定分还进部其些样理她本前开但因只从想实'
# era,era_english = ['甲骨文','金文','楚系文字','小篆'],['oracle','jinwen','chuxi','smallseal']
#
# class CharSpider(scrapy.Spider):
#     name = "chars"
#
#     def start_requests(self):
#         for c in new_set:
#             time.sleep(2)
#             try:
#                 big5= c.encode('big5').hex()
#                 url = 'http://char.iis.sinica.edu.tw/Search/char_SQL.aspx?char={}&type=0'.format(big5)
#                 yield scrapy.Request(url=url,meta={'char':c,'big5':big5})
#             except:
#                 continue
#
#     def parse(self, response):
#         meta = response.meta
#         # scrape original image
#         img = response.xpath("//img[@name='charImg']/@src").extract_first()[2:]
#         item = MyItem()
#         char_meta = []
#         img_url = 'http://char.iis.sinica.edu.tw' + img
#         img_name = 'acs/'+ meta['big5'] + '.jpg'
#         item['image_urls'],item['image_name'] = img_url,img_name
#         char_meta.append([meta['char'],meta['big5'],img_name])
#         time.sleep(2)
#         yield item
#
#         meta['id'] = idnum = response.xpath("//input[@type='hidden' and @name='char']/@value").extract()[0]
#         for chinese_era, english_era in zip(era, era_english):
#             time.sleep(2)
#             url = ("http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char={}&word={}&font={}".format(idnum,
#                                                                                                          meta['char'],
#                                                                                                          chinese_era))
#             print(url)
#             meta['era'] = chinese_era
#             meta['era_english'] = english_era
#             yield scrapy.Request(url=url,callback=self.parse_images,meta=meta)
#
#     def parse_images(self, response):
#         i = 0
#         item = MyItem()
#         char_meta = []
#
#         for elem in response.xpath("//img"):
#             m = response.meta
#             img_url = 'http://char.iis.sinica.edu.tw' + elem.xpath("@src").extract_first()
#             img_name = 'acs/' + m['big5'] + '/' + m['big5'] + '-' + m['era_english'] +'_'+ '{:03}'.format(i) + '.jpg'
#             item['image_urls'],item['image_name'] = img_url,img_name
#             char_meta.append([m['char'],m['big5'],m['id'],m['era_english'],m['era'],img_name])
#             i += 1
#             time.sleep(2)
#             yield item
#
#         with open('chars_data.csv', 'a') as c_data:
#             for row in char_meta:
#                 for column in row:
#                     c_data.write(column + ',')
#                 c_data.write('\n')
#         c_data.close()
#

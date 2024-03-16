# 数据类型说明

## 支持的基础类型


### faker.providers.address

	fake.address()                                                              # 81550 Freeman Crossroad Suite 109 Laurenfort, FL 75325
	fake.administrative_unit()                                                  # Alabama
	fake.bothify(text='## ??',                                                  # 37 sw
	  letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')           
	fake.building_number()                                                      # 268
	fake.city()                                                                 # Leahport
	fake.city_prefix()                                                          # Lake
	fake.city_suffix()                                                          # bury
	fake.country()                                                              # Indonesia
	fake.country_code(representation='alpha-2')                                 # TN
	fake.current_country()                                                      # United States
	fake.current_country_code()                                                 # US
	fake.hexify(text='^^^^', upper=False)                                       # b54f
	fake.language_code()                                                        # pt
	fake.lexify(text='????',                                                    # zDRe
	  letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')           
	fake.locale()                                                               # af_ZA
	fake.military_apo()                                                         # PSC 1118, Box 7104
	fake.military_dpo()                                                         # Unit 4236 Box 7158
	fake.military_ship()                                                        # USCGC
	fake.military_state()                                                       # AA
	fake.numerify(text='###')                                                   # 383
	fake.postalcode()                                                           # 43883
	fake.postalcode_in_state(state_abbr=None)                                   # 99905
	fake.postalcode_plus4()                                                     # 27849-0385
	fake.postcode()                                                             # 88545
	fake.postcode_in_state(state_abbr=None)                                     # 73024
	fake.random_choices(elements=('a', 'b', 'c'), length=None)                  # ['b', 'c', 'b']
	fake.random_digit()                                                         # 2
	fake.random_digit_above_two()                                               # 6
	fake.random_digit_not_null()                                                # 3
	fake.random_digit_not_null_or_empty()                                       # 2
	fake.random_digit_or_empty()                                                
	fake.random_element(elements=('a', 'b', 'c'))                               # a
	fake.random_elements(elements=('a', 'b', 'c'), length=None, unique=False,   # ['b', 'b', 'c']
	  use_weighting=None)                                                       
	fake.random_int(min=0, max=9999, step=1)                                    # 899
	fake.random_letter()                                                        # x
	fake.random_letters(length=16)                                              # ['E', 'v', 'j', 'D', 'l', 'l', 'o', 'T', 'R', 'P', 'Z', 'D', 'C', 'w',
	                                                                              't', 'S']
	fake.random_lowercase_letter()                                              # f
	fake.random_number(digits=None, fix_len=False)                              # 53599580
	fake.random_sample(elements=('a', 'b', 'c'), length=None)                   # ['b', 'a']
	fake.random_uppercase_letter()                                              # H
	fake.randomize_nb_elements(number=10, le=False, ge=False, min=None,         # 13
	  max=None)                                                                 
	fake.secondary_address()                                                    # Apt. 700
	fake.state()                                                                # West Virginia
	fake.state_abbr(include_territories=True,                                   # AS
	  include_freely_associated_states=True)                                    
	fake.street_address()                                                       # 9467 Patterson Summit
	fake.street_name()                                                          # Benitez Path
	fake.street_suffix()                                                        # Springs
	fake.zipcode()                                                              # 48550
	fake.zipcode_in_state(state_abbr=None)                                      # 51934
	fake.zipcode_plus4()                                                        # 48523-1569

### faker.providers.automotive

	fake.license_plate()                                                        # 356 MII
	fake.vin()                                                                  # UW62YWJ35W4ZXJ2AX

### faker.providers.bank

	fake.aba()                                                                  # 091314352
	fake.bank_country()                                                         # GB
	fake.bban()                                                                 # OGVC24778584633844
	fake.iban()                                                                 # GB56CLZP67690570267096
	fake.swift(length=None, primary=False, use_dataset=False)                   # FMWIGBZFM2D
	fake.swift11(primary=False, use_dataset=False)                              # BWPLGBXPYQD
	fake.swift8(use_dataset=False)                                              # NFGZGBHJ

### faker.providers.barcode

	fake.ean(length=13, prefixes=())                                            # 0608875251819
	fake.ean13(prefixes=(), leading_zero=None)                                  # 2331988468413
	fake.ean8(prefixes=())                                                      # 17336765
	fake.localized_ean(length=13)                                               # 0774944751006
	fake.localized_ean13()                                                      # 0768446465110
	fake.localized_ean8()                                                       # 02655574
	fake.upc_a(upc_ae_mode=False, base=None, number_system_digit=None)          # 553442498084
	fake.upc_e(base=None, number_system_digit=None, safe_mode=True)             # 07814428

### faker.providers.color

	fake.color(hue=None, luminosity=None, color_format='hex')                   # #7c3cb7
	fake.color_hsl(hue=None, luminosity=None)                                   # (188, 53, 68)
	fake.color_hsv(hue=None, luminosity=None)                                   # (25, 55, 94)
	fake.color_name()                                                           # Bisque
	fake.color_rgb(hue=None, luminosity=None)                                   # (135, 21, 6)
	fake.color_rgb_float(hue=None, luminosity=None)                             # (0.85, 0.67745, 0.35700000000000004)
	fake.hex_color()                                                            # #6c8404
	fake.rgb_color()                                                            # 238,133,13
	fake.rgb_css_color()                                                        # rgb(201,250,120)
	fake.safe_color_name()                                                      # olive
	fake.safe_hex_color()                                                       # #0088dd

### faker.providers.company

	fake.bs()                                                                   # orchestrate B2B relationships
	fake.catch_phrase()                                                         # Grass-roots client-driven flexibility
	fake.company()                                                              # Keller Inc
	fake.company_suffix()                                                       # Inc

### faker.providers.credit_card

	fake.credit_card_expire(start='now', end='+10y', date_format='%m/%y')       # 11/27
	fake.credit_card_full(card_type=None)                                       # JCB 15 digit Jonathan Rodriguez 213153317283489 04/28 CVC: 824
	fake.credit_card_number(card_type=None)                                     # 372632748167632
	fake.credit_card_provider(card_type=None)                                   # American Express
	fake.credit_card_security_code(card_type=None)                              # 0651

### faker.providers.currency

	fake.cryptocurrency()                                                       # ('LTC', 'Litecoin')
	fake.cryptocurrency_code()                                                  # DASH
	fake.cryptocurrency_name()                                                  # Ethereum
	fake.currency()                                                             # ('UGX', 'Ugandan shilling')
	fake.currency_code()                                                        # JOD
	fake.currency_name()                                                        # West African CFA franc
	fake.currency_symbol(code=None)                                             # E
	fake.pricetag()                                                             # $2.58

### faker.providers.date_time

	fake.am_pm()                                                                # PM
	fake.century()                                                              # VI
	fake.date(pattern='%Y-%m-%d', end_datetime=None)                            # 1980-01-17
	fake.date_between(start_date='-30y', end_date='today')                      # 2014-10-03
	fake.date_between_dates(date_start=None, date_end=None)                     # 2024-03-06
	fake.date_object(end_datetime=None)                                         # 2019-05-13
	fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115)             # 1910-02-24
	fake.date_this_century(before_today=True, after_today=False)                # 2020-06-12
	fake.date_this_decade(before_today=True, after_today=False)                 # 2023-04-23
	fake.date_this_month(before_today=True, after_today=False)                  # 2024-03-04
	fake.date_this_year(before_today=True, after_today=False)                   # 2024-01-01
	fake.date_time(tzinfo=None, end_datetime=None)                              # 1973-11-16 14:33:00.494038
	fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None)      # 0008-02-01 15:54:11.539055
	fake.date_time_between(start_date='-30y', end_date='now', tzinfo=None)      # 2015-06-17 23:04:11.257969
	fake.date_time_between_dates(datetime_start=None, datetime_end=None,        # 2024-03-06 16:50:59
	  tzinfo=None)                                                              
	fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)  # 2023-10-16 22:47:58.202318
	fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)   # 2020-10-21 04:49:32.757054
	fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)    # 2024-03-01 12:54:50.860383
	fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)     # 2024-02-21 23:38:10.870701
	fake.day_of_month()                                                         # 11
	fake.day_of_week()                                                          # Tuesday
	fake.future_date(end_date='+30d', tzinfo=None)                              # 2024-03-22
	fake.future_datetime(end_date='+30d', tzinfo=None)                          # 2024-03-10 13:49:50.378571
	fake.iso8601(tzinfo=None, end_datetime=None, sep='T', timespec='auto')      # 1973-01-08T03:39:23.385896
	fake.month()                                                                # 05
	fake.month_name()                                                           # April
	fake.past_date(start_date='-30d', tzinfo=None)                              # 2024-02-24
	fake.past_datetime(start_date='-30d', tzinfo=None)                          # 2024-03-06 04:42:42.373729
	fake.pytimezone(*args, **kwargs)                                            # tzfile('/usr/share/zoneinfo/Pacific/Port_Moresby')
	fake.time(pattern='%H:%M:%S', end_datetime=None)                            # 19:47:10
	fake.time_delta(end_datetime=None)                                          # 0:00:00
	fake.time_object(end_datetime=None)                                         # 04:42:04.769254
	fake.time_series(start_date='-30d', end_date='now', precision=None,         # <generator object Provider.time_series at 0x10ea58fb0>
	  distrib=None, tzinfo=None)                                                
	fake.timezone()                                                             # Asia/Damascus
	fake.unix_time(end_datetime=None, start_datetime=None)                      # 687720136.774966
	fake.year()                                                                 # 1974

### faker.providers.emoji

	fake.emoji()                                                                # 🪕

### faker.providers.file

	fake.file_extension(category=None)                                          # flac
	fake.file_name(category=None, extension=None)                               # pressure.xls
	fake.file_path(depth=1, category=None, extension=None, absolute=True,       # /attack/professor.pages
	  file_system_rule='linux')                                                 
	fake.mime_type(category=None)                                               # text/javascript
	fake.unix_device(prefix=None)                                               # /dev/xvdm
	fake.unix_partition(prefix=None)                                            # /dev/sdo2

### faker.providers.geo

	fake.coordinate(center=None, radius=0.001)                                  # -82.005242
	fake.latitude()                                                             # 16.2046585
	fake.latlng()                                                               # (Decimal('-76.9402285'), Decimal('-126.567122'))
	fake.local_latlng(country_code='US', coords_only=False)                     # ('37.60876', '-77.37331', 'Mechanicsville', 'US', 'America/New_York')
	fake.location_on_land(coords_only=False)                                    # ('47.05', '15.46667', 'Sankt Peter', 'AT', 'Europe/Vienna')
	fake.longitude()                                                            # -121.498980

### faker.providers.internet

	fake.ascii_company_email(*args, **kwargs)                                   # dylan05@butler-rodriguez.com
	fake.ascii_email(*args, **kwargs)                                           # alexismendoza@yahoo.com
	fake.ascii_free_email(*args, **kwargs)                                      # hprince@hotmail.com
	fake.ascii_safe_email(*args, **kwargs)                                      # ashley68@example.com
	fake.company_email(*args, **kwargs)                                         # daviscesar@watts-smith.com
	fake.dga(year=None, month=None, day=None, tld=None, length=None)            # ejukxwhwuiqtnvdlpdthnsifcnmbmxp.info
	fake.domain_name(*args, **kwargs)                                           # hudson-gordon.biz
	fake.domain_word(*args, **kwargs)                                           # shannon-gonzalez
	fake.email(*args, **kwargs)                                                 # georgehill@example.com
	fake.free_email(*args, **kwargs)                                            # ylong@hotmail.com
	fake.free_email_domain(*args, **kwargs)                                     # gmail.com
	fake.hostname(*args, **kwargs)                                              # desktop-42.fischer-young.org
	fake.http_method()                                                          # POST
	fake.http_status_code(include_unassigned=True)                              # 116
	fake.iana_id()                                                              # 7008873
	fake.image_url(width=None, height=None, placeholder_url=None)               # https://placekitten.com/761/764
	fake.ipv4(network=False, address_class=None, private=None)                  # 215.220.245.193
	fake.ipv4_network_class()                                                   # a
	fake.ipv4_private(network=False, address_class=None)                        # 192.168.32.215
	fake.ipv4_public(network=False, address_class=None)                         # 138.136.166.157
	fake.ipv6(network=False)                                                    # 4fee:14a9:3a94:1d75:9df6:e694:58e6:9f7e
	fake.mac_address(multicast=False)                                           # c2:64:aa:1c:76:34
	fake.nic_handle(suffix='FAKE')                                              # QZGA9857-FAKE
	fake.nic_handles(count=1, suffix='????')                                    # ['ZFRP843-RWUZ']
	fake.port_number(is_system=False, is_user=False, is_dynamic=False)          # 56018
	fake.ripe_id()                                                              # ORG-QM9-RIPE
	fake.safe_domain_name(*args, **kwargs)                                      # example.com
	fake.safe_email(*args, **kwargs)                                            # friedmanbrandi@example.org
	fake.slug(*args, **kwargs)                                                  # pay-then-popular
	fake.tld()                                                                  # net
	fake.uri(schemes=None, deep=None)                                           # https://clark.info/search/exploresearch.htm
	fake.uri_extension()                                                        # .htm
	fake.uri_page()                                                             # main
	fake.uri_path(deep=None)                                                    # app/list/explore
	fake.url(schemes=None)                                                      # https://www.phelps.org/
	fake.user_name(*args, **kwargs)                                             # hallandrew

### faker.providers.isbn

	fake.isbn10(separator='-')                                                  # 0-214-46601-9
	fake.isbn13(separator='-')                                                  # 978-0-9667528-4-7

### faker.providers.job

	fake.job()                                                                  # Maintenance engineer

### faker.providers.lorem

	fake.paragraph(nb_sentences=3, variable_nb_sentences=True,                  # Drop you write her fire high quickly. Agree occur available develop sell.
	  ext_word_list=None)                                                         According final wear later.
	fake.paragraphs(nb=3, ext_word_list=None)                                   # ['As its five leader. Option drop nor.', 'Voice shoulder find who.
	                                                                              Discover beautiful physical member.', 'Treatment third yeah. Art word
	                                                                              indicate rich toward. Room herself amount type.']
	fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)       # Opportunity hot smile role ok begin.
	fake.sentences(nb=3, ext_word_list=None)                                    # ['Role view produce deep.', 'Place her laugh.', 'Would man against story
	                                                                              this scene western.']
	fake.text(max_nb_chars=200, ext_word_list=None)                             # No recently site shoulder option live participant. Loss walk involve.
	                                                                              Final share hold candidate program Republican effort. Ten scientist at
	                                                                              consider partner. Line hard nice society.
	fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)                # ['Best avoid citizen become. Seem start reason unit by onto
	                                                                              government.\nNext wide region eye into increase. Trial control test win
	                                                                              fast.', 'Law politics record bag girl authority near know. Girl great
	                                                                              learn strategy southern. Same relationship bed recognize make.\nExecutive
	                                                                              standard piece. Save institution if old. Success Mr ask finish.', 'Fight
	                                                                              easy lay bill hot. Boy rather certain live anyone hear. Star education
	                                                                              difference maybe better share. Executive important hit thousand.']
	fake.word(part_of_speech=None, ext_word_list=None)                          # quality
	fake.words(nb=3, part_of_speech=None, ext_word_list=None, unique=False)     # ['expert', 'data', 'require']

### faker.providers.misc

	fake.binary(length=1048576)                                                 # b'\x1bW\xbc\x9f\x92y-
	                                                                              \x93\xd5\x86\x9d|\x06Sk\xbe\xe1\x95\x1dY\xaaHa)`o\xd6\xfdV`\xa1\xd8?\xd6\x
	                                                                              e5\xc2\xcf{\xa1&7w\xdbSg\xb2\xf8\xa3\x08\x9a\x16\xbc\x9f\x8aL55\x1b"\x85\x
	                                                                              12(.\xc7\x1a\xa4\xde\xdb|\xe4\xfa\x1e%8Mlp\x9d\xd7\x0f\xdb\x9f\xe4v,\x08\x'
	fake.boolean(chance_of_getting_true=50)                                     # False
	fake.csv(header=None, data_columns=('{{name}}', '{{address}}'),             # "Christina Crosby","33552 Ayala Walks Apt. 167 North Paula, WV 30111"
	  num_rows=10, include_row_ids=False)                                         "Christina Huff","1917 Adkins Rest South Keithchester, FL 08799"  "Michael
	                                                                              Carter","77377 Russell Vista Suite 263 North Jessefurt, VT 59741"
	                                                                              "Cynthia Hudson","77286 Patrick Dam Suite 037 North Nathan, AS 59346"
	                                                                              "John Simmons","0738 Smith Port Apt. 871 Andrewtown, PW 49599"  "Amber
	                                                                              Fisher","6493 Curry Hollow North Randallview, ME 05841"  "Thomas
	                                                                              Cooke","7947 Angela Hill Mendezburgh, MD 02257"  "Jeremy Cook","4301
	                                                                              Thompson Points Apt. 337 New Michael, PW 86835"  "Melissa Johnson","20306
	                                                                              Merritt Club West Zacharyville, MS 77131"  "Kathy Hanson","975 Ray Landing
	                                                                              Apt. 726 East Davidfurt, ME 42005"
	fake.dsv(dialect='faker-csv', header=None, data_columns=('{{name}}',        # "Olivia Davis","19740 Brandy Throughway Suite 999 Jenniferstad, NH 66659"
	  '{{address}}'), num_rows=10, include_row_ids=False, **fmtparams)            "John Adams","463 Davis Valley Suite 835 New Kimville, ND 82427"  "Drew
	                                                                              Hamilton","336 Jason Ferry Apt. 162 South Lauramouth, PR 73024"  "Diane
	                                                                              Wilson","9016 Amanda Freeway Suite 710 Timothymouth, ID 37374"  "Jerry
	                                                                              Knox","496 Russell Vista Apt. 946 North Dawn, NM 07665"  "Joshua
	                                                                              Green","264 Wright Spring Paulton, PA 95782"  "Melissa Andrews","4598
	                                                                              Angel Drive West Mia, VT 84979"  "Brandon Simmons","230 Harris Fall Port
	                                                                              Elizabethfurt, NE 72951"  "Brian Clark","8844 Hamilton Flat Apt. 516
	                                                                              Brownland, IN 38227"  "Daniel Pierce","PSC 1393, Box 7013 APO AA 65153"
	fake.fixed_width(data_columns=None, num_rows=10, align='left')              # Ethan Farley        19  Joseph Stanton      4   Andrew Jones        13
	                                                                              Kimberly Smith      0   Devin Smith         5   Christine Lane      4
	                                                                              Tonya Garcia        20  Tanya Williams      13  Patricia Sanchez    12
	                                                                              Austin Lutz         9
	fake.json(data_columns=None, num_rows=10, indent=None)                      # [{"name": "Lindsey Lamb", "residency": "949 Riley Drive\nWest Paulmouth,
	                                                                              CO 84924"}, {"name": "Michael Smith", "residency": "69259 Morgan
	                                                                              Wall\nGlennhaven, NY 29152"}, {"name": "Maria Sandoval", "residency":
	                                                                              "5360 Long Flat\nWest Jerrychester, FL 57545"}, {"name": "Jessica
	                                                                              Roberts", "residency": "6689 Jordan Trail\nPort Josephport, AS 65355"},
	                                                                              {"name": "Jacqueline Gonzales", "residency": "9897 Taylor Unions Apt.
	                                                                              851\nNorth Meganmouth, NY 25532"}, {"name": "Dana Hughes", "residency":
	                                                                              "PSC 3650, Box 5860\nAPO AP 66596"}, {"name": "Kevin Perez", "residency":
	                                                                              "4051 Crystal Unions\nFullerburgh, MT 28944"}, {"name": "Christopher
	                                                                              Carter", "residency": "702 Hamilton Landing\nBrandonshire, UT 71646"},
	                                                                              {"name": "Gary Green", "residency": "92120 Wood Route\nMelissafort, KS
	                                                                              20716"}, {"name": "Michelle Thomas", "residency": "668 Jordan Centers Apt.
	                                                                              262\nEast Ashleytown, NY 99457"}]
	fake.json_bytes(data_columns=None, num_rows=10, indent=None)                # b'[{"name": "Ashley Petersen", "residency": "673 Ashley Isle Apt.
	                                                                              852\\nAlyssaburgh, RI 53320"}, {"name": "Phillip Hunter", "residency":
	                                                                              "933 Hooper Knolls Suite 275\\nPort Linda, PA 21895"}, {"name": "Samuel
	                                                                              Thomas", "residency": "774 Ricky Estate\\nWest Curtis, MT 80318"},
	                                                                              {"name": "Nicholas Obrien", "residency": "801 Taylor Via\\nPort Hannah, WY
	                                                                              46804"}, {"name": "Devin Mann", "residency": "PSC 3221, Box 2468\\nAPO AA
	                                                                              38658"}, {"name": "Eric Wright", "residency": "36458 Ashley Roads\\nNew
	                                                                              Cassandra, KY 39175"}, {"name": "Mariah Mcdaniel", "residency": "143 Jo
	                                                                              Loaf Suite 638\\nClaymouth, AZ 63130"}, {"name": "Drew Nelson",
	                                                                              "residency": "89119 Hale View Apt. 789\\nTylerfurt, MO 24455"}, {"name":
	                                                                              "Tracy Price", "residency": "528 Weber Plaza Apt. 645\\nNorth Michael, WV
	                                                                              71424"}, {"name": "Jennifer Horn", "residency": "8810 Tracy
	                                                                              Mountain\\nKaufmanville, NV 22516"}]'
	fake.md5(raw_output=False)                                                  # 6a3953d6ff6cf14807d5182208cbe9e5
	fake.null_boolean()                                                         # False
	fake.password(length=10, special_chars=True, digits=True, upper_case=True,  # Q5TPsf#T(x
	  lower_case=True)                                                          
	fake.psv(header=None, data_columns=('{{name}}', '{{address}}'),             # "Alan Carney"|"250 Cervantes Trafficway South Mistyfurt, PR 55161"  "Jason
	  num_rows=10, include_row_ids=False)                                         Quinn DDS"|"925 Anderson Trail Suite 309 Port Megan, NY 96393"  "Paul
	                                                                              Pruitt"|"2788 Chang Estates Apt. 697 Garymouth, NC 93245"  "Kimberly
	                                                                              Scott"|"PSC 7222, Box 8033 APO AE 17611"  "Edward Cruz"|"0041 Dillon Lock
	                                                                              Huangmouth, PW 38777"  "Rebecca Powell"|"01800 John Gardens Suite 941 Lake
	                                                                              Antoniofort, AK 78465"  "Paul Schaefer"|"026 Farmer Pike Port Rachelshire,
	                                                                              CT 76103"  "Aaron Hardin"|"74361 Zhang Ford Rodriguezstad, WV 95430"
	                                                                              "Samuel White"|"5571 Reyes Hills Hernandezbury, VI 88739"  "Charles
	                                                                              Matthews"|"894 Jones Crescent Suite 377 Mcfarlandshire, DE 50427"
	fake.sha1(raw_output=False)                                                 # bf0946f3fd199f6488aedfc9eff651eff0232c4f
	fake.sha256(raw_output=False)                                               # 765143ff2a0066ea7f36638a7f7b775ac7952efe3f155ddf89dc7138ab79cce2
	fake.tar(uncompressed_size=65536, num_files=1, min_file_size=4096,          # b'UOzfbabJPmUzzmOPQgZG1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0
	  compression=None)                                                           0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
	                                                                              x00\x00\x00\x00\x00\x00......'
	fake.tsv(header=None, data_columns=('{{name}}', '{{address}}'),             # "Darin Rose"    "1434 Mills Lodge Wolfeberg, NC 45500"  "Ashley Gomez"
	  num_rows=10, include_row_ids=False)                                         "923 Russo Fork North Tanner, OR 88667"  "Rachel Morrison"       "847
	                                                                              Bonnie Landing Lake Joseph, WV 50274"  "Keith Scott"   "26345 Timothy
	                                                                              Village Suite 151 Millermouth, NH 67429"  "Denise Keith"  "758 Proctor
	                                                                              Locks Duncanview, TN 52125"  "Samuel Middleton"      "65708 Eric Crest
	                                                                              Karenborough, PA 37649"  "Bobby Diaz"    "70828 Santos Fields Parkermouth,
	                                                                              RI 40496"  "Misty Beltran DDS"     "39919 Jacob Center Apt. 587 Lake
	                                                                              Ericafurt, WI 64824"  "Brandon Thomas"        "853 Ford Falls Apt. 429
	                                                                              Hansonfurt, NH 03798"  "Daniel Meza"   "Unit 3972 Box 2027 DPO AE 69423"
	fake.uuid4(cast_to=<class 'str'>)                                           # e3912e01-95f8-455f-ab9a-147efcaec33a
	fake.zip(uncompressed_size=65536, num_files=1, min_file_size=4096,          # b'PK\x03\x04\x14\x00\x00\x00\x00\x00]\x86fX\xa7\x1a\xadb\x00\x04\x00\x00\x
	  compression=None)                                                           00\x04\x00\x00\x15\x00\x00\x00pEVhnwMHVErQORbxgtcv1\x0e\x12\xb6H\x96\xe8\x
	                                                                              ......'

### faker.providers.passport

	fake.passport_dates(birthday=2024-03-06)                                    # ('06 Mar 2024', '06 Mar 2024', '06 Mar 2029')
	fake.passport_dob()                                                         # 1932-08-09
	fake.passport_full()                                                        # Arthur Rodriguez M 11 Jul 1995 29 Jul 2019 29 Jul 2029 V32942291
	fake.passport_gender(seed=0)                                                # F
	fake.passport_number()                                                      # 186023063
	fake.passport_owner(gender='X')                                             # ('James', 'Clark')

### faker.providers.person

	fake.first_name()                                                           # Bailey
	fake.first_name_female()                                                    # Kristen
	fake.first_name_male()                                                      # Ryan
	fake.first_name_nonbinary()                                                 # Kayla
	fake.language_name()                                                        # Igbo
	fake.last_name()                                                            # Wood
	fake.last_name_female()                                                     # Moore
	fake.last_name_male()                                                       # Collins
	fake.last_name_nonbinary()                                                  # Sanders
	fake.name()                                                                 # William Little
	fake.name_female()                                                          # Claudia Cox
	fake.name_male()                                                            # Michael Williams
	fake.name_nonbinary()                                                       # Jeffrey Lewis
	fake.prefix()                                                               # Mr.
	fake.prefix_female()                                                        # Mrs.
	fake.prefix_male()                                                          # Dr.
	fake.prefix_nonbinary()                                                     # Mx.
	fake.suffix()                                                               # MD
	fake.suffix_female()                                                        # DDS
	fake.suffix_male()                                                          # DDS
	fake.suffix_nonbinary()                                                     # Jr.

### faker.providers.phone_number

	fake.basic_phone_number()                                                   # 673-484-0620
	fake.country_calling_code()                                                 # +1 939
	fake.msisdn()                                                               # 9846375211162
	fake.phone_number()                                                         # 546-750-8227x819

### faker.providers.profile

	fake.profile(fields=None, sex=None)                                         # {'job': 'Risk manager', 'company': 'Lopez, Campbell and Powell', 'ssn':
	                                                                              '640-77-9155', 'residence': '0256 Lloyd Lakes Suite 224\nNew Rachelport,
	                                                                              NH 71083', 'current_location': (Decimal('-64.0964095'),
	                                                                              Decimal('-78.572441')), 'blood_group': 'A-', 'website':
	                                                                              ['https://sims.net/'], 'username': 'rruiz', 'name': 'Jason Jones', 'sex':
	                                                                              'M', 'address': '151 Vincent Turnpike\nSimpsonmouth, MS 26413', 'mail':
	                                                                              'christopher03@gmail.com', 'birthdate': datetime.date(1914, 1, 25)}
	fake.simple_profile(sex=None)                                               # {'username': 'rebecca13', 'name': 'Miss Tina Tran MD', 'sex': 'F',
	                                                                              'address': '257 Jessica Plaza Suite 684\nHuynhstad, PA 16932', 'mail':
	                                                                              'amy63@gmail.com', 'birthdate': datetime.date(1913, 10, 9)}

### faker.providers.python

	fake.enum(enum_cls)                                                         # FakerEnum.A
	fake.pybool(truth_probability=50)                                           # True
	fake.pydecimal(left_digits=None, right_digits=None, positive=False,         # 988994542358086426960955447373257939167894699902289539.0890784308094891201
	  min_value=None, max_value=None)                                             59439770635392049563304362571989332603441123218822081003766
	fake.pydict(nb_elements=10, variable_nb_elements=True, value_types=None,    # {'international': 'hillkari@example.com', 'network': 7817, 'board':
	  allowed_types=None)                                                         'jonesdaisy@example.com', 'tend': 'mbAiSUWiFnyTYukXZISN', 'record':
	                                                                              'qBPCqkkSchdKZISZtFkW', 'bring': 2517}
	fake.pyfloat(left_digits=None, right_digits=None, positive=None,            # 611562231.41573
	  min_value=None, max_value=None)                                           
	fake.pyint(min_value=0, max_value=9999, step=1)                             # 161
	fake.pyiterable(nb_elements=10, variable_nb_elements=True,                  # ('NvpoVHSEYBBiUQRsXPvr', -5.71721379830282, Decimal('288.286900'),
	  value_types=None, allowed_types=None)                                       'hendrickscaitlin@example.com', 'fgOTzkCRjMgXDsHCFiyF',
	                                                                              'http://vaughn.info/main/posts/tagsindex.html', 'nUZdotmswknYWRFZGABN',
	                                                                              5526, 'wqamauvrWpyHRLfekxSb', Decimal('6188321922365458166666.456987682917
	                                                                              852907391406655211367088546377484156112570682406859128553866751908'),
	                                                                              'fONivzMmdqiZHsgHZRHk', 4023)
	fake.pylist(nb_elements=10, variable_nb_elements=True, value_types=None,    # ['aSfOkssCwuJvUezXsIHB', 'BnPgQrtInytRDkojWHRV', datetime.datetime(2000,
	  allowed_types=None)                                                         11, 13, 17, 9, 47, 735277), 'MjaIQPXXfJOUFeByTRQt', 4562,
	                                                                              'YntlwRssSoykYxGxWYvl', 'bsanchez@example.net', 1935,
	                                                                              'https://barnes.com/categories/list/taghomepage.jsp',
	                                                                              'scwLVNxCzRfhcXtohrYA', 'KtAEgbpUJxneEtDbqDVe', 'gqQzPWHSCBMkHtqXLVwb',
	                                                                              2249]
	fake.pyobject(object_type=None)                                             # None
	fake.pyset(nb_elements=10, variable_nb_elements=True, value_types=None,     # {'PGPNyIEUjLRiPkxRgGXc', 'oclpuKvaBWxKGKqAiRqF',
	  allowed_types=None)                                                         'eugenehoffman@example.org', datetime.datetime(1988, 12, 28, 13, 33, 2,
	                                                                              670999), 'http://weber.com/mainabout.html', 'eMVwdVzmBAjKKVzbYzRl', 7035,
	                                                                              'pfwueruNlOcOtqBSiKYi'}
	fake.pystr(min_chars=None, max_chars=20, prefix='', suffix='')              # BhglsMDFUSFvNbcWrfeg
	fake.pystr_format(string_format='?#-###{{random_int}}{{random_letter}}',    # d5-8794043g
	  letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')           
	fake.pystruct(count=10, value_types=None, allowed_types=None)               # (['EBtgpKbqalKqEOwyHtkD', datetime.datetime(1972, 11, 13, 0, 2, 46,
	                                                                              296635), 'http://mills-lewis.com/list/wp-content/wp-contentregister.htm',
	                                                                              'ZhcPZkVpdOriXuZLydkP', 'ndDRaHDMCivqmgdNdxzQ', ......)
	fake.pytuple(nb_elements=10, variable_nb_elements=True, value_types=None,   # (9306.9264314291, 'RdyVKDAhCCFlXNNljFBN', 'NGXtZpqwqjmSDoPfAWSw',
	  allowed_types=None)                                                         'https://www.brown-harmon.com/tags/list/searchcategory.htm',
	                                                                              'xgagaxvFmJgQaBpHmbcn', 'GLpwwngpCcQcWepnOkMz', 6098,
	                                                                              'SfHhlrRiGXpSluUCvOQN', 'iylPZSueVAjgFzZbnFtL', 'NyaLuOCcZjZFweeRiuqY',
	                                                                              'lfiEHeuDOAbuLfQxJpUF')

### faker.providers.sbn

	fake.sbn9(separator='-')                                                    # 258-87737-2

### faker.providers.ssn

	fake.ein()                                                                  # 57-3891268
	fake.invalid_ssn()                                                          # 333-27-0000
	fake.itin()                                                                 # 994-82-5830
	fake.ssn(taxpayer_identification_number_type='SSN')                         # 758-22-7278

### faker.providers.user_agent

	fake.android_platform_token()                                               # Android 2.3.6
	fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899)   # Mozilla/5.0 (Linux; Android 2.2.1) AppleWebKit/536.1 (KHTML, like Gecko)
	                                                                              Chrome/42.0.848.0 Safari/536.1
	fake.firefox()                                                              # Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_4 like Mac OS X) AppleWebKit/536.2
	                                                                              (KHTML, like Gecko) FxiOS/17.2o4793.0 Mobile/49Q661 Safari/536.2
	fake.internet_explorer()                                                    # Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 6.2; Trident/4.0)
	fake.ios_platform_token()                                                   # iPhone; CPU iPhone OS 12_4_8 like Mac OS X
	fake.linux_platform_token()                                                 # X11; Linux i686
	fake.linux_processor()                                                      # x86_64
	fake.mac_platform_token()                                                   # Macintosh; U; PPC Mac OS X 10_5_4
	fake.mac_processor()                                                        # U; Intel
	fake.opera()                                                                # Opera/9.76.(X11; Linux i686; ayc-PE) Presto/2.9.180 Version/12.00
	fake.safari()                                                               # Mozilla/5.0 (iPod; U; CPU iPhone OS 4_2 like Mac OS X; hi-IN)
	                                                                              AppleWebKit/531.48.3 (KHTML, like Gecko) Version/3.0.5 Mobile/8B115
	                                                                              Safari/6531.48.3
	fake.user_agent()                                                           # Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_6 rv:4.0; cy-GB)
	                                                                              AppleWebKit/532.41.6 (KHTML, like Gecko) Version/5.0 Safari/532.41.6
	fake.windows_platform_token()                                               # Windows NT 6.0


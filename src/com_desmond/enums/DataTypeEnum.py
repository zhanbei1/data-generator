#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> DataTypeEnum
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/6 16:43
@Desc   ：支持的数据类型枚举
==================================================
"""

from faker import Faker
from enum import Enum

from src.com_desmond.cutomer_data_type.CustomerDataType import CustomerDataType

fake = Faker()
fake.add_provider(CustomerDataType)


class DataType:
    def __init__(self, name: str, description: str, sample: str, function):
        self.name = name
        self.description = description
        self.sample = sample
        self.function = function


class DataTypeEnum(Enum):
    # providers.address
    ADDRESS = DataType("ADDRESS", "生成地址", "81550 Freeman Crossroad Suite 109 Laurenfort, FL 75325", fake.address)
    ADMINISTRATIVE_UNIT = DataType("ADMINISTRATIVE_UNIT", "行政单位", "Alabama", fake.administrative_unit)
    BUILDING_NUMBER = DataType("BUILDING_NUMBER", "门牌号", "268", fake.building_number)
    CITY = DataType("CITY", "城市", "Stacystad", fake.city)
    COUNTRY = DataType("COUNTRY", "国家", "Indonesia", fake.country)
    COUNTRY_CODE = DataType("COUNTRY_CODE", "城市编码", "US", fake.country_code)

    RANDOM_DIGIT = DataType("RANDOM_DIGIT", "随机数字", "2", fake.random_digit)
    RANDOM_DIGIT_ABOVE_TWO = DataType("RANDOM_DIGIT_ABOVE_TWO", "高于2的一个随机数字", "6", fake.random_digit_above_two)
    RANDOM_LETTER = DataType("RANDOM_LETTER", "随机字符", "x", fake.random_letter)
    ZIPCODE = DataType("ZIPCODE", "邮政编码。", "48550", fake.zipcode)
    ZIPCODE_PLUS4 = DataType("ZIPCODE_PLUS4", "加后四位的邮政编码。", "48523-1569", fake.zipcode_plus4)

    # faker.providers.automotive
    VIN = DataType("VIN", "生成vin编号。", "UW62YWJ35W4ZXJ2AX", fake.vin)
    LICENSE_PLATE = DataType("LICENSE_PLATE", "生成牌照。", "356 MII", fake.license_plate)

    #  faker.providers.bank
    ABA = DataType("ABA", "生成ABA路由转接号码。", "091314352", fake.aba)
    BANK_COUNTRY = DataType("BANK_COUNTRY", "生成银行提供商的ISO 3166-1字母-2国家代码。", "GB", fake.bank_country)
    BBAN = DataType("BBAN", "生成基本银行账号（BBAN）。", "OGVC24778584633844", fake.bban)
    IBAN = DataType("IBAN", "生成国际银行账号（IBAN）。", "OGVC24778584633844", fake.iban)

    # faker.providers.barcode
    EAN13 = DataType("EAN13", "生成EAN-13条码。", "2331988468413", fake.ean13)
    EAN8 = DataType("EAN8", "生成EAN-8条码。", "2331988468413", fake.ean8)

    # faker.providers.color
    COLOR_NAME = DataType("COLOR_NAME", "生成颜色名称。", "red", fake.color_name)
    COLOR_HSL = DataType("COLOR_HSL", "以一种人性化的方式生成一个RGB颜色的整数元组。", "(188, 53, 68)", fake.color_hsl)

    # faker.providers.company
    CATCH_PHRASE = DataType("CATCH_PHRASE", "生成公司口号。", "Strategic Paradigm", fake.catch_phrase)
    BS = DataType("BS", "生成公司业务。", "Triple-buffered stable service-desk", fake.bs)
    COMPANY = DataType("COMPANY", "生成公司名称。", "Beck Group", fake.company)

    # faker.providers.credit_card
    CREDIT_CARD_NUMBER = DataType("CREDIT_CARD_NUMBER", "生成信用卡号码。", "4321 4321 4321 432", fake.credit_card_number)
    CREDIT_CARD_EXPIRY_DATE = DataType("CREDIT_CARD_EXPIRY_DATE", "生成信用卡到期日。", "04/2020", fake.credit_card_expire)
    CREDIT_CARD_TYPE = DataType("CREDIT_CARD_TYPE", "生成信用卡提供商名称。", "MasterCard", fake.credit_card_provider)

    # faker.providers.currency
    CURRENCY_NAME = DataType("CURRENCY_NAME", "生成货币名称。", "Euro", fake.currency_name)
    CURRENCY_CODE = DataType("CURRENCY_CODE", "生成货币代码。", "EUR", fake.currency_code)
    CURRENCY_SYMBOL = DataType("CURRENCY_SYMBOL", "生成货币符号。", "€", fake.currency_symbol)
    CRYPTOCURRENCY = DataType("CRYPTOCURRENCY", "生成加密货币简称和名称对应元祖。", "Bitcoin", fake.cryptocurrency)
    CRYPTOCURRENCY_CODE = DataType("CRYPTOCURRENCY_CODE", "生成加密货币代码。", "BTC", fake.cryptocurrency_code)
    CRYPTOCURRENCY_NAME = DataType("CRYPTOCURRENCY_NAME", "生成加密货币名称。", "Bitcoin", fake.cryptocurrency_name)

    # faker.providers.date_time
    DATE_TIME = DataType("DATE_TIME", "生成日期时间，默认格式为：YYYY-MM-dd HH:mm:ss。", "2020-01-01 12:00:00", fake.date_time)
    CENTURY = DataType("CENTURY", "生成世纪。", "VI", fake.century)
    AM_PM = DataType("AM_PM", "生成上午或下午。", "AM", fake.am_pm)
    DATE = DataType("DATE", "生成日期，默认格式：YYYY-MM-dd。", "2020-01-01", fake.date)
    DAY_OF_MONTH = DataType("DAY_OF_MONTH", "生成日期，默认格式：dd。", "01", fake.day_of_month)
    DAY_OF_WEEK = DataType("DAY_OF_WEEK", "生成日期，默认格式：dd。", "Monday", fake.day_of_week)
    MONTH = DataType("MONTH", "生成月份，默认格式：MM。", "01", fake.month)
    MONTH_NAME = DataType("MONTH_NAME", "生成月份，默认格式：January。", "January", fake.month_name)
    TIME = DataType("TIME", "生成时间，默认格式：HH:mm:ss。", "12:00:00", fake.time)
    TIMEZONE = DataType("TIMEZONE", "生成时区，默认格式：UTC+4。", "UTC+4", fake.timezone)
    YEAR = DataType("YEAR", "生成年份，默认格式：YYYY。", "2020", fake.year)
    UNIX_TIME = DataType("UNIX_TIME", "生成Unix时间戳。", "160000000", fake.unix_time)
    UNIX_TIME_MS = DataType("UNIX_TIME_MS", "生成Unix时间戳（毫秒）。", "16000000000", fake.unix_time_ms)
    ISO8601 = DataType("ISO8601", "生成ISO8601时间格式。", "2020-01-01T12:00:00+08:00", fake.iso8601)
    # faker.providers.emoji
    EMOJI = DataType("EMOJI", "生成emoji。", "😊", fake.emoji)

    # faker.providers.file
    FILE_EXTENSION = DataType("FILE_EXTENSION", "生成文件扩展名。", "txt", fake.file_extension)
    FILE_NAME = DataType("FILE_NAME", "生成文件名。", "test.txt", fake.file_name)
    FILE_PATH = DataType("FILE_PATH", "生成文件路径。", "/home/user/test.txt", fake.file_path)
    MIME_TYPE = DataType("MIME_TYPE", "在指定的类别下生成mime类型。", "text/plain", fake.mime_type)
    UNIX_DEVICE = DataType("UNIX_DEVICE", "生成Unix设备文件名。", "16777215", fake.unix_device)
    UNIX_PARTITION = DataType("UNIX_PARTITION", "生成Unix分区名。", "65535", fake.unix_partition)

    # faker.providers.geo
    COORDINATE = DataType("COORDINATE", "随机生成一个坐标", "-82.005242", fake.coordinate)
    LATITUDE = DataType("LATITUDE", "生成一个纬度坐标，范围在-90到90之间", "-82.005242", fake.latitude)
    LATLNG = DataType("LATLNG", "生成一个经纬度坐标，格式为(latitude, longitude)", "-82.005242, 23.005242", fake.latlng)
    LONGITUDE = DataType("LONGITUDE", "生成一个经度坐标，范围在-180到180之间", "-82.005242", fake.longitude)
    LOCATION_ON_LAND = DataType("LOCATION_ON_LAND", "生成一个在陆地的经纬度坐标。",
                                "('47.05', '15.46667', 'Sankt Peter', 'AT', 'Europe/Vienna')", fake.location_on_land)

    # faker.providers.internet
    ASCII_COMPANY_EMAIL = DataType("ASCII_COMPANY_EMAIL", "生成一个ASCII字符集的公司的电子邮件地址。", "example@example.com",
                                   fake.ascii_company_email)
    EMAIL = DataType("EMAIL", "生成一个电子邮件地址。", "example@example.com", fake.email)
    HOSTNAME = DataType("HOSTNAME", "生成一个主机名。", "example.com", fake.hostname)
    HTTP_METHOD = DataType("HTTP_METHOD", "生成一个HTTP方法。", "GET", fake.http_method)
    HTTP_STATUS_CODE = DataType("HTTP_STATUS_CODE", "生成一个HTTP状态码。", "200", fake.http_status_code)
    # IPV4_ADDRESS = DataType("IPV4_ADDRESS", "生成一个IPv4地址。", "127.0.0.1", fake.ipv4)
    IPV6 = DataType("IPV6", "生成一个IPv6地址。", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", fake.ipv6)
    IMAGE_URL = DataType("IMAGE_URL", "生成一个随机的图片URL。", "https://placeimg.com/640/480/any", fake.image_url)
    IPV4_PRIVATE = DataType("IPV4_PRIVATE", "生成一个随机的私有IPv4地址。", "192.168.0.1", fake.ipv4_private)
    IPV4_PUBLIC = DataType("IPV4_PUBLIC", "生成一个随机的公共IPv4地址。", "8.8.8.8", fake.ipv4_public)
    MAC_ADDRESS = DataType("MAC_ADDRESS", "生成一个随机的MAC地址。", "08:00:27:00:00:00", fake.mac_address)
    NIC_HANDLE = DataType("NIC_HANDLE", "生成一个随机的网络接口卡（NIC）句柄。", "QZGA9857-FAKE", fake.nic_handle)
    PORT_NUMBER = DataType("PORT_NUMBER", "生成一个随机的端口号。", "80", fake.port_number)
    RIPE_ID = DataType("RIPE_ID", "生成一个随机的RIPE ID。", "ABCD-EXAMPLE-12345", fake.ripe_id)
    SAFE_DOMAIN_NAME = DataType("SAFE_DOMAIN_NAME", "生成一个随机的、安全的主机名。", "example.com", fake.safe_domain_name)
    SLUG = DataType("SLUG", "生成一个随机的算法名称。", "this-is-a-test", fake.slug)
    TLD = DataType("TLD", "生成一个随机的顶级域名后缀（TLD）。", "com", fake.tld)
    URI = DataType("URI", "生成一个随机的URI。", "https://clark.info/search/exploresearch.htm", fake.uri)
    URI_EXTENSION = DataType("URI_EXTENSION", "生成一个随机的URI扩展名。", "html", fake.uri_extension)
    URI_PATH = DataType("URI_PATH", "生成一个随机的URI路径。", "/path/to/resource", fake.uri_path)
    USER_NAME = DataType("USER_NAME", "生成一个随机的用户名。", "john_doe", fake.user_name)
    URL = DataType("URL", "生成一个随机的URL。", "https://example.com/path/to/resource", fake.url)

    # faker.providers.isbn
    ISBN10 = DataType("ISBN10", "生成一个随机的ISBN-10码， 默认'-'隔离开。", "0-214-46601-9", fake.isbn10)
    ISBN13 = DataType("ISBN13", "生成一个随机的ISBN-13码，默认'-'隔离开。", "978-0-9667528-4-7", fake.isbn13)

    # faker.providers.job
    JOB = DataType("JOB", "生成一个随机的职业。", "Software Engineer", fake.job)

    # faker.providers.lorem
    PARAGRAPH = DataType("PARAGRAPH", "生成一个随机的段落。", "Lorem ipsum dolor sit amet, consectetur a......", fake.paragraph)
    PARAGRAPHS = DataType("PARAGRAPHS", "生成一个随机的段落列表(默认3个)。",
                          '["Lorem ipsum ......", "Consectetur adipiscing elit......", "Sed do eiusmod tempor incididunt ......"]',
                          fake.paragraphs)
    SENTENCE = DataType("SENTENCE", "生成一个随机的句子。", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                        fake.sentence)
    SENTENCES = DataType("SENTENCES", "生成一个随机的句子列表(默认3个)。",
                         '["Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."]',
                         fake.sentences)

    TEXT = DataType("TEXT", "生成一个随机的文本。",
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    fake.text)
    TEXTS = DataType("TEXTS", "生成一个随机的文本列表(默认3个)。",
                     '["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."]',
                     fake.texts)
    WORD = DataType("WORD", "生成一个随机的单词。", "Lorem", fake.word)
    WORDS = DataType("WORDS", "生成一个随机的单词列表(默认3个)。", '["Lorem", "ipsum", "dolor", "sit", "amet"]', fake.words)

    # faker.providers.misc
    BINARY = DataType("BINARY", "生成一个随机的二进制数据。",
                      "\x1bW\xbc\x9f\x92y-\x93\xd5\x86\x9d|\x06Sk\xbe\xe1\x95\x1dY\xaaHa)`o\xd6\xfdV`\xa1\xd8?\xd6\xe5\xc2\。",
                      fake.binary)
    BOOLEAN = DataType("BOOLEAN", "生成一个随机的布尔值。", "True", fake.boolean)
    CSV = DataType("CSV", "生成一个随机的CSV数据。",
                   '"Christina Crosby","33552 Ayala Walks Apt. 167 North Paula, WV 30111"\n"Christina Huff","1917 Adkins Rest South Keithchester, FL 08799"\n"MichaelCarter","77377 Russell Vista Suite 263 North Jessefurt, VT 59741"\n"Cynthia Hudson","77286 Patrick Dam Suite 037 North Nathan, AS 59346"\n"John Simmons","0738 Smith Port Apt. 871 Andrewtown, PW 49599"\n"Amber"',
                   fake.csv)
    JSON = DataType("JSON", "生成一个随机的JSON数据。", '{"name": "John", "age": 30, "city": "New York"}', fake.json)

    JSON_BYTES = DataType("JSON_BYTES", "生成一个随机的JSON byte 类型数据。", 'b"{"name": "John", "age": 30, "city": "New York"}"',
                          fake.json_bytes)
    MD5 = DataType("MD5", "生成一个随机的MD5 类型数据。", "65a8e27d887f45e2550d3791e61f591", fake.md5)
    PASSWORD = DataType("PASSWORD", "生成一个随机的10位密码。", "Q5TPsf#T(x", fake.password)
    SHA1 = DataType("SHA1", "生成一个随机的SHA1 类型数据。", "65a8e27d887f45e2550d3791e61f591", fake.sha1)
    SHA256 = DataType("SHA256", "生成一个随机的SHA256 类型数据。", "65a8e27d887f45e2550d3791e61f591", fake.sha256)
    UUID4 = DataType("UUID4", "生成一个随机的UUID4 类型数据。", "d85059bb-c0c5-4915-981b-5194e63a9067", fake.uuid4)

    # faker.providers.person
    NAME = DataType("NAME", "生成一个随机的名字。", "Christina Huff", fake.name)

    # faker.providers.phone_number
    PHONE_NUMBER = DataType("PHONE_NUMBER", "生成一个随机的电话号码。", "(087) 555-1212", fake.phone_number)

    # faker.providers.profile
    PROFILE = DataType("PROFILE", "生成一个随机的个人完整信息。",
                       '{"name": "John", "surname": "Doe", "address": "1234 Main St", "city": "New York", "country": "United States", "postcode": "10001"}',
                       fake.profile)
    SIMPLE_PROFILE = DataType("SIMPLE_PROFILE", "生成一个随机的个人简单信息。", '{"name": "John", "surname": "Doe"}',
                              fake.simple_profile)

    # faker.providers.user_agent
    ANDROID_PLATFORM_TOKEN = DataType("ANDROID_PLATFORM_TOKEN", "生成一个随机的Android平台令牌。", "Linux; Android 10; SM-G975U1",
                                      fake.android_platform_token)
    CHROME = DataType("CHROME", "生成一个随机的Chrome浏览器用户代理。",
                      "Mozilla/5.0 (Linux; Android 10; SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
                      fake.chrome)
    FIREFOX = DataType("FIREFOX", "生成一个随机的Firefox浏览器用户代理。",
                       "Mozilla/5.0 (Android 10; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0", fake.firefox)
    INTERNET_EXPLORER = DataType("INTERNET_EXPLORER", "生成一个随机的Internet Explorer浏览器用户代理。",
                                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36",
                                 fake.internet_explorer)
    IOS_PLATFORM_TOKEN = DataType("IOS_PLATFORM_TOKEN", "生成一个随机的iOS平台令牌。", "iPhone9,2", fake.ios_platform_token)
    LINUX_PLATFORM_TOKEN = DataType("LINUX_PLATFORM_TOKEN", "生成一个随机的Linux平台令牌。", "X11; Linux x86_64",
                                    fake.linux_platform_token)
    LINUX_PROCESSOR = DataType("LINUX_PROCESSOR", "生成一个随机的Linux处理器。", "x86_64", fake.linux_processor)
    MAC_PLATFORM_TOKEN = DataType("MAC_PLATFORM_TOKEN", "生成一个随机的Mac平台令牌。", "Macintosh; Intel Mac OS X 10_15_7",
                                  fake.mac_platform_token)
    MAC_PROCESSOR = DataType("MAC_PROCESSOR", "生成一个随机的Mac处理器。", "U; Intel", fake.mac_processor)
    OPERA = DataType("OPERA", "生成一个随机的Opera浏览器用户代理。",
                     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36 OPR/74.0.3914.68",
                     fake.opera)
    SAFARI = DataType("SAFARI", "生成一个随机的Safari浏览器用户代理。",
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
                      fake.safari)
    WINDOWS_PLATFORM_TOKEN = DataType("WINDOWS_PLATFORM_TOKEN", "生成一个随机的Windows平台令牌。", "Windows NT 10.0; Win64; x64",
                                      fake.windows_platform_token)

    @staticmethod
    def value_of(name: str):
        t = DataTypeEnum[name]
        return t.value

    @staticmethod
    def generator_by_key(name: str):
        type_model: DataType = DataTypeEnum.value_of(name)
        result = type_model.function()
        if type(result) == type:
            return str(result)
        else:
            return type_model.function()


if __name__ == '__main__':
    print(DataTypeEnum.ADDRESS)
    print(DataTypeEnum.value_of("ADDRESS"))

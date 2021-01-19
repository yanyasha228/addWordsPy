# This is a sample Python script.

import products
import re
import pymorphy2

# Press the green button in the gutter to run the script.

bad_entries = [" , ",
               " - "
               " & ",
               " &",
               "& ",
               ", ",
               " ,",
               " -",
               "- ",
               ";",
               ":",
               "!",
               "(",
               ")"
               "\""]
key_add_words = ["купить", "распродажа"]

xmlPath = "https://gunsto.prom.ua/yandex_market.xml?hash_tag=b9ad6ea71fccc0f742251582148b0f12&sales_notes=&product_ids=&label_ids=3204078&exclude_fields=&html_description=0&yandex_cpa=&process_presence_sure=&export_lang=ru&group_ids="


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


if __name__ == '__main__':
    # productList = products.XmlPromProductService.get_products(xmlPath)
    productList = [
        products.Product("32431414", 'Пули H&N Silver Point (0.75г, 500 шт)', 'Пуля для пневматического оружия')]
    analyz = pymorphy2.MorphAnalyzer()
    wordParse = analyz.parse("пневматическая винтовка")[0]
    dich2 = wordParse.inflect({'sing', 'accs'}).word

    for product in productList:
        product_key_words = set()
        product_name = product.name.lower()
        for bad in bad_entries:
            product_name = product_name.replace(bad, " ")

        product_name = re.sub(' +', ' ', product_name)
        product_group_name = product.group_name.lower()

        group_name_words_arr = product_group_name.split(" ")
        product_name_words_arr = product_name.split(" ")
        dich = 89

    kuk = 0

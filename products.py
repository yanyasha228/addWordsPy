import requests
import xml.etree.ElementTree as ElementTree

bad_entries = [" , ",
               ", "
               " ,"
               ";",
               ":",
               "!",
               " -",
               "- ",
               " - ",
               "&"
               "\""]
key_add_words = ["купить", "распродажа", "акция"]


class Product:
    def __init__(self, prod_id: str, name: str, group_name: str):
        self.__id = int(prod_id)
        self.__name = name
        self.__group_name = group_name
        self.__key_words = str

    @property
    def key_words(self):
        return self.key_words

    @key_words.setter
    def key_words(self, key_words: str):
        self.__key_words = key_words

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group_name(self):
        return self.__group_name


class ProductKeyWordsGenerator:

    @staticmethod
    def generate_product_keywords(products: [Product]):
        for product in products:
            product_name = product.name
            category_name = product.group_name


class XmlPromProductService:

    @staticmethod
    def get_products(url: str):
        response_prom_xml = requests.get(url)

        str_res_prom = str(response_prom_xml.content, 'utf-8')

        elem_tree_prom = ElementTree.fromstring(str_res_prom)

        product_list = list()

        categories_map = {}

        category_item_list = list()
        category_item = None

        for elC in elem_tree_prom.iter('categories'):
            category_item_list.append(elC)

        category_item = category_item_list[0]

        for elPrCategory in category_item.findall('category'):
            categories_map[elPrCategory.get('id')] = elPrCategory.text

        for elPr in elem_tree_prom.iter('offer'):
            prodId = elPr.get('id')
            prodName = elPr.find('name').text
            prodCategoryName = categories_map[elPr.find('categoryId').text]
            product_list.append(Product(prod_id=prodId, name=prodName, group_name=prodCategoryName))

        return product_list

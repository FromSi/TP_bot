from requests import get
import xml.etree.ElementTree as ET

def data(name):
    """Получить сегодняшний гороскоп ${name}
    
    Аргументы функции:
    name -- название гороскопа
    """
    response = get('http://img.ignio.com/r/export/utf/xml/daily/com.xml')

    return parser(response.content, name)

def parser(xml, name):
    """Парсинг XML с сайта http://img.ignio.com
    
    Аргументы функции:
    xml -- XML ответ сайта http://img.ignio.com
    name -- название гороскопа
    """
    tree = ET.fromstring(xml)
    root = tree

    return root.find(name).find('today').text
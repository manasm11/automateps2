import pickle
from decouple import config
from webbot import Browser
from lxml import etree
from time import sleep

class PS2Stations:
    def login(self, username=config('USERNAME'), password=config('PASSWORD')):
        b = Browser(browser_executable='brave-browser')
        self.b = b
        b.go_to('http://psd.bits-pilani.ac.in/Login.aspx')
        b.type(username, xpath='//*[@login="login"]')
        b.type(password, xpath='//*[@type="password"]')
        b.click('Login')
        while b.exists('ACCEPT PS TERMS AND CONDITIONS(PROCEED To Dashboard)'):
            b.click('ACCEPT PS TERMS AND CONDITIONS(PROCEED To Dashboard)')
            sleep(0.5)
            b.scrolly(99999999999999)

    def go_to_stations_list(self):
        b = self.b
        b.click('Problem Bank')
        b.click('View Active Station Problem Banks')
        self.tree = etree.HTML(b.driver.page_source)

    def update_stations_from_stations_list(self):
        rows = self.tree.findall('.//*[@id="prohid"]')
        self.rows = rows
        ids = ['sno', 'lOCATION', 'stationname', 'Industry', 'stipend']
        self.stations = [Station() for _ in range(len(rows))]
        stations = self.stations
        tree = self.tree
        for id_ in ids:
            for i,e in enumerate(tree.findall(f'.//*[@id="{id_}"]')):
                s = stations[i]
                t = e.text
                if id_ == ids[0]:
                    s.sno = t
                elif id_ == ids[1]:
                    s.location = t
                elif id_ == ids[2]:
                    s.name = t
                elif id_ == ids[3]:
                    s.industry = t
                else:
                    s.stipend = t

    def export_stations_to_pickle_file(self, filename):
        with open('stations_raw1.data', 'wb') as f:
            pickle.dump(self.stations, f)

    def import_stations_from_pickle_file(self, filename):
        with open('stations_raw1.data', 'rb') as f:
            self.stations = pickle.load(f)
        return self.stations

#views = b.find_elements(css_selector='#StationData')
#views[0].click()
#b.find_elements(id='viewProj')
#[Out]# [<selenium.webdriver.remote.webelement.WebElement (session="4b01a2aeef73f35144416e74a798fdd4", element="c6a66b67-51e6-40eb-b6a0-78024d943cae")>,
#[Out]#  <selenium.webdriver.remote.webelement.WebElement (session="4b01a2aeef73f35144416e74a798fdd4", element="287b44a2-6069-4020-a6b0-5ccec594a4ce")>,
#[Out]#  <selenium.webdriver.remote.webelement.WebElement (session="4b01a2aeef73f35144416e74a798fdd4", element="dcd12179-ca89-41c0-926a-91332fb121ae")>,
#[Out]#  <selenium.webdriver.remote.webelement.WebElement (session="4b01a2aeef73f35144416e74a798fdd4", element="70bf73b5-6291-47f2-807c-c59218f4eb6d")>]
#len(_)
##[Out]# 4
#b.switch_to_tab(2)
#tree2 = etree.HTML(b.driver.page_source)
#tree2.cssselect('h4')
##[Out]# [<Element h4 at 0x7f785db2f3c8>,
##[Out]#  <Element h4 at 0x7f785db59d88>,
##[Out]#  <Element h4 at 0x7f785e0242c8>]
#tree2.cssselect('.title')
##[Out]# [<Element td at 0x7f785e088e88>, <Element td at 0x7f785dc7bdc8>]
#tree2.cssselect('.title')[0].text
##[Out]# 'Web application development'
#stations.project = tree2.cssselect('.title')[0].text
#stations[0].project = tree2.cssselect('.title')[0].text
#tree2.cssselect('.Des')[0].text
#[Out]# 'As an enterprise SaaS product,\nwork will be adding new\nfeatures for the core product\nwrt. functionality and\ncustomer requirements.\n'
#stations[0].description = tree2.cssselect('.Des')[0].text
#tree2.cssselect('.Skil')[0].text
##[Out]# 'Data Analytics , Database , Database systems , Javascript (Reactjs and Nodejs), , Analytical and Problem solving skills , communication skill'
#stations[0].skills = tree2.cssselect('.Skil')[0].text
#b.go_back()
#b.click(id='StationData')
#stations[0]
##[Out]# <__main__.Station at 0x7f785f236668>
class Station:
    pass

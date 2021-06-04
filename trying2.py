# IPython log file
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

    def go_to_station_detail_modal(self, station_index):
        self.__i = station_index
        i = station_index
        #p.b.driver.execute_script("window.debugger=function(){};")
        detail_links = p.b.find_elements(id='StationData')
        detail_links[i].click()

    def update_stations_list_from_detail_modal(self):
        i = self.__i
        tree2 = etree.HTML(p.b.driver.page_source)
        tree2.findall('.//*[@id="viewProj"]')
        self.stations[i]._batch = tree2.findall('.//*[@id="BatchID"]')[0].text
        self.stations[i].nprojects = tree2.findall('.//*[@id="NoOfProject"]')[0].text
        self.stations[i].disciplines = tree2.findall('.//*[@id="Tag"]')[0].text

    def export_stations_to_pickle_file(self, filename):
        with open('stations_raw1.data', 'wb') as f:
            pickle.dump(self.stations, f)

    def import_stations_from_pickle_file(self, filename):
        with open('stations_raw1.data', 'rb') as f:
            self.stations = pickle.load(f)
        return self.stations

class Station:
    pass

#p = PS2Stations()
#p.login()
#p.go_to_stations_list()
#p.update_stations_from_stations_list()
#p.stations
#p.stations[0]
##[Out]# <__main__.Station at 0x7ff88e6b1128>
##p.stations[0].industry
##[Out]# 'IT'
##p.stations[4].industry
##[Out]# 'Finance and Mgmt'
##p.b.go_back()
##p.go_to_stations_list()
#len(detail_links)
##[Out]# 275
#detail_links[0]
##[Out]# <selenium.webdriver.remote.webelement.WebElement (session="5d9343bde83ea41dcc88e791a01dccfc", element="7fd32d13-d5f4-45d2-af22-c453be35ee3e")>
#detail_links[0].click()
#tree2 = etree.HTML(p.b.driver.page_source)
#tree2.findall('.//*[@id="viewProj"]')
##[Out]# [<Element a at 0x7ff88e4d3208>,
##[Out]#  <Element a at 0x7ff88e750a48>,
##[Out]#  <Element a at 0x7ff88e4d32c8>,
##[Out]#  <Element a at 0x7ff88e4d3588>,
##[Out]#  <Element a at 0x7ff88e4d39c8>]
#tree2.findall('.//*[@id="viewProj"]')[0]
##[Out]# <Element a at 0x7ff88e4d3208>
#tree2.findall('.//*[@id="BatchID"]')
##[Out]# [<Element td at 0x7ff89f114408>,
##[Out]#  <Element td at 0x7ff88e4e1b48>,
##[Out]#  <Element td at 0x7ff88e477848>,
##[Out]#  <Element td at 0x7ff88e477f08>,
##[Out]#  <Element td at 0x7ff88e477748>]
#tree2.findall('.//*[@id="BatchID"]')[0].text
##[Out]# '2021-2022 / SEM-I'
#stations[0]._batch = tree2.findall('.//*[@id="BatchID"]')[0].text
#p.stations[0]._batch = tree2.findall('.//*[@id="BatchID"]')[0].text
#p.stations[0]._batch
##[Out]# '2021-2022 / SEM-I'
#p.stations[0].stipend
##[Out]# '30000'
#p.stations[0].nprojects = tree2.findall('.//*[@id="NoOfProject"]')[0].text
#p.stations[0].nprojects
##[Out]# '1'
#p.stations[0].disciplines = tree2.findall('.//*[@id="Tag"]')[0].text
#p.stations[0].disciplines

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
        i = station_index
        #p.b.driver.execute_script("window.debugger=function(){};")
        if not hasattr(self, 'detail_links'):
            self.detail_links = p.b.find_elements(id='StationData')
        self.detail_links[i].click()

    def update_stations_list_from_detail_modal(self, station_index):
        i = station_index
        tree2 = etree.HTML(p.b.driver.page_source)
        tree2.findall('.//*[@id="viewProj"]')
        self.stations[i]._batch = tree2.findall('.//*[@id="BatchID"]')[0].text
        self.stations[i].nprojects = tree2.findall('.//*[@id="NoOfProject"]')[0].text
        self.stations[i].disciplines = tree2.findall('.//*[@id="Tag"]')[0].text

    def close_station_detail_modal(self):
        self.b.click(id='panel-close')

    def export_stations_to_pickle_file(self, filename):
        with open('stations_raw1.data', 'wb') as f:
            pickle.dump(self.stations, f)

    def import_stations_from_pickle_file(self, filename):
        with open('stations_raw1.data', 'rb') as f:
            self.stations = pickle.load(f)
        return self.stations

    def reload(self):
        self.b.refresh()

class Station:
    pass


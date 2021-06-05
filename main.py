from decouple import config
from webbot import Browser
from trying5 import PS2Stations



if __name__=='__main__':
    p = PS2Stations()
    p.login()
    p.go_to_stations_list()
    p.update_stations_from_stations_list()
    for i in range(len(p.stations)):
        p.go_to_station_detail_modal(i)
        p.update_stations_list_from_detail_modal(i)
        p.go_to_detail_page(i)
        p.update_stations_and_projects_from_detail_page(i)
        p.close_detail_page()
        p.close_station_detail_modal()
    p.export_stations_to_pickle_file('main2.pkl')

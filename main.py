from decouple import config
from webbot import Browser
from trying4 import PS2Stations


def main():
    p = PS2Stations()
    p.login()
    p.go_to_stations_list()
    p.update_stations_from_stations_list()
    try:
        for i in range(len(p.stations)):
            p.go_to_station_detail_modal(i)
            p.update_stations_list_from_detail_modal(i)
            p.close_station_detail_modal()
    except Exception as e:
        print(e)
    p.export_stations_to_pickle_file('main1.pkl')



if __name__=='__main__':
    main()

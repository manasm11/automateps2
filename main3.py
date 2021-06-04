# IPython log file

# %load main2.py
# IPython log file

from trying5 import *
p = PS2Stations()
p.login()
p.go_to_stations_list()
p.go_to_station_detail_modal(0)
p.close_station_detail_modal()
p.update_stations_from_stations_list()
p.go_to_station_detail_modal(0)
p.update_stations_list_from_detail_modal(0)
p.go_to_detail_page(0)
p.update_stations_and_projects_from_detail_page(0)
p.close_detail_page()
p.close_station_detail_modal()
p.go_to_station_detail_modal(1)
p.update_stations_list_from_detail_modal(1)
p.go_to_detail_page(1)
p.update_stations_and_projects_from_detail_page(1)
p.close_detail_page()
p.close_station_detail_modal()
p.stations[0].projects
#[Out]# [<trying5.Project at 0x7f9d3e8ce668>]
p.stations[2].projects
p.stations[1].projects
#[Out]# [<trying5.Project at 0x7f9d3e9848d0>]
pr = p.stations[1].projects[0]
pr = p.stations[1].projects[0]
pr
#[Out]# <trying5.Project at 0x7f9d3e9848d0>
dir(pr)
#[Out]# ['__class__',
#[Out]#  '__delattr__',
#[Out]#  '__dict__',
#[Out]#  '__dir__',
#[Out]#  '__doc__',
#[Out]#  '__eq__',
#[Out]#  '__format__',
#[Out]#  '__ge__',
#[Out]#  '__getattribute__',
#[Out]#  '__gt__',
#[Out]#  '__hash__',
#[Out]#  '__init__',
#[Out]#  '__init_subclass__',
#[Out]#  '__le__',
#[Out]#  '__lt__',
#[Out]#  '__module__',
#[Out]#  '__ne__',
#[Out]#  '__new__',
#[Out]#  '__reduce__',
#[Out]#  '__reduce_ex__',
#[Out]#  '__repr__',
#[Out]#  '__setattr__',
#[Out]#  '__sizeof__',
#[Out]#  '__str__',
#[Out]#  '__subclasshook__',
#[Out]#  '__weakref__']
# %load main2.py
# IPython log file

from trying5 import *
p = PS2Stations()
p.login()
p.go_to_stations_list()
p.go_to_station_detail_modal(0)
p.close_station_detail_modal()
p.update_stations_from_stations_list()
p.go_to_station_detail_modal(0)
p.update_stations_list_from_detail_modal(0)
p.go_to_detail_page(0)
p.update_stations_and_projects_from_detail_page(0)
p.close_detail_page()
p.close_station_detail_modal()
p.go_to_station_detail_modal(1)
p.update_stations_list_from_detail_modal(1)
p.go_to_detail_page(1)
p.update_stations_and_projects_from_detail_page(1)
p.close_detail_page()
p.close_station_detail_modal()
p.stations[0].projects
#[Out]# [<trying5.Project at 0x7f9d3e8ce668>]
p.stations[1].projects
#[Out]# [<trying5.Project at 0x7f9d3e9848d0>]
pr = p.stations[1].projects[0]
pr = p.stations[1].projects[0]
pr
#[Out]# <trying5.Project at 0x7f9d3e9848d0>
dir(pr)
get_ipython().run_line_magic('save', '--help')
get_ipython().run_line_magic('save', '-h')
get_ipython().run_line_magic('magic', 'save')

from decouple import config
from webbot import Browser


def main():
    b = Browser(browser_executable='brave-browser')
    b.go_to('http://psd.bits-pilani.ac.in/Login.aspx')



if __name__=='__main__':
    main()

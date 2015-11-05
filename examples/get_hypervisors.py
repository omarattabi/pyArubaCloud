import argparse

from ArubaCloud.PyArubaAPI import CloudInterface

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--datacenter', help='Specify datacenter to login.', action='store', dest='dc')
    parser.add_argument('-u', '--username', help='Specify username.', action='store', dest='username')
    parser.add_argument('-w', '--password', help='Specify password.', action='store', dest='password')
    p = parser.parse_args()

    i = CloudInterface(dc=p.dc)
    i.login(username=p.username, password=p.password, load=True)

    i.get_hypervisors()

    from pprint import pprint
    pprint(i.find_template(name='Debian', hv=4))

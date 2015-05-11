__author__ = 'swabyears'
import requests
import json
'''
Test app to change the banner on a Cisco CSR 1000v with the REST API.
'''
def main():

    # CONSTANTS
    base_uri = 'https://192.168.174.132:55443/api/v1/'
    username = 'cisco'
    password = 'cisco'

    r = requests.post(base_uri+'auth/token-services', auth=(username,password), verify=False)
    resp = json.loads(r.text)
    token_expiration = resp['expiry-time']
    token_id = resp['token-id']

    params = {
        "X-Auth-Token" : token_id,
        "Accept" : "application/json",
        "content-type" : "application/json"
    }

    get_banner = requests.request("GET",base_uri+'global/banner',headers=params, verify=False)
    get_banner_json = json.loads(get_banner.content)

    if (get_banner_json['exec']==''):
        data = '{"exec" : "MOTD dudes!"}'
        put_banner = requests.request("PUT",base_uri+'global/banner',data=data, headers=params, verify=False)

        if put_banner.status_code == 204:
            print 'Exec banner set.'
    else:
        print 'Exec banner already set.'

if __name__ == "__main__":
    main()



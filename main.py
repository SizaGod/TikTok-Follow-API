import requests
from Gorgon import Gorgon
from Argus import Argus
from Ladon import Ladon
from urllib.parse import urlencode
import time
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "v04.04.05-ov-android", sdk_version: int = 134744640, platform: int = 0, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = int(time.time())
    
        return Gorgon(params, unix, payload, cookie).get_value() | { 
            "x-ladon"   : Ladon.encrypt(unix, license_id, aid),
            "x-argus"   : Argus.get_sign(params, x_ss_stub, unix,
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )
        }
def base_params():
        global iid,did,uid,secuid
        return {
  'user_id': uid,
  'sec_user_id': secuid,
  'type': "1",
  'channel_id': "0",
  'from': "13",
  'from_pre': "13",
  'item_id': "7420915643500825861",
  'enter_from': "homepage_hot",
  'action_time': "1735088222318",
  'is_network_available': "true",
  'device_platform': "android",
  'os': "android",
  'ssmix': "a",
  '_rticket': "1735088222332",
  'cdid': "7d846037-255f-440b-8552-b870aa4f8095",
  'channel': "googleplay",
  'aid': "1233",
  'app_name': "musical_ly",
  'version_code': "370805",
  'version_name': "37.8.5",
  'manifest_version_code': "2023708050",
  'update_version_code': "2023708050",
  'ab_version': "37.8.5",
  'resolution': "720*1280",
  'dpi': "240",
  'device_type': "SM-G935F",
  'device_brand': "samsung",
  'language': "en",
  'os_api': "28",
  'os_version': "9",
  'ac': "wifi",
  'is_pad': "0",
  'current_region': "CA",
  'app_type': "normal",
  'sys_region': "US",
  'last_install_time': "1734987222",
  'mcc_mnc': "60302",
  'timezone_name': "Africa/Algiers",
  'residence': "CA",
  'app_language': "en",
  'carrier_region': "CA",
  'timezone_offset': "3600",
  'host_abi': "arm64-v8a",
  'locale': "en",
  'content_language': "en",
  'ac2': "wifi",
  'uoo': "0",
  'op_region': "CA",
  'build_number': "37.8.5",
  'region': "US",
  'ts': "1735088222",
  'iid':iid,
  'device_id':did,
  'openudid': "35952731903405ea"
        }
def algo():
 global iid,did,uid,secuid
 params = base_params()
 return sign(urlencode(params))
cook="sessionid="
iid='7389856192924976902'
did='7389854904419223045'
uid='7065740413541712902'
secuid='MS4wLjABAAAAr5U_HUg-SS9ieJv-ZayCTZIzRsVNjM9xnUfJg7JPNk_fW-R0xuL7OhobYy267-v-'
url = "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/commit/follow/user/"
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; fr; SM-G935F; Build/PI;tt-ok/3.12.13.16)",
  'Accept-Encoding': "gzip",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-tt-pba-enable': "1",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket': "1735088222336",
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
  'tt-ticket-guard-version': "3",
  'passport-sdk-version': "6031990",
  'oec-vc-sdk-version': "3.0.5.i18n",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-request-tag': "n=0;nr=011;bg=0",
  'x-tt-store-region': "ca",
  'x-tt-store-region-src': "uid",
  'x-tt-pba-enable': "1",
  'x-argus':algo()['x-argus'],
  'x-gorgon': algo()['x-gorgon'],
  'x-khronos':algo()['x-khronos'],
  'x-ladon':algo()['x-ladon'],
  'Cookie': cook
}
response = requests.get(url, params=urlencode(base_params()), headers=headers)
print(response.json())

"""
Project : xixunyun-sign
Author  : Womsxd
License : GNU Affero General Public License v3.0
GitHub  : https://github.com/Womsxd/xixunyun-sign
"""


# 获取Openssl版本
def get_openssl_version() -> int:
    try:
        import ssl
    except ImportError:
        from loghelper import log
        log.error("Openssl Lib Error !!")
        # return -99
        # 建议直接更新Python的版本，有特殊情况请提交issues
        exit(-1)
    temp_list = ssl.OPENSSL_VERSION_INFO
    return int(f"{str(temp_list[0])}{str(temp_list[1])}{str(temp_list[2])}")


try:
    # 优先使用httpx，在httpx无法使用的环境下使用requests
    import httpx

    http = httpx.Client(timeout=10, transport=httpx.HTTPTransport(retries=5))
    # 当openssl版本小于1.0.2的时候直接进行一个空请求让httpx报错
    if get_openssl_version() <= 102:
        httpx.get()
except:
    import requests
    from requests.adapters import HTTPAdapter

    http = requests.Session()
    http.mount('http://', HTTPAdapter(max_retries=5))
    http.mount('https://', HTTPAdapter(max_retries=5))

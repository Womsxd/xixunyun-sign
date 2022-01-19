"""
Project : xixunyun-sign
Author  : Womsxd
License : GNU Affero General Public License v3.0
GitHub  : https://github.com/Womsxd/xixunyun-sign
"""
import rsa
import json
import httpx
import base64
import random

rsa_public_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlYsiV3DsG" \
                 "+t8OFMLyhdmG2P2J4GJwmwb1rKKcDZmTxEphPiYTeFIg4IFEiqDCA" \
                 "TAPHs8UHypphZTK6LlzANyTzl9LjQS6BYVQk81LhQ29dxyrXgwkRw9RdWa" \
                 "MPtcXRD4h6ovx6FQjwQlBM5vaHaJOHhEorHOSyd/deTvcS+hRSQIDAQAB\n-----END PUBLIC KEY-----"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "okhttp/3.8.1",
}


def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        temp = json.load(f)
        f.close()
    return temp


def public_encrypt(raw_data):
    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(rsa_public_key)
    base46_enc = base64.b64encode(rsa.encrypt(raw_data.encode('utf-8'), pub_key))
    return base46_enc.decode('utf-8')


def login():
    req = httpx.post(
        url="https://api.xixunyun.com/login/api?from=app&version="
            "{}&platform=android&entrance_year=0&graduate_year=0&school_id={}".format(
                config["app_version"], config["school_id"]),
        data={
            "app_version": config["app_version"],
            "request_source": 3,
            "platform": 2,
            "mac": "FF:FF:FF:FF:FF:FF",
            "password": config["password"],
            "system": config["system"],
            "school_id": config["school_id"],
            "model": "11514",
            "app_id": "cn.vanber.xixunyun.saas",
            "account": config["account"],
            "key": ""},
        headers=headers
    )
    data = req.json()
    if data["code"] != 20000:
        print("账号/密码/学校错误！")
        exit(1)
    return data["data"]["token"]


def day_signing(token):
    req = httpx.post(
        url="https://api.xixunyun.com/signin_rsa?token={}&from=app&version="
            "{}&platform=android&entrance_year=0&graduate_year=0&school_id={}".format(
                token, config["app_version"], config["school_id"]),
        data={
            "address": config["address"],
            "latitude": public_encrypt(config["latitude"]+str(random.randint(10, 99))),
            "remark": 0,
            "comment": "",
            "address_name": config["address_name"],
            "change_sign_resource": 0,
            "longitude": public_encrypt(config["longitude"]+str(random.randint(10, 99)))},
        headers=headers
    )
    return req.json()


def signing_result_to_message(result):
    if result["code"] != 20000:
        return "签到失败！\n"+result
    return "签到成功，获得{}个积分，已签到{}天".format(result["data"]["point"], result["data"]["continuous"])


config = load_config()
token = login()
result = day_signing(token)
message = signing_result_to_message(result)
print(message)

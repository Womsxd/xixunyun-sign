# 签到配置文件相关说明

## 登入信息配置

```json
"account": "",
"password": ""
"school_id": ""
"app_version": "4.6.2"
"system": "9"
```

### 账号和密码

`account`和`password`分别代表账号和密码，填入即可

### 学校ID

`school_id`表示学校id，请自行获取后填入即可

### 信息模拟

`app_version`和`system`分别代表习讯云版本和手机的系统版本，默认模拟4.6.2版本的习讯云和安卓9

## 健康日报相关功能

```json
"health": {
        "enable": true,
        "health_type": 1,
        "code": 2,
        "vaccin": 2,
        "strong": 1,
        "high-risk_areas": 0,
        "ill": 0,
        "family_name": "",
        "family_phone": ""
    }
```

### 如何启用/关闭

```json
"enable": true
```

将`enable`的值改为`true`即为启用，改为`false`即为关闭

### 健康状态

```json
"health_type": 1
```

可填入`1`和`2`两个值，`1`代表健康，`2`代表有**发烧、咳嗽等症状**

### 健康码

```json
"code": 2
```

可以填入`2`、`3`、`4`三个值 **(没有1)**，分别代表**绿码**，黄码，红码

### 是否接种疫苗(不包含加强针)

```json
"vaccin": 2
```

可以填入`1`、`2`两个值，分别代表**未接种**和接种

### 是否接种加强针

```json
"strong": 1
```

可以填入`1`、`2`两个值，分别代表**未接种**和接种

### 14天内是否去过高风险地区

```json
"high-risk_areas": 0
```

可以填入`0`或`1`两个值，分别代表**没去过高风险地区**和**去过高风险地区**

### 是否接触过疑似或确诊新冠患者

```json
"ill": 0
```

可以填入`0`或`1`两个值，分别代表**没接触**和**接触**

### 家庭紧急联系人

```json
"family_name": "",
"family_phone": ""
```

分别填入姓名和手机号

## 自动打卡相关功能设置

已改入子配置，请看子配置里面的自动打卡

## 指定需要启用的子配置

```json
"config_list": ["default"]
```

通过修改这个值可以设置多个子配置

示例(2个，3个或者更多)：

```json
"config_list": ["name1","name2"]
"config_list": ["name1","name2","name3"]
"config_list": ["name1","name2","name3",……"name n"]
```

## 设置子配置

```json

    "use_day" : ["1","2","3","4","5"],
    "sign": {
        "address": "",
        "address_name": "",
        "latitude": "",
        "longitude": "",
        "remark": 9
    },
    "health": {
        "state": 3 
    }
}
```

### 子配置名称

```json
"default": {
```

此处为子配置的名称配置，可根据喜好自行设置

### 使用配置的日期

```json
"use_day" : ["1","2","3","4","5"],
```

指定星期几使用此子配置

### 自动打卡

```json
"sign": {
    "address": "",
    "address_name": "",
    "latitude": "",
    "longitude": "",
    "remark": 9
}
```

#### 打卡地址和名称

```json
"address": "",
"address_name": ""
```

填入打卡的具体地址和打卡地址的名称

示例：

```json
"address": "浙江省杭州市萧山区空港大道1号",
"address_name": "杭州萧山国际机场"
```

#### 打卡地址的坐标

```json
"latitude": "",
"longitude": "",
```

填入打卡地址的坐标，只保留小数点后四位，脚本会随机填充两位进入

获取地址[坐标拾取器 - 高德开放平台](https://lbs.amap.com/tools/picker)

示例：

获取到的杭州萧山国际机场的坐标为：120.432414,30.234708

```json
"latitude": "30.2347",
"longitude": "120.4324",
```

#### 打卡备注

```json
"remark": 9
```

可以填入0-11中的任意一个值，分别代表：上班、因公外出、假期、请假、轮岗、回校、外宿、在家、下班、学习、毕业设计、院区轮转

### 健康日报其他设置

```json
"health": {
    "state": 3 
}
```

只有一个`state`参数，可以填入1-5，分别代表：上班在岗、在家、在学校、居家隔离、集中隔离

## 示例配置文件

下面模拟的情况为**凭空捏造**，如有雷同，**请勿当真**

文件名为`demo.json`，模拟了一个在1、3、5在浙江大学上学，2、4在萧山国际机场上班，6、7在家休息的实习生

# CV_Classification

����ǰ���ն�λ������CV_Classification������mymain.py


ͼ���ϴ������з��࣬ǰ��ͨ������������ɿ��ӻ�����

ת�Ӱ�ԭ��ͼhttps://content.arduino.cc/assets/MachineLearningCarrierV1.0.pdf

ͼ��ߴ�ΪQCIF��v2��׺�ߴ�ΪQVGA

## ͼ�����

�ο���https://github.com/chestnut24/SVMImageClassification

## �ϴ�

Ԥ��·�������������ϴ����ء���>wifi�����ϴ����ء���>wifi�ϴ��ƶ�

�ϴ������У��ϴ���ͼƬ��������SVMImageClassification/test_photo��

### ���������ϴ�����

arduino�ĳ���Ϊtest_camera.ino

��arduino��¼���������com_upload.py�����°�ť������һ�����պ��ϴ�ͼƬ��com_upload.py���к��һֱѭ��

### wifi�����ϴ�����

arduino�ĳ���Ϊwifi_upload.ino

esp-01���ͻ��ˣ�PC������������ͨ��TCPЭ�鴫������

��arduino��¼���������wifi_upload.py�����°�ť������һ�����պ��ϴ�ͼƬ��wifi_upload.py���к��һֱѭ��

arduino��esp-01�Ĵ���ͨ�Ų������ڵ���ʽ

## ǰ��


## �������ĵ�

arduino nano 33 ble�����棬����ʱ������ʹ��vscode��¼�����Ĵ��ڻ��

ov7675�ܵ�Ÿ��ź�����

��tinymlsheldͷ�ļ��и�������ͷ��IO�����ӣ��ڵ�·���öŰ��߸��ģ�������ͼ�����֣���ȷ���Ƿ�Ҳ���ܵ�Ÿ���Ӱ��

arduino nano 33 ble�޷�ʹ��SoftwareSerial����������ʹ��UART��

```
UART softSerial2(digitalPinToPinName(1), digitalPinToPinName(0), NC, NC);
```

�����뿪��1�ź�0�������ڣ�Ϊʲô��1�ź�0��Ҳ�ܽ��д����շ����벻����

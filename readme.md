# CV_Classification

����mymain.py

ͼ��������ϴ������з��࣬ǰ��ͨ������������ɿ��ӻ�����

## ת�Ӱ�

[�����ĵ�](https://xn4zlkzg4p.feishu.cn/wiki/DSxzwSo8iiLLURkXnTMca9K1nwh?from=from_copylink)

�ٷ�ת�Ӱ�ԭ��ͼ [�ٷ�](https://content.arduino.cc/assets/MachineLearningCarrierV1.0.pdf)

����ת�Ӱ� [����](https://pro.lceda.cn/editor#id=f7357ab4b7e142e686c2cabcdf9fad5d)

## ͼ�����

�ο��� [SVMImageClassification](https://github.com/chestnut24/SVMImageClassification)

## ��������

[��������](https://xn4zlkzg4p.feishu.cn/wiki/Ftn9wbrffiWQCpkAhVVcfoKCn7d?from=from_copylink)

�ο�Edge Impulse��վ����������̳̣�ѵ���󵼳��⣬arduinoֱ�Ӽ�������������ϴ�

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

[ǰ��](https://xn4zlkzg4p.feishu.cn/wiki/MMwnwaufji8mv3kawXqcMhXpn4b?from=from_copylink)

pyQT��������txt����ȫ�������ݿ��У�����ʾ����

## ����Ҫ����

arduino nano 33 ble�����棬����ʱ������ʹ��vscode��¼�����Ĵ��ڻ��

ov7675�Ĺٷ�ת�Ӱ�ԭ��ͼD10��D1���߷��ˣ�layout�ǶԵ�

��tinymlsheldͷ�ļ��и�������ͷ��IO�����ӣ��ڵ�·���öŰ��߸��ģ�������ͼ�����֣���ȷ���Ƿ�Ҳ���ܵ�Ÿ���Ӱ��

arduino nano 33 ble�޷�ʹ��SoftwareSerial����������ʹ��UART��

```
UART softSerial2(digitalPinToPinName(2), digitalPinToPinName(0), NC, NC);
```

�����뿪��2�ź�0�������ڣ�Ϊʲô��1�ź�0��Ҳ�ܽ��д����շ����벻����

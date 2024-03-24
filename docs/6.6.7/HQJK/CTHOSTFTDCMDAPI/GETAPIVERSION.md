<p>获取API的版本信息</p>
<span class="anchor" id="1cca618f-bbf9-4225-8d32-15d7cd45bbf4"></span>
## 1.函数原型
<p>virtual const char * <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/GETAPIVERSION/">GetApiVersion</a> () = 0;</p>
<span class="anchor" id="ca11b150-462a-4a58-8d4d-ce3a6fb7e675"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="51d5ab2c-9ce7-4a53-af06-b08eca9ec4e6"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="efa1757c-e663-4b0b-aeee-3a53b7ff0bb6"></span>
## 4.FAQ
<p>无</p>

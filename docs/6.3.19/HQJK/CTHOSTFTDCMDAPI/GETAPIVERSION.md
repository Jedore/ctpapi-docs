<p>获取API的版本信息</p>
<span class="anchor" id="1fdfbc7a-ea18-4f3e-97b3-ede4d3f1339e"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="58ac2bbc-6818-4e96-bf5c-2163cc86f35a"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="984b0e7b-0241-4ac4-b730-3f9d7a3ef291"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="f58d9b35-609f-4313-b0dd-f2888e32eb57"></span>
## 4.FAQ
<p>无</p>

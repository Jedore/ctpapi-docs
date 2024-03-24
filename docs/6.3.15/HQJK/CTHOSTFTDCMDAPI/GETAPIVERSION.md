<p>获取API的版本信息</p>
<span class="anchor" id="20ceae9b-f045-4b7c-88d3-aac6ee8283fd"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="47225106-6441-467b-92d1-dfca3e06782d"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="92b54f9f-1eb6-464e-ae88-2c9f26fa916f"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="de0eb2f6-ffab-4a0b-ae37-01f3e8d96824"></span>
## 4.FAQ
<p>无</p>

<p>获取API的版本信息</p>
<span class="anchor" id="314f9fe1-0464-4cd6-aa82-49c1be7f5aa7"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="c7616f11-9def-4929-85e2-520079b83bbd"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="03b54b17-f23a-4739-9cf8-831468a255ce"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="19145f7b-b45f-4af3-b352-5ae2e85d2bd0"></span>
## 4.FAQ
<p>无</p>

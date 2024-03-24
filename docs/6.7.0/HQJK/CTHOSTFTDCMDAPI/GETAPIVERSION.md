<p>获取API的版本信息</p>
<span class="anchor" id="1be989f3-11dc-4fea-974b-2c09ae0c985a"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="d0769577-0a66-41ef-87b3-dfc51ce041c4"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="1cd5b96e-b5d1-4594-ba03-a2026f77a30b"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="9eaf74a0-e1b1-4f6b-9595-6dd35e5b21cd"></span>
## 4.FAQ
<p>无</p>

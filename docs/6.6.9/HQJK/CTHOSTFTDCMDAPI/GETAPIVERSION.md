<p>获取API的版本信息</p>
<span class="anchor" id="43f95529-82e2-4c67-95dc-fa89eb02656e"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="46590472-ae38-463d-be73-bc7987f62b15"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="46d88dde-32c7-4bc3-9187-50911c0d6785"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="59d4d542-287c-4da3-8493-b3a5090cd250"></span>
## 4.FAQ
<p>无</p>

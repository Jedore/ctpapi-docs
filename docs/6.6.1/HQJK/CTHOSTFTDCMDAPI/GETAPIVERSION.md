<p>获取API的版本信息</p>
<span class="anchor" id="e38a52bf-9f3d-4ca9-addf-003a5d60a77f"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="3c32598a-6078-44f6-b9a3-0bbe736bedcd"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="d6bb8eb8-7969-4b60-aa4e-98ea4229c1f9"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="775c8472-4315-4db6-b354-b12a6b047a48"></span>
## 4.FAQ
<p>无</p>

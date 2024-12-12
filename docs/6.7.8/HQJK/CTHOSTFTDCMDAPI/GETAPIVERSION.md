<p>获取API的版本信息</p>
<span class="anchor" id="c7d97174-8b79-49c7-8368-f92c9d471874"></span>
## 1.函数原型
<p>virtual const char * GetApiVersion () = 0;</p>
<span class="anchor" id="83386194-de3c-4495-9853-dc044c61bb58"></span>
## 2.返回
<p>const char * 返回一个指向版本字符串的指针</p>
<span class="anchor" id="a8e7d0bb-eae5-47a4-b562-057e9887a53b"></span>
## 3.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
printf("版本号为:%s\n", pUserMdApi-&gt;GetApiVersion());
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
pUserMdApi-&gt;RegisterFront(“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="c64cb6c9-ee68-4078-b9ff-9edf98fcf5ae"></span>
## 4.FAQ
<p>无</p>

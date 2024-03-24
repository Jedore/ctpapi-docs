<p>获取API的版本信息</p>
<span class="anchor" id="0345d205-48ba-430b-9f2c-e936bb257e2f"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETAPIVERSION/">GetApiVersion</a>() = 0;</p>
<span class="anchor" id="d9ba504a-d763-4687-93c8-49b052b5c602"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="654ca15d-5076-44a8-8a5a-82e4c8bb4531"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="2540311e-869e-4794-a1aa-7a927f7b2123"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
LOG(pUserApi-&gt;GetApiVersion());
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="24465fff-a7f4-4726-880b-88f524bd95a0"></span>
## 5.FAQ
<p>无</p>

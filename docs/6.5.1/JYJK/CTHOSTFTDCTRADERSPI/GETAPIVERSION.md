<p>获取API的版本信息</p>
<span class="anchor" id="b52d7f2e-80b1-44a4-8f23-0a4a6610d353"></span>
## 1.函数原型
<p>virtual const char *GetApiVersion() = 0;</p>
<span class="anchor" id="062414cf-ccba-4f49-89bc-ace981aa4a20"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="db92a023-bcc8-4484-88e9-399d8fbb67bf"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="e0a01aa3-fe7c-42d1-9800-53b94dc7ed05"></span>
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
<span class="anchor" id="71648c6a-d80e-4066-bf80-3ffb66574399"></span>
## 5.FAQ
<p>无</p>

<p>获取API的版本信息</p>
<span class="anchor" id="696206b6-9a55-469b-b426-2f5843f5910a"></span>
## 1.函数原型
<p>virtual const char *GetApiVersion() = 0;</p>
<span class="anchor" id="0e73e504-77f2-46a4-b5ed-769f42661b89"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="eb073bce-ddb2-417b-bce7-ca10ff774b60"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="dea4b8c2-92a7-471d-a3d6-82accf78fbb2"></span>
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
<span class="anchor" id="c9fed91b-7cc5-4dbc-91d4-db253e78269a"></span>
## 5.FAQ
<p>无</p>

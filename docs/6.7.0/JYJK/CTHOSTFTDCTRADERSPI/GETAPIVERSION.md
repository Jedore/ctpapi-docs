<p>获取API的版本信息</p>
<span class="anchor" id="32ee218d-cf84-4df7-9fe8-27940059be49"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETAPIVERSION/">GetApiVersion</a>() = 0;</p>
<span class="anchor" id="dfd1d0d3-873e-40ca-b3f9-47c7860661ed"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="b36d08de-69bd-4f7f-bf0d-a47964b24a6a"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="2689e134-365a-4a48-8ee9-01e32689075f"></span>
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
<span class="anchor" id="67bd3d5a-37e5-4b1a-af25-c9cf5fb159eb"></span>
## 5.FAQ
<p>无</p>

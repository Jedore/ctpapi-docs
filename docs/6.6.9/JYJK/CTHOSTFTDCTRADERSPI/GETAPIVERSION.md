<p>获取API的版本信息</p>
<span class="anchor" id="2b57c5fd-c784-489a-8e64-00a80a079c98"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETAPIVERSION/">GetApiVersion</a>() = 0;</p>
<span class="anchor" id="30b444a2-4dc9-461f-8474-fb9781f49b42"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="8b79ab05-c44f-44e8-bea7-29eed303589b"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="668f5893-24d5-4ada-ab89-995bf7a6de67"></span>
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
<span class="anchor" id="98615706-64ce-43ee-9d7b-1d9685563e05"></span>
## 5.FAQ
<p>无</p>

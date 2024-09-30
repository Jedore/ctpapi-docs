<p>获取API的版本信息</p>
<span class="anchor" id="541cf247-b33d-43bb-bfcb-46e8c8d6909e"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETAPIVERSION/">GetApiVersion</a>() = 0;</p>
<span class="anchor" id="26c51d56-d52b-4a18-a9fd-1a25d09cdab7"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="b3e1654d-8426-43d9-ad29-b9ef3559d73d"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="e2084926-9e23-49fd-9c50-a3437127ffac"></span>
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
<span class="anchor" id="8c36f75d-f668-4ce1-a675-c4478a0634ec"></span>
## 5.FAQ
<p>无</p>

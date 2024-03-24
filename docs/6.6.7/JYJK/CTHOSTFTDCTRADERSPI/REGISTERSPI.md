<p>注册一个派生自<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="5cd1c9e1-bc3f-430b-8117-7aa402115a6c"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERSPI/">RegisterSpi</a>(<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> *pSpi) = 0;</p>
<span class="anchor" id="c4baf8fb-d2bd-4542-85b5-7f6a06a7e4a3"></span>
## 2.参数
<p>pSpi：实现了<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>接口的实例指针。</p>
<span class="anchor" id="ed1a8d15-f70c-450e-baff-2e12752aaea5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2dbc0489-0662-40b8-9b72-1bad8a55dd44"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="41a21a30-f525-49b6-b2be-171731947342"></span>
## 5.FAQ
<p>无</p>

<p>注册一个派生自<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="d9d2d25b-8ab2-4850-b530-180f0ec1ab1b"></span>
## 1.函数原型
<p>virtual void RegisterSpi(<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> *pSpi) = 0;</p>
<span class="anchor" id="2c336b73-8ee0-4046-8a52-7c9ac9ffb9c0"></span>
## 2.参数
<p>pSpi：实现了<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>接口的实例指针。</p>
<span class="anchor" id="71b934b4-e77e-4355-b1b0-912142926496"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="92e9a9ce-df31-4966-945f-4dc4831947ac"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="46d69858-7bfe-4b0b-8b1b-0213d925bb08"></span>
## 5.FAQ
<p>无</p>

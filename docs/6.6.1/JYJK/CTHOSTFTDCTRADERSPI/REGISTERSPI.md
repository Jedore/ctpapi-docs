<p>注册一个派生自<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="63440ba5-2dfd-407c-8b26-6c6e1719b00a"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERSPI/">RegisterSpi</a>(<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> *pSpi) = 0;</p>
<span class="anchor" id="a01684b2-e1b6-45dd-8d7f-aa549893b156"></span>
## 2.参数
<p>pSpi：实现了<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>接口的实例指针。</p>
<span class="anchor" id="f6df0e88-a8cb-4d7f-9fb1-731bbf0316ff"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="391a3746-725d-470b-b325-a8691a7bf02b"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="776e499e-82a9-4a43-b027-995af006f9eb"></span>
## 5.FAQ
<p>无</p>

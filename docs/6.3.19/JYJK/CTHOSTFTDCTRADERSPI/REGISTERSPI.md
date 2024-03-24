<p>注册一个派生自CThostFtdcTraderSpi 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="79ba4d3e-f1de-40c9-ab7a-c3cf1abf74fe"></span>
## 1.函数原型
<p>virtual void RegisterSpi(CThostFtdcTraderSpi *pSpi) = 0;</p>
<span class="anchor" id="463f3048-6408-43fd-a696-56a6c75bcf86"></span>
## 2.参数
<p>pSpi：实现了CThostFtdcTraderSpi接口的实例指针。</p>
<span class="anchor" id="9661485b-0730-4ff8-bd3a-3aa843ea6c1e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3ec4cec1-de1b-4eb1-9bb8-266b2c6f3322"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="dcdcbef4-1ebc-45d9-959c-1914b678107b"></span>
## 5.FAQ
<p>无</p>

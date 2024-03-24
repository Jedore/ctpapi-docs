<p>注册一个派生自CThostFtdcTraderSpi 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="a06ff348-2b5f-4af3-ac00-df96f79b2020"></span>
## 1.函数原型
<p>virtual void RegisterSpi(CThostFtdcTraderSpi *pSpi) = 0;</p>
<span class="anchor" id="efc6d21d-8cac-4f0a-a4d7-718c650e58be"></span>
## 2.参数
<p>pSpi：实现了CThostFtdcTraderSpi接口的实例指针。</p>
<span class="anchor" id="8c4d64da-9502-4989-9fad-128b51c8c172"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="eb55969c-ecac-4eb5-af46-1978d23965a0"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="3ccb3dd9-28de-4f8b-a5fb-918b0af897cd"></span>
## 5.FAQ
<p>无</p>

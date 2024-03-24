<p>注册一个派生自CThostFtdcTraderSpi 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="40421bfb-71d3-4afe-98d7-bdf2cdb285b7"></span>
## 1.函数原型
<p>virtual void RegisterSpi(CThostFtdcTraderSpi *pSpi) = 0;</p>
<span class="anchor" id="4db87a26-cc09-4349-935a-53d36dd2fbe4"></span>
## 2.参数
<p>pSpi：实现了CThostFtdcTraderSpi接口的实例指针。</p>
<span class="anchor" id="3c54c4a0-d18c-4d37-9b75-a15a713b2e94"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ed096db6-2822-476d-8f3e-9671a2d00f6a"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="e6ad0415-d90b-4aed-9392-5dd47225917e"></span>
## 5.FAQ
<p>无</p>

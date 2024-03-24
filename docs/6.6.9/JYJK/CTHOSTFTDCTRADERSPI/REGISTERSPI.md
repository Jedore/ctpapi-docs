<p>注册一个派生自<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="21b42b17-ea67-4124-b6eb-69fb0b2c9faf"></span>
## 1.函数原型
<p>virtual void RegisterSpi(<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> *pSpi) = 0;</p>
<span class="anchor" id="96ba9e55-35e2-4a50-83a2-21924799e4fe"></span>
## 2.参数
<p>pSpi：实现了<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>接口的实例指针。</p>
<span class="anchor" id="d1f5c507-2343-4fb1-aa27-286ae30505ae"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bc85f65e-bcd7-412a-b5d0-220dfc440a51"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="9aceb71d-2952-4523-a2ad-bffb7fc1f0eb"></span>
## 5.FAQ
<p>无</p>

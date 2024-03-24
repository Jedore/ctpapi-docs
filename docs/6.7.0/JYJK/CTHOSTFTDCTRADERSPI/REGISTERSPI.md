<p>注册一个派生自<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> 接口类的实例，该实例将完成事件处理。</p>
<span class="anchor" id="326af7b5-14a5-4dda-8536-d09ff0d22bb6"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERSPI/">RegisterSpi</a>(<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a> *pSpi) = 0;</p>
<span class="anchor" id="5ff0a645-894a-43e2-ade4-eca460da85cd"></span>
## 2.参数
<p>pSpi：实现了<a href="../../CTHOSTFTDCTRADERAPI/_CTHOSTFTDCTRADERAPI/">CThostFtdcTraderSpi</a>接口的实例指针。</p>
<span class="anchor" id="361e69da-3481-495d-bf4b-e14d9504c5d6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="caf81232-f3ae-48ac-97fa-18a3ee0ec051"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\api_liu\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="89c35fa2-0cdb-49ae-8a9e-11bd4a943b5b"></span>
## 5.FAQ
<p>无</p>

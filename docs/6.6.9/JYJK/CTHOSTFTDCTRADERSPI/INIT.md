<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="d1907ebf-5b2d-413a-9b96-b9d9c10dfbaa"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="2593ee50-1f75-4a2e-8b93-f82de5ca5da0"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="720e8464-cdcb-486a-bf68-71dec292dfe7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d44fcc1c-8ed2-4a54-ab81-dd53ef03a262"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="52764352-6e93-4cac-bc38-5edffa06bd74"></span>
## 5.FAQ
<p>无</p>

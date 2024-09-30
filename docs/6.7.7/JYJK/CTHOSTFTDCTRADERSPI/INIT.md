<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="95996f80-401d-4be1-88b7-c61bcd4c5f83"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="8bab93db-9633-4d17-8c6b-6d176e896947"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="eaa09977-c9c8-4f7a-8e4e-5beaa243af57"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ea34f9af-71f5-4555-9a76-6010d838955e"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="087fe875-b822-4a34-9bca-38a676178dde"></span>
## 5.FAQ
<p>无</p>

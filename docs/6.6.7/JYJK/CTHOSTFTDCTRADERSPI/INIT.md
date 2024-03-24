<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="4afcd2b9-19f9-456d-bab4-822f8ea58cbf"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="603c2dc3-d0a6-43c5-9747-bc182362abc1"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="c89fdc4b-aa97-41df-a063-f3754927bd81"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3e3e0999-9191-4f01-97e4-30a0a16cfde4"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="d08e3854-19d3-47d0-b79c-9eee59805890"></span>
## 5.FAQ
<p>无</p>

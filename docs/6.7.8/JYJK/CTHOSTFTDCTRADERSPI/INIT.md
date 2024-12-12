<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="72b47bda-80ff-42c1-b7af-048dd229a4cf"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="bb61fbfb-e571-4d9d-be87-d5d803f03e5b"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="8c08e247-065a-49af-bcb5-95415e24c322"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b1729ae4-84ca-4b68-a9f4-41d19f3b633c"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="c72d36db-3f1b-4e6f-b78a-cba993c8ed44"></span>
## 5.FAQ
<p>无</p>

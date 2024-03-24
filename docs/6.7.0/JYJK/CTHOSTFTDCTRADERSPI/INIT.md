<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="cc9174c7-ccca-4536-9e50-04bedea59a35"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="14792e82-500a-4b76-9573-633f32167d1e"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="0ff0528c-62fa-471e-b0d6-41de31e7a31b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6c9d0c86-6ba4-47b0-b124-f58aa28785aa"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="86198fb4-f866-446a-81c7-4c43d9594ea0"></span>
## 5.FAQ
<p>无</p>

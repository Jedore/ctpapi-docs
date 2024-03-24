<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="ac4b4b29-f007-4269-8567-6e141328d51d"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="8f0d83e2-128d-4c88-87fa-8b4d3ced5d34"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="f64766a3-4958-45dc-9e0e-16f89db9e25e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="06070455-5ad7-4a89-9e6c-1c7d10aa08b8"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="a500a9f3-ac26-42c2-be9e-c423bad35a38"></span>
## 5.FAQ
<p>无</p>

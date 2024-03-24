<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="1e695f71-4018-4954-b58f-1b0741671412"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="c887ac45-ac96-4b47-9a78-55a1610d0848"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="50aa336e-92b5-4480-bf1f-b07961214da1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3b7a7073-3156-40a1-9730-d837188ab6ef"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="c40e5f15-27c6-464e-9770-d61723fcfa86"></span>
## 5.FAQ
<p>无</p>

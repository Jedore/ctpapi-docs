<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="85955e9b-5b76-4366-8448-233365d0aa82"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="14c4a257-d8d1-49dc-9dc3-6ce41976e502"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="803518eb-734d-4fe2-a3e8-56d0a22c54db"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6f0a3b00-6aab-4771-80c6-7e1467ab9df9"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="1fd4480a-4dbe-41cc-ba3a-90547e98a6dc"></span>
## 5.FAQ
<p>无</p>

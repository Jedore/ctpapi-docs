<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<span class="anchor" id="124ca660-9ac9-4cbc-b45d-5d53821e8164"></span>
## 1.函数原型
<p>virtual void Init() = 0;</p>
<span class="anchor" id="9c1b5b5a-86b4-4e04-8298-cd3a8410a85e"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="d01dab38-3055-455f-a5c3-7362f2a3fc85"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c11d76a6-afd6-4465-98d0-1d2b3a44431e"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="e017fe08-5d9f-4418-b0b4-ff850d93bba0"></span>
## 5.FAQ
<p>无</p>

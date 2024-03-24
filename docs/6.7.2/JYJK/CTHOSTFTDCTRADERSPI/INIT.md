<p>使客户端开始与交易托管系统建立连接，连接成功后可以进行登陆。</p>
<p>非线程安全，多线程使用请加锁。</p>
<span class="anchor" id="a4c9c32b-2e07-49d3-9ce9-00e7143e0b34"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a>() = 0;</p>
<span class="anchor" id="6ebbe60d-bc86-4505-bee7-6e40bd5598c7"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="7afb9b54-5678-4809-8ed5-31e278ef291b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="64c40919-4311-466e-9f37-4c00bc9b107f"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="a2bc6cca-fc45-41e0-a3ae-aba7b65d9984"></span>
## 5.FAQ
<p>无</p>

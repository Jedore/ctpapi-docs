<p>订阅公共流。该方法要在Init 方法前调用。若不调用则不会收到公共流的数据。</p>
<span class="anchor" id="54f99165-65af-4f61-8f3b-8237e5a67dd9"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST<em>TE</em>RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="836d1305-b3f4-4169-9e66-6a52c6318582"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
</blockquote>
<span class="anchor" id="337ce5af-57b6-4d22-9006-a633f9543d15"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d00c2982-65e5-465c-9212-cc5b274b5d6a"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="7e5e2785-602a-4b81-81e6-f7a5c23a6f1a"></span>
## 5.FAQ
<p>无</p>

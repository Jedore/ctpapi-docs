<p>订阅公共流。该方法要在Init 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="9c0e4bd4-dbd3-44e7-b9eb-c316ab7b7e21"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="f810533e-0e48-4c9f-b8ab-96a890fd6813"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
</blockquote>
<span class="anchor" id="b6ab92ba-e102-41b9-98b3-5e289ae62343"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="00e0a1b1-9e0c-479e-a8a8-192ee1399bc1"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="b209942a-3b8f-4b87-b405-cea44ad28da4"></span>
## 5.FAQ
<p>无</p>

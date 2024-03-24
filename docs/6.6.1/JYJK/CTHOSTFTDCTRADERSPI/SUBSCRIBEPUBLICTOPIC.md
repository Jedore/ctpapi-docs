<p>订阅公共流。该方法要在<a href="../INIT/">Init</a> 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="95cc78c4-1838-492f-badc-6a879f504edf"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="792c0cc1-c503-413c-8a24-3f23ca7204b9"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
<p>THOST_TERT_NONE：取消订阅公有流</p>
</blockquote>
<span class="anchor" id="cc1d2479-8a0e-4595-ae2d-707c6e22a2ed"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2c1446c4-76bc-43cb-8e21-a5ed0eda0775"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="b4ebd952-d5e9-4884-88ab-bb1bf670ed64"></span>
## 5.FAQ
<p>无</p>

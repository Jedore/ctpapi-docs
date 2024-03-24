<p>订阅公共流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="9425a8ad-9a8b-4960-9b4e-3fc59082493f"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="70546a33-0950-4f50-9fbf-e4249cca7804"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
<p>THOST_TERT_NONE：取消订阅公有流</p>
</blockquote>
<span class="anchor" id="02ceec0e-48f3-4b05-9c41-da79b5c81bc3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fa1db14e-4e25-4cbb-bb4d-faf9fa760de1"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="ac8040eb-d35a-4da1-a766-998c7b8b3610"></span>
## 5.FAQ
<p>无</p>

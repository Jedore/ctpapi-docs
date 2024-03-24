<p>订阅公共流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="7ccbe002-58ec-4fa9-95b2-ccadb690c204"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="4cc8066f-093a-4fb0-853a-0868b4333fea"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
<p>THOST_TERT_NONE：取消订阅公有流</p>
</blockquote>
<span class="anchor" id="b2473967-4763-418f-8d05-9bad3498eeca"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f6773d74-eeab-4bd7-8f11-b1a1d641ffcd"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="c400f078-e15b-4e93-b279-f102595c156f"></span>
## 5.FAQ
<p>无</p>

<p>订阅公共流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="e71d26e2-6652-44f8-b987-a94cb0df40cd"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="4a8617e1-f8e6-44c4-bbaf-40968348d68e"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
<p>THOST_TERT_NONE：取消订阅公有流</p>
</blockquote>
<span class="anchor" id="158c305a-a9c8-4a79-b54b-5ad77485f790"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="cd5934a4-4c15-4205-98df-81007d7e8fde"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="d57d195a-f9d2-4dca-a9ae-1f29808753b7"></span>
## 5.FAQ
<p>无</p>

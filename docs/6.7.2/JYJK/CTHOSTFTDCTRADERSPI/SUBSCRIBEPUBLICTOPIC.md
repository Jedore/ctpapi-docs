<p>订阅公共流。该方法要在<a href="../../../HQJK/CTHOSTFTDCMDAPI/INIT/">Init</a> 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="68c4f041-4237-4c86-b017-9024839407d1"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="5fa9e33f-f376-427f-b1a9-677459e8eae1"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
<p>THOST_TERT_NONE：取消订阅公有流</p>
</blockquote>
<span class="anchor" id="207c5d30-3410-4c84-b043-a140cdf22e9c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7bb4b7b7-31ee-4084-b242-8f19dce69c05"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="06506b0c-ac53-41a3-b31f-681bd9697c7e"></span>
## 5.FAQ
<p>无</p>

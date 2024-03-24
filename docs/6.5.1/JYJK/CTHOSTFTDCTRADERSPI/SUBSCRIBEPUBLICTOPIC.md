<p>订阅公共流。该方法要在Init 方法前调用。若不调用，默认RESTART模式订阅。</p>
<span class="anchor" id="53efcdac-d5f8-4912-a83f-eb6d6a158979"></span>
## 1.函数原型
<p>virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;</p>
<span class="anchor" id="29bfa4c4-45ac-4479-9b11-db32b91f1288"></span>
## 2.参数
<p>nResumeType：私有流重传方式。</p>
<blockquote>
<p>THOST_TERT_RESTART：从本交易日开始重传</p>
<p>THOST_TERT_RESUME：从上次收到的续传</p>
<p>THOST_TERT_QUICK：只传送登录后私有流的内容</p>
<p>THOST_TERT_NONE：取消订阅公有流</p>
</blockquote>
<span class="anchor" id="ae84ba52-03f4-42b2-9c80-57f5e936f375"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="562c4e4d-97c0-4e61-ad08-348de65d0d6b"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_RESUME);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_RESUME);
pUserApi-&gt;RegisterFront("tcp://127.0.0.1:51205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="a92ec19b-2994-4d8b-ad7a-0f383915e0d0"></span>
## 5.FAQ
<p>无</p>

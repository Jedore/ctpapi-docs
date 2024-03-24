<p>获取API的版本信息</p>
<span class="anchor" id="be0f9b28-b4a0-4462-bbf1-c94a96dc1111"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="d6e69c41-7332-4cbf-96cf-a13ab3137233"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="08260516-3208-4abe-bd86-dca75d440f92"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="ccac0ae2-59f9-4098-930a-5e0ba83fcd6c"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
LOG(pUserApi-&gt;GetApiVersion());
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="d0389b50-530b-4783-a01f-b1441df5f402"></span>
## 5.FAQ
<p>无</p>

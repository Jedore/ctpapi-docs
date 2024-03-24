<p>获取API的版本信息</p>
<span class="anchor" id="15efea71-609d-4b92-bf31-fecbccee2a96"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="dae154d2-e8f1-4f01-a362-29b4ddfed10d"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="2aac8937-3de1-4a33-813b-fba578e0a438"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="e54184c2-7943-4bb8-ba0c-9e0dd94aa411"></span>
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
<span class="anchor" id="71e4c106-43ce-4001-b9ce-37f2e8b9fbf0"></span>
## 5.FAQ
<p>无</p>

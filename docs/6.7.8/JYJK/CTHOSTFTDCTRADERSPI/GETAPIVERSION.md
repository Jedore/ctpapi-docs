<p>获取API的版本信息</p>
<span class="anchor" id="917efe81-904f-4723-9d7b-a718075d6924"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETAPIVERSION/">GetApiVersion</a>() = 0;</p>
<span class="anchor" id="15641268-38ac-4661-980f-4653f46ac14f"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="359dc820-8c7d-41c4-bc9c-b43c4c69e8c9"></span>
## 3.返回
<p>返回具体的版本号，如（v6.3.11_20180109 14:59:39）</p>
<span class="anchor" id="e40c9d08-181d-436b-b513-30f3ace00533"></span>
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
<span class="anchor" id="73fbdcfc-101c-4bc5-b1d9-53c30f255cea"></span>
## 5.FAQ
<p>无</p>

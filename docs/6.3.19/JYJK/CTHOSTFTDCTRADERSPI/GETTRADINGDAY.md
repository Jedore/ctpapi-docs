<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="5f609531-e064-4118-9276-65c9920f4954"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="ba3e2ade-e0cb-4a6b-9fac-b16a55ef53c7"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="842bb9e0-1189-4906-a24f-dae50b32d679"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="30929c5a-04cd-4a0f-bc96-4b72f63e9bff"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
pUserApi-&gt;RegisterFront(“tcp://127.0.0.1:51205”);
pUserApi-&gt;Init();
WaitForSingleObject(g_LoginSig, INFINITE); //等待登陆成功后
printf(pUserApi-&gt;GetTradingDay()); //获取交易日
</code></pre>
<span class="anchor" id="5a63952e-439c-41a7-be8e-abe9072e547d"></span>
## 5.FAQ
<p>无</p>

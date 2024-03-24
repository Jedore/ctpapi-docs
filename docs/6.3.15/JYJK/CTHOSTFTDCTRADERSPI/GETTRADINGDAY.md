<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="c4421dd3-c126-4971-9f18-05110f5a79c4"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="b42fb62f-1e32-4b18-90c3-4eea245f80a2"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="08a0000e-b5d4-42db-b8bc-19da4802f9b6"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="a70b3ad9-876a-4750-97dd-7a03f0a9a592"></span>
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
<span class="anchor" id="74a94ef8-3244-4fac-8c6d-808860821fa8"></span>
## 5.FAQ
<p>无</p>

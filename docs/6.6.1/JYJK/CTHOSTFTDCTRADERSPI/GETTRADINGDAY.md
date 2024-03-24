<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="f4d43a05-37e2-40b2-a2a8-5148b31ad3c2"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="6d2d86e2-4438-4556-9d14-9a051332b1b3"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="ff4ea01c-0603-4f0d-a123-c58abb6c1091"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="aa01991f-487b-4e3c-9ad5-9cbabd6efa56"></span>
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
<span class="anchor" id="e0cc60fd-4b02-4d3d-8ac5-0ae3b03b7b5f"></span>
## 5.FAQ
<p>无</p>

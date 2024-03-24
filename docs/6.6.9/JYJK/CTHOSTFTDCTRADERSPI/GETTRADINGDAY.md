<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="50844614-ed52-4688-a54e-269bf5e649fb"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="6675a844-5640-48d5-be1e-851498f89bbd"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="6302aa7d-47da-41f1-ab7e-e9efab6ca8e7"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="09b688d1-c6a2-45af-b07c-bec78227ddef"></span>
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
<span class="anchor" id="e119af5d-ca8b-49f3-a375-ce982291a4b5"></span>
## 5.FAQ
<p>无</p>

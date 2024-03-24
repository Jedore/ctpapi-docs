<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="0c8367e8-272d-471d-b215-fde3ed4dabbf"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="fa0a9913-4f7e-4393-bda1-5857ed92f9c8"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="cdc1c3fc-99ce-48c6-86fd-06b6486c6651"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="212fb249-c7ca-4757-ac7a-7ddcb0880b4d"></span>
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
<span class="anchor" id="dfef3c22-cc7c-4bc5-b51e-7dcc9dd1f140"></span>
## 5.FAQ
<p>无</p>

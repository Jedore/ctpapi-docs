<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="b36894de-864e-4879-b9db-cbaea08de6bf"></span>
## 1.函数原型
<p>virtual const char *GetTradingDay() = 0;</p>
<span class="anchor" id="59c04a00-fabe-43ed-a802-42f0f22876db"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="368199f9-4dbe-44a7-8d89-e3aaa5669f2c"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="5e10a818-e67f-4935-8103-96e048fe338b"></span>
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
<span class="anchor" id="e214d416-529d-4d6c-b4a6-b0c02d25b10b"></span>
## 5.FAQ
<p>无</p>

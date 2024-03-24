<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="c2e310e3-f4df-4efc-a84d-a3a60186a61d"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETTRADINGDAY/">GetTradingDay</a>() = 0;</p>
<span class="anchor" id="4d03f5b0-4717-478d-9521-b13ca97c63cc"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="5915f5aa-a763-4060-a04d-20f447560bfa"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="ec24ca4d-1f4b-4bd1-a03d-14aa167b042e"></span>
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
<span class="anchor" id="1d2ba1b3-fdcd-4b35-ae0d-9bfa41b64b8c"></span>
## 5.FAQ
<p>无</p>

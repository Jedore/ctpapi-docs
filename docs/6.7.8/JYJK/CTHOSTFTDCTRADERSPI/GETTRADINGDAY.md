<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="497918f3-a46b-4b6e-9b19-803621307f13"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETTRADINGDAY/">GetTradingDay</a>() = 0;</p>
<span class="anchor" id="24325d86-5980-492d-9fc9-152640cb95de"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="ccb0fed1-091a-479a-be06-1b5f1f79fdee"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="3cc9eb6e-c126-4862-80ac-522ed461b8bb"></span>
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
<span class="anchor" id="5dfb7ded-89e6-427d-8206-333a968f68ac"></span>
## 5.FAQ
<p>无</p>

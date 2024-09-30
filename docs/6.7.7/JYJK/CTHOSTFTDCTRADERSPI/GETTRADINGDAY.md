<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="e7f84e14-e44b-40ff-88d8-81d5643f4b7c"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETTRADINGDAY/">GetTradingDay</a>() = 0;</p>
<span class="anchor" id="d41a41f6-500d-4e0d-bbe8-fe0334a24b16"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="e22eea51-88c5-4879-a2d1-83137cb35ded"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="d70164be-5d34-4880-aa93-3ca1daa683f0"></span>
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
<span class="anchor" id="842db64b-6a17-45e0-96d0-aaa305657101"></span>
## 5.FAQ
<p>无</p>

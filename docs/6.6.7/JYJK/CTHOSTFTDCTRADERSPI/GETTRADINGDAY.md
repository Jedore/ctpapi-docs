<p>获得当前交易日。只有当登陆成功后才会取到正确的值。</p>
<span class="anchor" id="877db391-589f-4403-b6d4-3d66f75ebfcd"></span>
## 1.函数原型
<p>virtual const char *<a href="../../../HQJK/CTHOSTFTDCMDAPI/GETTRADINGDAY/">GetTradingDay</a>() = 0;</p>
<span class="anchor" id="e8b8b642-7420-404f-b903-4c6ba89515ec"></span>
## 2.参数
<p>无</p>
<span class="anchor" id="46c6dc10-d499-467e-9df9-732f5cccf47f"></span>
## 3.返回
<p>返回一个指向日期信息字符串的常量指针。</p>
<span class="anchor" id="bc942ce1-8e1e-41aa-a5fd-e61703dc70ba"></span>
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
<span class="anchor" id="c3a4c6d6-8d95-4b46-8a96-f305be81ed34"></span>
## 5.FAQ
<p>无</p>

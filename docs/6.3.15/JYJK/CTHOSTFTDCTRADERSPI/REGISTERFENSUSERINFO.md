<p>注册名字服务器用户信息，调用RegisterNameServer前需要先使用RegisterFensUserInfo设置登录模式。</p>
<span class="anchor" id="1699df76-e103-413c-8235-40ce6b713bd4"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField 》 pFensUserInfo) = 0;</p>
<span class="anchor" id="3a97ca04-1bf8-4b2a-b598-47e5cdba06a6"></span>
## 2.参数
<p>CThostFtdcFensUserInfoField：Fens用户信息</p>
<pre><code>struct CThostFtdcFensUserInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///登录模式
    TThostFtdcLoginModeType LoginMode;
};
</code></pre>
<p>LoginMode：填写<code>THOST_FTDC_LM_Trade</code></p>
<span class="anchor" id="79fe29cd-2ed8-4801-9441-93a12f12933f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5babd86f-e414-4e4d-ac16-cbd0c1d78264"></span>
## 4.调用示例
<pre><code>CThostFtdcTraderApi *pUserApi = CThostFtdcTraderApi::CreateFtdcTraderApi("F:\\flow\\");
CSimpleHandler sh(pUserApi);
pUserApi-&gt;RegisterSpi(&amp;sh);
printf(pUserApi-&gt;GetApiVersion());
pUserApi-&gt;SubscribePrivateTopic(THOST_TERT_QUICK);
pUserApi-&gt;SubscribePublicTopic(THOST_TERT_QUICK);
CThostFtdcFensUserInfoField pFensUserInfo = { 0 };
strcpy_s(pFensUserInfo.BrokerID, "9999");
strcpy_s(pFensUserInfo.UserID, "1000001");
pFensUserInfo.LoginMode = THOST_FTDC_LM_Trade;
pUserMdApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo);
pUserMdApi-&gt; RegisterNameServer(“tcp://127.0.0.1:41205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="2f51d533-5959-4c3c-8212-bf588adda337"></span>
## 5.FAQ
<p>无</p>

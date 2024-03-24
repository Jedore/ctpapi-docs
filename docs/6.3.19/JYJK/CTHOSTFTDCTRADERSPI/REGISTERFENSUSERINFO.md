<p>注册名字服务器用户信息，调用RegisterNameServer前需要先使用RegisterFensUserInfo设置登录模式。</p>
<span class="anchor" id="108cff7b-c088-4f4f-962e-dee2331f9194"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="6d37114a-26cb-4364-986a-c0aaad5723c2"></span>
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
<span class="anchor" id="3742ee2b-7802-4fba-b6b1-9d9a652faf2c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="29d23bc3-de8c-4ad6-92a0-984f3cae10ed"></span>
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
pUserApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo);
pUserApi-&gt; RegisterNameServer("tcp://127.0.0.1:41205");
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="bacbdafe-a8da-4a48-b7dc-ce0944ef18fe"></span>
## 5.FAQ
<p>无</p>

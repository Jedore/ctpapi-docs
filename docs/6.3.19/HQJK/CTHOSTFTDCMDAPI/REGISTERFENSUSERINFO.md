<p>注册名字服务器用户信息，调用RegisterNameServer前需要先使用RegisterFensUserInfo设置登录模式。</p>
<span class="anchor" id="4e97c90b-8f91-44f0-aafd-76b645a77d79"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="01bee7cc-9ba7-4b0f-a995-4d64f7173102"></span>
## 2.参数
<p>pFensUserInfo：Fens用户信息</p>
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
<span class="anchor" id="23332e34-e308-4f23-add7-acbfd1fae7e5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="824d20e9-aa15-464c-94e3-1f99d14ec7f2"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
CThostFtdcFensUserInfoField pFensUserInfo = { 0 };
strcpy_s(pFensUserInfo.BrokerID, "9999");
strcpy_s(pFensUserInfo.UserID, "00001");
pFensUserInfo.LoginMode = THOST_FTDC_LM_Trade;
pUserMdApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo);
pUserMdApi-&gt; RegisterNameServer ("tcp://127.0.0.1:41213");
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="b0f7f65c-e9da-4af6-b9e5-329d25c05795"></span>
## 5.FAQ
<p>无</p>

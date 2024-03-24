<p>注册名字服务器用户信息，调用RegisterNameServer前需要先使用RegisterFensUserInfo设置登录模式。</p>
<span class="anchor" id="8544b5a3-12e0-43d0-b361-b90d3eaf864d"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="19edd74a-f3b9-44ff-a907-6b51e37f57cd"></span>
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
<span class="anchor" id="a7c3599d-a9fe-4490-aa55-b679abfa971d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e81c3c99-e4df-4b9b-bd8e-f65ea00c90d9"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
CThostFtdcFensUserInfoField pFensUserInfo = { 0 };
strcpy_s(pFensUserInfo.BrokerID, g_chBrokerID);
strcpy_s(pFensUserInfo.UserID, g_chUserID);
pFensUserInfo.LoginMode = THOST_FTDC_LM_Trade;
m_pUserApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo, nRequestID++);
pUserMdApi-&gt; RegisterNameServer (“tcp://127.0.0.1:41213”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="5ede56f9-1b4b-4847-9398-59d329361285"></span>
## 5.FAQ
<p>无</p>

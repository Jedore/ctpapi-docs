<p>注册名字服务器用户信息，调用<a href="../REGISTERNAMESERVER/">RegisterNameServer</a>前需要先使用<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="187d5b6d-9a14-491c-b396-211e67ff77c3"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="03e0bcb0-e02c-41e4-9118-82d184a5015f"></span>
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
<span class="anchor" id="583de195-3326-4392-9e35-8f09419c8547"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3016ca1d-f0c0-4540-b07a-8a70df94c578"></span>
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
<span class="anchor" id="7eeb69c7-e6ed-409a-bbf8-ccefbafab960"></span>
## 5.FAQ
<p>无</p>

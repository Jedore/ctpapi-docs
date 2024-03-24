<p>注册名字服务器用户信息，调用<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERNAMESERVER/">RegisterNameServer</a>前需要先使用RegisterFensUserInfo设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="ef0b3fa8-4da2-4abd-92d2-2f445718ccec"></span>
## 1.函数原型
<p>virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="2ae8ac9c-9be9-4357-860a-4654fb55cb0e"></span>
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
<span class="anchor" id="1e5809ce-25c5-4594-9ecd-589cbf642dc6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="80d29008-ce0e-4c27-871a-2b97076ed81c"></span>
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
<span class="anchor" id="e1eaaeda-7ecf-4da3-91de-4faf7e41c28d"></span>
## 5.FAQ
<p>无</p>

<p>注册名字服务器用户信息，调用<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERNAMESERVER/">RegisterNameServer</a>前需要先使用<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="4bbc2df0-b33a-4561-8489-cb9bdb1044b6"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>(CThostFtdcFensUserInfoField * pFensUserInfo) = 0;</p>
<span class="anchor" id="05075199-8654-4f88-b540-8811e4e5f679"></span>
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
<span class="anchor" id="774532ba-a857-4a8b-908d-51542b54c182"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="77695041-55c4-49be-a8d3-d8f1575f492b"></span>
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
<span class="anchor" id="ade93073-cbb5-41e0-ba79-fa14d087d7eb"></span>
## 5.FAQ
<p>无</p>

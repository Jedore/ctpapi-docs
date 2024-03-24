<p>设置名字服务器网络地址。<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERNAMESERVER/">RegisterNameServer</a>优先于<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFRONT/">RegisterFront</a>。</p>
<p>调用前需要先使用<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>如果CTP系统启用了fens前置，则可以使用该接口连接fens前置地址。</p>
<blockquote>
<p>fens的好处是fens地址对应的后端地址是一个前置地址池，前置地址的增删改都对用户透明，用户不需要调整自己的接入地址。当API使用fens地址接入时，fens前置会返回一个地址池，随后API择优选择一个地址进行接入。</p>
</blockquote>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="e38941f1-9c0b-44f2-9db2-3ff8b579e450"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERNAMESERVER/">RegisterNameServer</a>(char *pszNsAddress) = 0;</p>
<span class="anchor" id="0712a9a8-2fab-429c-8b87-f6bbd95b7baf"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”。如：“tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。“17001”代表服务器端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="c277f593-b69d-4b7c-82a0-53d7656daf77"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="680e0bab-21f2-443a-bffd-c36bea167f60"></span>
## 4.调用示例
<pre><code>CThostFtdcMdApi  *pUserMdApi = CThostFtdcMdApi::CreateFtdcMdApi();
CSimpleMdHandler ash(pUserMdApi);
pUserMdApi-&gt;RegisterSpi(&amp;ash);
CThostFtdcFensUserInfoField pFensUserInfo = { 0 };
strcpy_s(pFensUserInfo.BrokerID, g_chBrokerID);
strcpy_s(pFensUserInfo.UserID, g_chUserID);
pFensUserInfo.LoginMode = THOST_FTDC_LM_Trade;
pUserMdApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo, nRequestID++);
pUserMdApi-&gt;RegisterNameServer (“tcp://127.0.0.1:41205”);
pUserMdApi-&gt;Init();
</code></pre>
<span class="anchor" id="a9ad9469-f704-42fb-b6c1-a997c8228e52"></span>
## 5.FAQ
<p>无</p>

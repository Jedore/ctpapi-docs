<p>设置名字服务器网络地址。RegisterNameServer优先于<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REGISTERFRONT/">RegisterFront</a>。</p>
<p>调用前需要先使用<a href="../REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>如果CTP系统启用了fens前置，则可以使用该接口连接fens前置地址。</p>
<blockquote>
<p>fens的好处是fens地址对应的后端地址是一个前置地址池，前置地址的增删改都对用户透明，用户不需要调整自己的接入地址。当API使用fens地址接入时，fens前置会返回一个地址池，随后API择优选择一个地址进行接入。</p>
</blockquote>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="ad9da000-59dc-45da-b41f-d1ae90b495bc"></span>
## 1.函数原型
<p>virtual void RegisterNameServer(char *pszNsAddress) = 0;</p>
<span class="anchor" id="3d507299-75db-40b5-8b8a-b161496f0902"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”。如：“tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。“17001”代表服务器端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="89acddee-0039-4921-b939-27364b51910f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="bc2fe5c9-20a4-49d5-a164-cbe4aa90cd25"></span>
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
<span class="anchor" id="5e726e6f-0313-4b93-96ec-26109f3137db"></span>
## 5.FAQ
<p>无</p>

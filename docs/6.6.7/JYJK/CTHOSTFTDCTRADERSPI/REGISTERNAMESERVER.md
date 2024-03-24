<p>设置名字服务器网络地址。RegisterNameServer优先于<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERFRONT/">RegisterFront</a>。</p>
<p>调用前需要先使用<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="0a0f6223-0371-4dc3-b39e-d7eb64104cf5"></span>
## 1.函数原型
<p>virtual void RegisterNameServer(char *pszNsAddress) = 0;</p>
<span class="anchor" id="cb122819-415f-4c5d-a110-c5ef42f0091c"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="67e6350d-d81d-4aa2-bb68-23e67aea117b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7167a622-bbe6-4eaa-837c-7285affe7f10"></span>
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
pUserApi-&gt; RegisterNameServer (“tcp://127.0.0.1:41205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="1b93a1a3-734f-4599-ae3d-8dce5505efeb"></span>
## 5.FAQ
<p>无</p>

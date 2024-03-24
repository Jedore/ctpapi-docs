<p>设置名字服务器网络地址。<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERNAMESERVER/">RegisterNameServer</a>优先于<a href="../REGISTERFRONT/">RegisterFront</a>。</p>
<p>调用前需要先使用<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="bbe14894-3418-41be-9f11-7b9157f6e1ac"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERNAMESERVER/">RegisterNameServer</a>(char *pszNsAddress) = 0;</p>
<span class="anchor" id="34d3b485-1889-4160-8a5a-eca9b43848d2"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="5b2b8fc5-fe6b-4dad-8cdf-5db3319e91a9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="64d350c9-f206-4758-8a9d-bd34b57839e5"></span>
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
<span class="anchor" id="6cea9594-223f-4de6-a798-b804271892a4"></span>
## 5.FAQ
<p>无</p>

<p>设置名字服务器网络地址。<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERNAMESERVER/">RegisterNameServer</a>优先于<a href="../REGISTERFRONT/">RegisterFront</a>。</p>
<p>调用前需要先使用<a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERFENSUSERINFO/">RegisterFensUserInfo</a>设置登录模式。</p>
<p>详见<a href="../../../QTYWGZ/FENS/">fens连接说明</a></p>
<span class="anchor" id="6a399822-fa43-4e8f-9d13-0a635e32363f"></span>
## 1.函数原型
<p>virtual void <a href="../../../HQJK/CTHOSTFTDCMDAPI/REGISTERNAMESERVER/">RegisterNameServer</a>(char *pszNsAddress) = 0;</p>
<span class="anchor" id="053890ff-d4fa-47cd-9184-e860ecdb0d74"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。</p>
<p>SSL前置格式：ssl://192.168.0.1:41205</p>
<p>TCP前置IPv4格式：tcp://192.168.0.1:41205</p>
<p>TCP前置IPv6格式：tcp6://fe80::20f8:aa9b:7d59:887d:35001</p>
</blockquote>
<span class="anchor" id="4115a40f-3189-4b94-bb8f-cce26ff20f59"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="70b37825-a97c-48a4-9173-a5fbeb0c226d"></span>
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
<span class="anchor" id="4e628433-5cd3-4126-84db-15ff1ffcc6e5"></span>
## 5.FAQ
<p>无</p>

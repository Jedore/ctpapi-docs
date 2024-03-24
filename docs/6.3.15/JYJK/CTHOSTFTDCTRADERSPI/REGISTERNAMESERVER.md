<p>设置名字服务器网络地址。RegisterNameServer优先于RegisterFront。</p>
<p>调用前需要先使用RegisterFensUserInfo设置登录模式。</p>
<span class="anchor" id="4d471c20-49c0-4f0b-abb3-20eaa3c69282"></span>
## 1.函数原型
<p>virtual void RegisterNameServer(char *pszNsAddress) = 0;</p>
<span class="anchor" id="39a27f88-bbfd-4b07-a8da-ca314d2e2c42"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。</p>
</blockquote>
<span class="anchor" id="11558ea0-e2dc-4999-b5fa-e84a10be6fa6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="840493f7-e494-4515-8c91-fa8242e9018d"></span>
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
pUserMdApi-&gt;RegisterFensUserInfo(&amp;pFensUserInfo);
pUserMdApi-&gt; RegisterNameServer (“tcp://127.0.0.1:41205”);
pUserApi-&gt;Init();
</code></pre>
<span class="anchor" id="9e4d47bc-0bd3-4e04-a741-60a871671c1d"></span>
## 5.FAQ
<p>无</p>

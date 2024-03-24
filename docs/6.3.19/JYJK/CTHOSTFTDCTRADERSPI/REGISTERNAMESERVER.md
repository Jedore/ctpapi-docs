<p>设置名字服务器网络地址。RegisterNameServer优先于RegisterFront。</p>
<p>调用前需要先使用RegisterFensUserInfo设置登录模式。</p>
<span class="anchor" id="96b8fbb4-f861-48e7-a7f6-aa9fd7134691"></span>
## 1.函数原型
<p>virtual void RegisterNameServer(char *pszNsAddress) = 0;</p>
<span class="anchor" id="f26e774a-44fa-458b-9a11-d08b53a2b868"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。</p>
</blockquote>
<span class="anchor" id="52e425de-d3de-4ee7-a78d-d9367126f773"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d5e7b00c-1a3d-4a68-9b04-1ec3cbf738aa"></span>
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
<span class="anchor" id="5a26818c-7a25-47a7-a932-aea7d100c69e"></span>
## 5.FAQ
<p>无</p>

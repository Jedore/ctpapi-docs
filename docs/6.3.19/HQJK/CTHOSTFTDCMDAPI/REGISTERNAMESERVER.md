<p>设置名字服务器网络地址。RegisterNameServer优先于RegisterFront。</p>
<p>调用前需要先使用RegisterFensUserInfo设置登录模式。</p>
<p>如果CTP系统启用了fens前置，则可以使用该接口连接fens前置地址。</p>
<blockquote>
<p>fens的好处是fens地址对应的后端地址是一个前置地址池，前置地址的增删改都对用户透明，用户不需要调整自己的接入地址。当API使用fens地址接入时，fens前置会返回一个地址池，随后API随机选择一个地址进行接入。</p>
</blockquote>
<span class="anchor" id="d12593a5-0af5-4589-84be-a9f34ef5f66c"></span>
## 1.函数原型
<p>virtual void RegisterNameServer(char *pszNsAddress) = 0;</p>
<span class="anchor" id="cd7cbd9e-e61c-4737-9c11-b7ae3105c7bd"></span>
## 2.参数
<p>pszNsAddress:指向后台服务器地址的指针。</p>
<blockquote>
<p>服务器地址的格式为：“protocol://ipaddress:port”。如：“tcp://127.0.0.1:17001”。“tcp”代表传输协议，“127.0.0.1”代表服务器地址。“17001”代表服务器端口号。</p>
</blockquote>
<span class="anchor" id="1b9bd98f-8cb6-4bc1-b4c6-aa6b6e38d074"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="cbdaf471-d991-437d-9cdf-318e1e6edac7"></span>
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
<span class="anchor" id="efb9eac2-8739-4d27-bc71-933aac032332"></span>
## 5.FAQ
<p>无</p>

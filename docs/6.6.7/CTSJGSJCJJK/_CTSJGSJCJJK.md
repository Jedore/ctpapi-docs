<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>

</div></td><td class="square-block-right"></td></tr></tbody></table>
<span class="anchor" id="d942734d-0ba2-4c4f-8721-a76394f95912"></span>
## 1.定义
<table>
<tr>
<td bgcolor="#0062A8"><font color="#FFFFFF" face="微软雅黑">术语</font></td>
<td bgcolor="#0062A8"><font color="#FFFFFF" face="微软雅黑">术语说明</font></td>
</tr>
<tr>
<td>采集API链接库</td>
<td>负责采集终端信息的动态链接库(windows版的WinDataCollect.dll，linux版的LinuxDataCollect.so，安卓版的InfoCollection_single_release.aar)，只有连接中继服务器的终端需要调用，直连模式或中继服务器无需调用</td>
</tr>
<tr>
<td>直连类型终端</td>
<td>直接连接到CTP交易系统的客户交易终端</td>
</tr>
<tr>
<td>中继类型终端</td>
<td>先连接到中继服务器,中继服务器再调用TraderAPI连接到CTP交易系统的客户交易终端</td>
</tr>
<tr>
<td>多对多类型中继服务器</td>
<td>为每个客户终端，建立CTP API实例，每个用户独占一个交易API实例的中继服务器</td>
</tr>
<tr>
<td>一对多类型中继服务器</td>
<td>为多个客户终端，建立一个CTP API实例，使用操作员为多个客户进行交易的中继服务器</td>
</tr>
<tr>
<td>AppID</td>
<td>每个期货终端软件需要向期货公司申请自己的AppID</td>
</tr>
<tr>
<td>RelayAppID</td>
<td>中继服务器软件需要向期货公司申请自己的RelayAppID</td>
</tr>
</table>
<blockquote>
<p><strong>AppID和RelayAppID必须符合监控中心的格式要求</strong>。见监控中心官网技术规范。</p>
<p>直连类型终端<code>无需加载</code>采集链接库，登录时会自动采集并上报终端信息。</p>
<p>中继类型服务器<code>无需加载</code>采集链接库，仅负责接收客户端的采集信息并上报CTP。</p>
<p>中继类型终端需要加载采集链接库，并将采集到的信息发送给中继服务器。</p>
</blockquote>
<span class="anchor" id="b75ac0a9-26d2-48c7-8084-e2b977312cd6"></span>
## 2.说明
<p>期货公司确认终端软件集成了正确的数据采集模块后，为该AppID的终端软件分配授权码。终端软件需要保护好自己的AppID和授权码，防止被其他软件盗用。CTP对终端的认证流程如下：</p>
<ul>
<li>直连终端认证流程</li>
</ul>
<p>对于直接连接期货公司交易柜台的终端，期货公司确认终端软件集成了正确的数据采集模块后。给该终端软件（根据AppID）分配一个授权码。这个授权码和AppID是绑定的，当终端试图登录期货公司交易软件的时候，交易后台会验证该终端是否持有合法的AppID和授权码。</p>
<ul>
<li>中继和中继下属终端的认证流程</li>
</ul>
<p>对于使用中继服务器连接期货公司交易柜台的终端，期货公司确认终端软件集成了正确的数据采集模块和确认中继可以正常报送终端信息后。期货公司给该终端软件（根据AppID）分配一个授权码，给中继服务器（根据RelayAppID） 分配一个授权码。当终端登录中继服务器时，中继服务器负责验证终端的合法性；当中继服务器登录期货公司交易软件的时候，交易后台会验证该中继服务器是否持有合法的RelayAppID和授权码。</p>
<p><strong><font color="#FF0000">注:信息采集过程中，遇到某些信息没有采集到，无法判断是否正常。此时可以参考监控中心规范文档里的函数手工调用，判断是否是权限问题或者相应操作系统命令组件没有部署。如果正常情况下手工调用能采集到，而采集函数采集不到，请联系上期技术。</font></strong></p>
<p><span alt="" id="anchor-id-03"></span> </p>
<span class="anchor" id="eb1acbc7-0380-49a8-b4e7-9df8171a58be"></span>
## 3.权限要求
<p>采集库需要u+s权限</p>
<span class="anchor" id="6f7bdab5-dd54-47e0-b798-332f70bd0200"></span>
## 4.相关接口
<pre><code>///客户端认证请求
virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) = 0;
///客户端认证响应
virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
///上报用户终端信息，用于中继服务器操作员登录模式
///操作员登录后，可以多次调用该接口上报客户信息
virtual int SubmitUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;
///注册用户终端信息，用于中继服务器多连接模式
///需要在终端认证成功后，用户登录前调用该接口
virtual int RegisterUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;
</code></pre>
<blockquote>
<p>注意，采集库不是线程安全的。多线程调用采集库时要加锁，如果是直连模式则要在登录函数上加锁。</p>
</blockquote>
<span class="anchor" id="fd4680a3-914b-42dd-82f0-98af00216f39"></span>
## 5.示例代码
<p><strong>每个类型的终端调用流程不同，请注意区分！</strong></p>
<span class="anchor" id="6a77a2a6-2e5d-4e97-b47d-b1ec19f1d80f"></span>
### 5.1.直连终端的采集使用流程示例代码：
<p class="step-para"><span class="step-mark">Step 1</span> 在API连接后发起认证</p>
<pre><code>void CUser::OnFrontConnected()
{
    cout &lt;&lt; "OnFrontConnected." &lt;&lt; endl;
    static const char *version = m_pUserApi-&gt;GetApiVersion();
    cout &lt;&lt; "------当前版本号 ：" &lt;&lt; version &lt;&lt; " ------" &lt;&lt; endl;
    ReqAuthenticate();
}
int CUser::ReqAuthenticate()
{
    CThostFtdcReqAuthenticateField field;
    memset(&amp;field, 0, sizeof(field));
    strcpy(field.BrokerID, "8000");
    strcpy(field.UserID, "001888");
    strcpy(field.AppID, "XY_Q7_V1.0.0");
    strcpy(field.AuthCode, "5A5P4V7AZ5LCFEAK");
    return m_pUserApi-&gt;ReqAuthenticate(&amp;field, 5);
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 2</span> 认证成功后发起登录</p>
<pre><code>void CUser::OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    printf("OnRspAuthenticate\n");
    if (pRspInfo != NULL &amp;&amp; pRspInfo-&gt;ErrorID == 0)
    {
        printf("认证成功,ErrorID=0x%04x, ErrMsg=%s\n\n", pRspInfo-&gt;ErrorID, pRspInfo-&gt;ErrorMsg);
        ReqUserLogin();
    }
    else
    cout &lt;&lt; "认证失败，" &lt;&lt; "ErrorID=" &lt;&lt; pRspInfo-&gt;ErrorID &lt;&lt; "  ,ErrMsg=" &lt;&lt; pRspInfo-&gt;ErrorMsg &lt;&lt; endl;
}
int CUser::ReqUserLogin()
{
    printf("====ReqUserLogin====,用户登录中...\n\n");
    CThostFtdcReqUserLoginField reqUserLogin;
    memset(&amp;reqUserLogin, 0, sizeof(reqUserLogin));
    strcpy_s(reqUserLogin.BrokerID, "8000");
    strcpy(reqUserLogin.UserID, "001888");
    strcpy(reqUserLogin.Password, "1");
    strcpy(reqUserLogin.TradingDay, "20150715");
    return m_pUserApi-&gt;ReqUserLogin(&amp;reqUserLogin, ++RequestID);
}
</code></pre>
<span class="anchor" id="3c5329ae-f769-4d3d-972f-db880dcfaae7"></span>
### 5.2.多对多中继终端使用流程示例代码：
<p class="step-para"><span class="step-mark">Step 1</span> 终端侧采集信息，向中继发起登录，并将终端信息发送给中继</p>
<pre><code>char pSystemInfo[344];
int len;
CTP_GetSystemInfo(pSystemInfo, len);
cout &lt;&lt; "CTP_GetSystemInfo once" &lt;&lt; endl;
</code></pre>
<p class="step-para"><span class="step-mark">Step 2</span> 中继收到终端的登录请求，新建一个API实例，并发起连接</p>
<pre><code>void CUser::OnFrontConnected()
{
    cout &lt;&lt; "OnFrontConnected." &lt;&lt; endl;
    static const char *version = m_pUserApi-&gt;GetApiVersion();
    cout &lt;&lt; "------当前版本号 ：" &lt;&lt; version &lt;&lt; " ------" &lt;&lt; endl;
    ReqAuthenticate();
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 3</span> 中继连上前置后，发起认证请求</p>
<pre><code>int CUser::ReqAuthenticate()
{
    CThostFtdcReqAuthenticateField field;
    memset(&amp;field, 0, sizeof(field));
    strcpy(field.BrokerID, "8000");
    strcpy(field.UserID, "001888");
    strcpy(field.AppID, "XY_RELAY_V1.0.0");
    strcpy(field.AuthCode, "5A5P4V7AZ5LCFEAK");
    return m_pUserApi-&gt;ReqAuthenticate(&amp;field, 5);
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 4</span> 中继认证成功后，注册终端的采集信息</p>
<pre><code>void CUser::OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    printf("OnRspAuthenticate\n");
    if (pRspInfo != NULL &amp;&amp; pRspInfo-&gt;ErrorID == 0)
    {
        printf("认证成功,ErrorID=0x%04x, ErrMsg=%s\n\n", pRspInfo-&gt;ErrorID, pRspInfo-&gt;ErrorMsg);
        RegSystemInfo();
        ReqUserLogin();
    }
    else
        cout &lt;&lt; "认证失败，" &lt;&lt; "ErrorID=" &lt;&lt; pRspInfo-&gt;ErrorID &lt;&lt; "  ,ErrMsg=" &lt;&lt; pRspInfo-&gt;ErrorMsg &lt;&lt; endl;
}
void CUser::RegSystemInfo()
{
    //char pSystemInfo[344];
    //int len;   
    ////将前面从终端得到的信息赋值给下面结构体
    CThostFtdcUserSystemInfoField field;
    memset(&amp;field, 0, sizeof(field));
    strcpy(field.BrokerID, "8000");
    strcpy(field.UserID, "001888");
    //strcpy(field.ClientSystemInfo, pSystemInfo); 不能用 因为不是字符串
    memcpy(field.ClientSystemInfo, pSystemInfo, len);
    field.ClientSystemInfoLen = len;
    strcpy(field.ClientPublicIP, "198.4.4.124");
    field.ClientIPPort = 65535;
    strcpy(field.ClientLoginTime, "11:28:28");
    strcpy(field.ClientAppID, "Q7");
    int ret = m_pUserApi-&gt;RegisterUserSystemInfo(&amp;field);
    cout &lt;&lt; "retd = " &lt;&lt; ret &lt;&lt; endl;
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 5</span> 中继注册好终端的信息后，发起登录</p>
<pre><code>int CUser::ReqUserLogin()
{
    printf("====ReqUserLogin====,用户登录中...\n\n");
    CThostFtdcReqUserLoginField reqUserLogin;
    memset(&amp;reqUserLogin, 0, sizeof(reqUserLogin));
    strcpy_s(reqUserLogin.BrokerID, "8000");
    strcpy(reqUserLogin.UserID, "001888");
    strcpy(reqUserLogin.Password, "1");
    strcpy(reqUserLogin.TradingDay, "20150715");
    return m_pUserApi-&gt;ReqUserLogin(&amp;reqUserLogin, ++RequestID);
}
</code></pre>
<span class="anchor" id="11688c6e-2933-433d-a180-95599389c5c5"></span>
### 5.3.一对多中继终端使用流程示例代码：
<p class="step-para"><span class="step-mark">Step 1</span> 中继在启动后，在API连接后发起认证</p>
<pre><code>void CUser::OnFrontConnected()
{
    cout &lt;&lt; "OnFrontConnected." &lt;&lt; endl;
    static const char *version = m_pUserApi-&gt;GetApiVersion();
    cout &lt;&lt; "------当前版本号 ：" &lt;&lt; version &lt;&lt; " ------" &lt;&lt; endl;
    ReqAuthenticate();
}
int CUser::ReqAuthenticate()
{
    CThostFtdcReqAuthenticateField field;
    memset(&amp;field, 0, sizeof(field));
    strcpy(field.BrokerID, "8000");
    strcpy(field.UserID, "8000_admin");
    strcpy(field.AppID, " XY_RELAYB_V1.0.0");
    strcpy(field.AuthCode, "BLFLTYGD16FZZ91T");
    return m_pUserApi-&gt;ReqAuthenticate(&amp;field, 5);
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 2</span> 中继认证成功后，<code>使用操作员</code>发起登录</p>
<pre><code>void CUser::OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
{
    printf("OnRspAuthenticate\n");
    if (pRspInfo != NULL &amp;&amp; pRspInfo-&gt;ErrorID == 0)
   {
        printf("认证成功,ErrorID=0x%04x, ErrMsg=%s\n\n", pRspInfo-&gt;ErrorID, pRspInfo-&gt;ErrorMsg);
        ReqUserLogin();
    }
    else
        cout &lt;&lt; "认证失败，" &lt;&lt; "ErrorID=" &lt;&lt; pRspInfo-&gt;ErrorID &lt;&lt; "  ,ErrMsg=" &lt;&lt; pRspInfo-&gt;ErrorMsg &lt;&lt; endl;
}
int CUser::ReqUserLogin()
{
    printf("====ReqUserLogin====,用户登录中...\n\n");
    CThostFtdcReqUserLoginField reqUserLogin;
    memset(&amp;reqUserLogin, 0, sizeof(reqUserLogin));
    strcpy_s(reqUserLogin.BrokerID, "8000");
    strcpy(reqUserLogin.UserID, "8000_admin");
    strcpy(reqUserLogin.Password, "1");
    strcpy(reqUserLogin.TradingDay, "");
    strcpy(reqUserLogin.ClientIPAddress, "1.1.1.1");
    reqUserLogin.ClientIPPort = 11;
    return m_pUserApi-&gt;ReqUserLogin(&amp;reqUserLogin, ++RequestID);
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 3</span> 此时有终端登录中继，并将采集信息发送给中继</p>
<pre><code>char pSystemInfo[344];
int len;
CTP_GetSystemInfo(pSystemInfo, len);
cout &lt;&lt; "CTP_GetSystemInfo once" &lt;&lt; endl;
</code></pre>
<p class="step-para"><span class="step-mark">Step 4</span> 中继接收到采集信息后，发起终端信息的上报</p>
<pre><code>void CUser::SubSystemInfo()
{
    //char pSystemInfo[344];
    //int len;
    ///CTP_GetSystemInfo(pSystemInfo, len);
    /////终端信息由终端发送到中继，并提交信息
    cout &lt;&lt; "SubSystemInfo 1" &lt;&lt; endl;
    CThostFtdcUserSystemInfoField field;
    memset(&amp;field, 0, sizeof(field));
    strcpy(field.BrokerID, "8000");
    strcpy(field.UserID, "0018881");
    //strcpy(field.ClientSystemInfo, pSystemInfo); 不能用 因为不是字符串
    memcpy(field.ClientSystemInfo, pSystemInfo, len);
    field.ClientSystemInfoLen = len;
    strcpy(field.ClientPublicIP, "198.114.114.124");
    field.ClientIPPort = 65535;
    strcpy(field.ClientLoginTime, "11:28:28");
    strcpy(field.ClientAppID, "Q7");
    int retx = m_pUserApi-&gt;SubmitUserSystemInfo(&amp;field);
    cout &lt;&lt; "ret = " &lt;&lt; retx &lt;&lt; endl;
     //为另一个用户提交采集信息
    CThostFtdcUserSystemInfoField field1;
    memset(&amp;field1, 0, sizeof(field1));
    strcpy(field1.BrokerID, "8000");
    strcpy(field1.UserID, "0018882");
    memcpy(field1.ClientSystemInfo, pSystemInfo, len);
    field1.ClientSystemInfoLen = len;
    strcpy(field1.ClientPublicIP, "198.4.4.120");
    field1.ClientIPPort = 65532;
    strcpy(field1.ClientLoginTime, "11:28:29");
    strcpy(field1.ClientAppID, "Q7");
    m_pUserApi-&gt;SubmitUserSystemInfo(&amp;field1);
}
</code></pre>
<div class="sub-links-list" style="text-indent:0px;"><hr class="SubLinksListLine"/>
<p class="sub-links-list-header">请参阅：</p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../CJFAQ/">常见FAQ</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../CTP-GETSYSTEMINFO/">CTP-GetSystemInfo</a></p>
<p class="sub-links-paragraph">    <a class="sub-links-action" href="../CTP-GETDATACOLLECTAPIVERSION/">CTP-GetDataCollectApiVersion</a></p>
</div>

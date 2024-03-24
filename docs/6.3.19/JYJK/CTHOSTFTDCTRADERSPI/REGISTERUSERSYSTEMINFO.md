<p>注册用户终端信息，用于中继服务器多连接模式</p>
<p>需要在终端认证成功后，用户登录前调用该接口</p>
<span class="anchor" id="edf44840-a73e-49a3-9346-e53e0bcaff44"></span>
## 1.函数原型
<p>virtual int RegisterUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;</p>
<span class="anchor" id="b4412f3a-1333-4e83-8330-8fbfaec46f1f"></span>
## 2.参数
<p>CThostFtdcUserSystemInfoField ：用户系统信息</p>
<pre><code>struct CThostFtdcUserSystemInfoField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///用户端系统内部信息长度
    TThostFtdcSystemInfoLenType ClientSystemInfoLen;
    ///用户端系统内部信息
    TThostFtdcClientSystemInfoType ClientSystemInfo;
    ///用户公网IP
    TThostFtdcIPAddressType ClientPublicIP;
    ///终端IP端口
    TThostFtdcIPPortType ClientIPPort;
    ///登录成功时间
    TThostFtdcTimeType ClientLoginTime;
    ///App代码
    TThostFtdcAppIDType ClientAppID;
};
</code></pre>
<p>ClientSystemInfoLen：存储的为加密后的用户终端系统内部信息的长度</p>
<p>ClientSystemInfo：存储的为加密后的用户终端系统内部信息。</p>
<p>ClientPublicIP：存储的为用户终端IP，由中继服务器采集和填写</p>
<p>ClientLoginTime：存储的为用户登录中继时间，由中继服务器采集和填写</p>
<p>ClientAppid：存储的为用户终端的appid，由中继服务器采集和填写</p>
<span class="anchor" id="1b586036-05c7-4b15-8b04-2f8db7eac2f3"></span>
## 3.返回
<p>0 正确</p>
<p>-1 字段长度不对</p>
<p>-2 非CTP采集的终端信息</p>
<p>-3 当前终端类型非多对多中继</p>
<p>-5 字段中存在非法字符或者长度超限</p>
<p>-6 采集结果字段错误</p>
<span class="anchor" id="d99b8005-9b4c-428f-987b-58e0d4a1eb90"></span>
## 4.调用示例
<p>//多对多中继终端使用流程</p>
<p class="step-para"><span class="step-mark">Step 1</span> 终端侧采集信息 向中继发起登录 并将终端信息发送给中继</p>
<pre><code>char pSystemInfo[344];
int len;
CTP_GetSystemInfo(pSystemInfo, len);
</code></pre>
<p class="step-para"><span class="step-mark">Step 2</span> 中继收到终端的登录请求，发起终端认证</p>
<pre><code>ReqAuthenticate();
</code></pre>
<p class="step-para"><span class="step-mark">Step 3</span> 终端认证成功后，中继上报用户信息</p>
<pre><code>RegisterUserSystemInfo()
{
    char pSystemInfo[344];
    int len;
    ////将从终端得到的信息赋值给下面结构体
    CThostFtdcUserSystemInfoField field;
    memset(&amp;field, 0, sizeof(field));
    strcpy(field.BrokerID, "9999");
    strcpy(field.UserID, "00001");
    memcpy(field.ClientSystemInfo, pSystemInfo, len);
    field.ClientSystemInfoLen = len;
    strcpy(field.ClientPublicIP, "127.0.0.1");
    field.ClientIPPort = 65535;
    strcpy(field.ClientLoginTime, "11:28:28");
    strcpy(field.ClientAppID, "aaa");
    m_pUserApi-&gt;RegisterUserSystemInfo(&amp;field);
}
</code></pre>
<p class="step-para"><span class="step-mark">Step 4</span> 中继上报成功后，发起登录</p>
<pre><code>ReqUserLogin();
</code></pre>
<p class="step-para"><span class="step-mark">Step 5</span> 中继登录成功</p>
<span class="anchor" id="3cf4ad48-0131-408e-b47a-926536469ebc"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">采集信息上报时候总是提示operation not permitted，这是为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>如果提示operation not permitted，可能是AppID类型错误。例如，直连模式的AppID，却错误调用了SubmitUserSystemInfo。</p>
<p>此错误不会通过特定接口返回，只在标准输出中提示，例如直接在屏幕上打印出来。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">不上报采集信息，会影响登录吗？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>不影响登录，CTP不做控制，但这样不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">多对多中继代理模式的AppID怎么填？是填RelayAppID还是ClientAppID？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>认证时用relayappid，上报时填客户端的appid。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">使用中继模式，已经认证成功了。用工具查看不到采集获得的信息，但是在代码里看到的pSystemInfo不为空的。这可能是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>采集不落库，基本上都是采集的数据在转储时被截断了。</p>
<p>一定要使用memcpy，不要把采集的数据当成字符串，他不是字符串。</p>
<p>还有一种常见错误，ClientSystemInfoLen不按照采集库的返回值填写，而是自己用strlen()之类的函数去获取。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

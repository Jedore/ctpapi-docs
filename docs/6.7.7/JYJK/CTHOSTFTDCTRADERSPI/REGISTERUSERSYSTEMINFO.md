<p>注册用户终端信息，用于中继服务器多连接模式</p>
<p>需要在终端认证成功后，用户登录前调用该接口</p>
<span class="anchor" id="d3544bec-3bcb-42b1-b4aa-c8a79edee90e"></span>
## 1.函数原型
<p>virtual int RegisterUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;</p>
<span class="anchor" id="daa42e75-a35f-4da9-9159-d21c310443a8"></span>
## 2.参数
<p>CThostFtdcUserSystemInfoField ：用户系统信息</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientSystemInfoType</td>
<td style="TEXT-ALIGN: left;">ClientSystemInfo</td>
<td style="TEXT-ALIGN: left;">用户端系统内部信息</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcIPAddressType</td>
<td style="TEXT-ALIGN: left;">ClientPublicIP</td>
<td style="TEXT-ALIGN: left;">终端IP端口</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeType</td>
<td style="TEXT-ALIGN: left;">ClientLoginTime</td>
<td style="TEXT-ALIGN: left;">登录成功时间</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAppIDType</td>
<td style="TEXT-ALIGN: left;">ClientAppID</td>
<td style="TEXT-ALIGN: left;">App代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSystemInfoLenType</td>
<td style="TEXT-ALIGN: left;">ClientSystemInfoLen</td>
<td style="TEXT-ALIGN: left;">用户端系统内部信息长度</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcIPPortType</td>
<td style="TEXT-ALIGN: left;">ClientIPPort</td>
<td style="TEXT-ALIGN: left;">终端IP端口</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldIPAddressType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientLoginRemarkType</td>
<td style="TEXT-ALIGN: left;">ClientLoginRemark</td>
<td style="TEXT-ALIGN: left;">客户登录备注2</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>ClientSystemInfoLen：存储的为加密后的用户终端系统内部信息的长度</p>
<p>ClientSystemInfo：存储的为加密后的用户终端系统内部信息。</p>
<p>ClientPublicIP：存储的为用户终端IP，由中继服务器采集和填写</p>
<p>ClientLoginTime：存储的为用户登录中继时间，由中继服务器采集和填写</p>
<p>ClientAppid：存储的为用户终端的appid，由中继服务器采集和填写</p>
<span class="anchor" id="d6a8fda3-a17b-4a3a-b77c-74e1c6429060"></span>
## 3.返回
<p>0 正确</p>
<p>-1 字段长度不对</p>
<p>-2 非CTP采集的终端信息</p>
<p>-3 当前终端类型非多对多中继</p>
<p>-5 字段中存在非法字符或者长度超限</p>
<p>-6 采集结果字段错误</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>-7 采集库的版本类型和生产库的不一致</p>
<span class="anchor" id="3ff41343-282b-4c1e-9c81-ee64be6627b3"></span>
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
<span class="anchor" id="28067ae6-4195-477e-99cd-06b0a6c3c1ef"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">采集信息上报时候总是提示operation not permitted，这是为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>如果提示operation not permitted，可能是AppID类型错误。例如，直连模式的AppID，却错误调用了<a href="../SUBMITUSERSYSTEMINFO/">SubmitUserSystemInfo</a>。</p>
<p>此错误不会通过特定接口返回，只在标准输出中提示，例如直接在屏幕上打印出来。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">不上报采集信息，会影响登录吗？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>不影响登录，CTP不做控制，但这样不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">多对多中继代理模式的AppID怎么填？是填RelayAppID还是ClientAppID？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>认证时用relayappid，上报时填客户端的appid。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">使用中继模式，已经认证成功了。用工具查看不到采集获得的信息，但是在代码里看到的pSystemInfo不为空的。这可能是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>采集不落库，基本上都是采集的数据在转储时被截断了。</p>
<p>一定要使用memcpy，不要把采集的数据当成字符串，他不是字符串。</p>
<p>还有一种常见错误，ClientSystemInfoLen不按照采集库的返回值填写，而是自己用strlen()之类的函数去获取。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

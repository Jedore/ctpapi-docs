<p>上报用户终端信息，用于中继服务器操作员登录模式，操作员登录后，可以多次调用该接口上报不同客户信息。</p>
<span class="anchor" id="3e704f3d-ebdb-4754-843d-532be66c9fa7"></span>
## 1.函数原型
<p>virtual int SubmitUserSystemInfo(CThostFtdcUserSystemInfoField *pUserSystemInfo) = 0;</p>
<span class="anchor" id="392c8453-f319-4e70-83cc-996112c35cad"></span>
## 2.参数
<p>pUserSystemInfo：用户系统信息</p>
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
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientLoginRemarkType</td>
<td style="TEXT-ALIGN: left;">ClientLoginRemark</td>
<td style="TEXT-ALIGN: left;">客户登录备注2</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>UserID：此处应该填终端的投资者账号，即InvestorID，而非操作员账号。</p>
<p>ClientSystemInfoLen：加密后的用户终端系统内部信息的长度</p>
<p>ClientSystemInfo：加密后的用户终端系统内部信息。</p>
<p>ClientPublicIP：用户终端IP，由中继服务器采集和填写</p>
<p>ClientLoginTime：用户登录中继时间，由中继服务器采集和填写</p>
<p>ClientAppid：用户终端的appid，由中继服务器采集和填写</p>
<span class="anchor" id="1eb31956-d1e2-4c8d-9b2d-96bc6a8b2e42"></span>
## 3.返回
<p>0 正确</p>
<p>-1 字段长度不对</p>
<p>-2 非CTP采集的终端信息</p>
<p>-4 当前用户非一对多操作员</p>
<p>-5 字段中存在非法字符或者长度超限</p>
<p>-6 采集结果字段错误</p>
<span class="anchor" id="53dfbf53-b308-465e-8d52-0ddf2f6cc50f"></span>
## 4.调用示例
<p>//一对多中继终端使用方法   </p>
<p class="step-para"><span class="step-mark">Step 1</span> 中继在启动后，在API连接后发起认证</p>
<pre><code>Authenticate();
</code></pre>
<p class="step-para"><span class="step-mark">Step 2</span> 认证成功后发起登录</p>
<pre><code>UserLogin();
</code></pre>
<p class="step-para"><span class="step-mark">Step 3</span> 终端登录中继时，中继上报用户终端信息</p>
<pre><code>char pSystemInfo[344];
  int len;
  CTP_GetSystemInfo(pSystemInfo, len);
  CThostFtdcUserSystemInfoField field1;
  memset(&amp;field1, 0, sizeof(field));
  strcpy(field1.BrokerID, "9999");
  strcpy(field1.UserID, "00001");
  memcpy(field1.ClientSystemInfo, pSystemInfo, len);
  field1.ClientSystemInfoLen = len;
  strcpy(field1.ClientPublicIP, "127.0.0.1");
  field1.ClientIPPort = 65535;
  strcpy(field1.ClientLoginTime, "11:28:28");
  strcpy(field1.ClientAppID, "Q7");
  m_pUserApi-&gt;SubmitUserSystemInfo(&amp;field1);
</code></pre>
<span class="anchor" id="482a6b73-c595-4d9b-b5d5-73e11350aa9e"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">采集信息上报时候总是提示operation not permitted，这是为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>如果提示operation not permitted，可能是AppID类型错误。例如，直连模式的AppID，却错误调用了SubmitUserSystemInfo。</p>
<p>此错误不会通过特定接口返回，只在标准输出中提示，例如直接在屏幕上打印出来。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">不上报采集信息，会影响登录吗？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>不影响登录，CTP不做控制，但这样不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">一对多模式下，如果认证成功后，密码输错导致登录失败了，是否要退出登录，重新认证和登录？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>要退出登录，重新认证和登录。否则继续登录的话会导致submitusersysinfo调用失败！</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

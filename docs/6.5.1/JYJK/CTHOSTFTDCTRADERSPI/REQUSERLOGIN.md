<p>用户登录请求，对应响应OnRspUserLogin。</p>
<span class="anchor" id="6cab8f86-ea38-4b4f-9f59-6abedab0cb1c"></span>
## 1.函数原型
<p>virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;</p>
<span class="anchor" id="603bc76b-6646-46b4-ac4b-d2b8bb675ec4"></span>
## 2.参数
<p>pReqUserLoginField：用户登录请求</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcDateType</td>
<td style="TEXT-ALIGN: left;">TradingDay</td>
<td style="TEXT-ALIGN: left;">交易日</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPasswordType</td>
<td style="TEXT-ALIGN: left;">Password</td>
<td style="TEXT-ALIGN: left;">密码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductInfoType</td>
<td style="TEXT-ALIGN: left;">UserProductInfo</td>
<td style="TEXT-ALIGN: left;">用户端产品信息</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductInfoType</td>
<td style="TEXT-ALIGN: left;">InterfaceProductInfo</td>
<td style="TEXT-ALIGN: left;">接口端产品信息</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProtocolInfoType</td>
<td style="TEXT-ALIGN: left;">ProtocolInfo</td>
<td style="TEXT-ALIGN: left;">协议信息</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcMacAddressType</td>
<td style="TEXT-ALIGN: left;">MacAddress</td>
<td style="TEXT-ALIGN: left;">Mac地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPasswordType</td>
<td style="TEXT-ALIGN: left;">OneTimePassword</td>
<td style="TEXT-ALIGN: left;">动态密码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldIPAddressType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcIPAddressType</td>
<td style="TEXT-ALIGN: left;">ClientIPAddress</td>
<td style="TEXT-ALIGN: left;">终端IP地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcLoginRemarkType</td>
<td style="TEXT-ALIGN: left;">LoginRemark</td>
<td style="TEXT-ALIGN: left;">登录备注</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcIPPortType</td>
<td style="TEXT-ALIGN: left;">ClientIPPort</td>
<td style="TEXT-ALIGN: left;">终端IP端口</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>UserID：操作员代码，之后的investorid需要属于该操作员管理下。</p>
<p>UserProductInfo：客户端的产品信息，如软件开发商、版本号等。</p>
<p>用户事件中的UserProductInfo取决于认证填写的值，而非登录。</p>
<blockquote>
<p>例如：SFITTraderV100。</p>
</blockquote>
<p>LoginRemark：可以写登录备注，能够被交易系统的日志查询到。</p>
<p>OneTimePassword：如果期货公司启用了动态口令，客户会有一个电子口令牌，把生成的值，输入到登录报文里的OneTimePassword(动态密码)这个字段中去即可</p>
<p>ClientIPAddress：CTP前置主动获取，填写无效。</p>
<p>MacAddress：API采集，填写无效。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e203063a-6ff7-429c-83b7-b2a99f99f3a2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b046d2c7-1446-4d5d-90f0-74ac52c1b66c"></span>
## 4.调用示例
<pre><code>CThostFtdcReqUserLoginField reqUserLogin = { 0 };
strcpy_s(reqUserLogin.BrokerID, “0000”);
strcpy_s(reqUserLogin.UserID, “00001”);
strcpy_s(reqUserLogin.Password, “123456”); 
m_pUserApi-&gt;ReqUserLogin(&amp;reqUserLogin, nRequestID++);
</code></pre>
<span class="anchor" id="9a2079b0-cee1-4cbb-8e3b-41b51ebb7be5"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">现在投资者登录的时候，有时候会被锁定，请问会有什么原因？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>CTP有单独锁IP的功能。被锁定的情况下继续登录会报“CTP：登录失败次数超限，IP被禁止”。目前这个阈值一般设置为5000，单个交易日内累积计算。</p>
<p>CTP有锁IP+账号的功能。被锁定的情况下继续登录会报“CTP：连续登录失败次数超限，登录被禁止”。目前这个阈值一般设置为6-10，注意这里的登录错误次数CTP是连续计算的。</p>
<p>具体的阈值以期货公司设置的为准。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">首次登陆如果提示修改密码，如何修改？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>首次登陆如果提示修改密码，则必须在<code>当前会话</code>调用ReqUserPasswordUpdate来修改密码。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:用户在线会话超出上限”是什么意思？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>表示该UserID的同时在线会话数超出了期货公司设置的阈值，具体阈值咨询期货公司柜台设置。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">登录报“CTP：重复的登录”，是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>正常情况下，收到登录成功的响应后再发起登录，是没有响应的，这是因为如果前置收到登陆成功的响应，则会过滤后续的相同Session的登陆请求。</p>
<p>极端情况下，当前置还没收到核心返回的登录成功响应，而此时又再次收到来自客户端的登录请求，就不会过滤，核心收到重复的登录请求后就会返回“CTP：重复的登录”的错误响应。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_5" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">登录时候报错：“CTP：连续登录失败数超限，登录被禁止”，为什么？</p><div class="region_panel" id="region_panel_5" style="display:block;"><table><tr><td>
<p>此报错说明用户连续输错密码被禁止登录了，ip被锁定。此时用户换ip或者联系期货公司解锁即可。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_5" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

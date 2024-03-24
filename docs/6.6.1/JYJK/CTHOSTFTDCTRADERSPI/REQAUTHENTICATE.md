<p>客户端认证请求，对应响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPAUTHENTICATE/">OnRspAuthenticate</a>。如果交易系统开启了强制终端认证，则必须认证通过后才能发起登陆；如果未开启，则不需要认证即可登陆，此时如果主动去认证，不管成功或失败，也不影响后续登陆。</p>
<span class="anchor" id="be192f7c-486d-48a4-8628-d05192a73180"></span>
## 1.函数原型
<p>virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) = 0;</p>
<span class="anchor" id="74197e30-5a21-4b81-96f9-f62e9e629c25"></span>
## 2.参数
<p>pReqAuthenticateField：客户端认证请求</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductInfoType</td>
<td style="TEXT-ALIGN: left;">UserProductInfo</td>
<td style="TEXT-ALIGN: left;">用户端产品信息</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAuthCodeType</td>
<td style="TEXT-ALIGN: left;">AuthCode</td>
<td style="TEXT-ALIGN: left;">认证码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAppIDType</td>
<td style="TEXT-ALIGN: left;">AppID</td>
<td style="TEXT-ALIGN: left;">App代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
</table>
<p>UserProductInfo：客户端的产品信息，如软件开发商、版本号等。</p>
<blockquote>
<p>CTP后台用户事件中的用户登录事件所显示的用户端产品信息取自ReqAuthentication接口里的UserProductInfo，而非<a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGIN/">ReqUserLogin</a>里的。</p>
</blockquote>
<p>AuthCode：认证码需要向期货公司申请得到</p>
<p>AppID：<strong><font color="#FF0000">必填项</font></strong>，不然认证失败，如果没有则要向期货公司申请，申请的AppID必须遵循监控中心规范格式</p>
<p>UserID：<strong><font color="#FF0000">必填项</font></strong>，用户代码。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="6b5753ed-10f2-463e-8a5c-8dab37a9c203"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9ec6c6c0-4bc8-474c-be0f-38f927a8afbd"></span>
## 4.调用示例
<pre><code>CThostFtdcReqAuthenticateField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.UserProductInfo, "mytest");
strcpy_s(a.AuthCode, "MLX0LEA4L4UPUCBF"); 
strcpy_s(a.AppID, "mytest");
m_pUserApi-&gt;ReqAuthenticate(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="b68f5a8d-ef4e-49b8-ba48-d2d07e39e659"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">每次重连都需要做一遍客户端认证吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>重新连接都需要重新认证一下。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">非穿透式版本，开通了强制认证，需要申请一个认证码的。穿透式版本，也需要一个穿透式的认证码。如果想同时开通非穿透式强制认证和穿透式认证，这样就要两个认证码；但API里是只需要一个认证码，那请问这种情况怎么解决？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>这种场景是不存在的，因为穿透式和非穿透式版本的api互不兼容，所以不存在用一个api去同时做新旧前置的认证。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">在使用“看穿式监管信息采集评测工具”时候，发现获取到的记录数和数据库中信息的条目数不匹配。这是为什么？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>数据库中的记录为乱码的话就不显示。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">采集信息库是否是线程安全的？能多个线程同时调用吗？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>不是线程安全的，不能同时调用。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

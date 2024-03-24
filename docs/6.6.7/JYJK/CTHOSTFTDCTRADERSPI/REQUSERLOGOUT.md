<p>登出请求，对应响应<a href="../../../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>。</p>
<span class="anchor" id="f69e1ed9-107c-4643-94d8-03ffb792581f"></span>
## 1.函数原型
<p>virtual int <a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGOUT/">ReqUserLogout</a>(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;</p>
<span class="anchor" id="0c18c289-4feb-41cf-a6eb-1c4b7f27cc14"></span>
## 2.参数
<p>pUserLogout：用户登出请求</p>
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
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="49167c1c-8dc7-43a9-8ec3-a4b9f94f5758"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="66c8a00b-e1e7-472e-8dd6-2c3389a6c4a1"></span>
## 4.调用示例
<pre><code>CThostFtdcUserLogoutField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.UserID, "1000001");
m_pUserApi-&gt;ReqUserLogout(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="407d3041-16e7-40c8-976a-6fd8a9ccbb9a"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">用户调用<a href="../../../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGOUT/">ReqUserLogout</a>后是否会自动重连？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>会，Logout后，触发<a href="../../CTHOSTFTDCTRADERAPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>，能自动<a href="../../CTHOSTFTDCTRADERAPI/ONFRONTCONNECTED/">OnFrontConnected</a>。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

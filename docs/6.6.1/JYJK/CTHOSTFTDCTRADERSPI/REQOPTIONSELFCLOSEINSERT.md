<p>期权自对冲录入请求</p>
<p>错误响应: <a href="../../CTHOSTFTDCTRADERAPI/ONERRRTNOPTIONSELFCLOSEINSERT/">OnErrRtnOptionSelfCloseInsert</a>，<a href="../../CTHOSTFTDCTRADERAPI/ONRSPOPTIONSELFCLOSEINSERT/">OnRspOptionSelfCloseInsert</a></p>
<p>正确响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a></p>
<span class="anchor" id="927d0c3e-0b85-4a6b-8843-bbdfc481bcea"></span>
## 1.函数原型
<p>virtual int ReqOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID) = 0;</p>
<span class="anchor" id="d45ef4df-9cab-424e-acf6-66afe7b54521"></span>
## 2.参数
<p>pInputOptionSelfClose：输入的期权自对冲</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">OptionSelfCloseRef</td>
<td style="TEXT-ALIGN: left;">期权自对冲引用</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBusinessUnitType</td>
<td style="TEXT-ALIGN: left;">BusinessUnit</td>
<td style="TEXT-ALIGN: left;">业务单元</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientIDType</td>
<td style="TEXT-ALIGN: left;">ClientID</td>
<td style="TEXT-ALIGN: left;">客户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcIPAddressType</td>
<td style="TEXT-ALIGN: left;">IPAddress</td>
<td style="TEXT-ALIGN: left;">IP地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcMacAddressType</td>
<td style="TEXT-ALIGN: left;">MacAddress</td>
<td style="TEXT-ALIGN: left;">Mac地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">Volume</td>
<td style="TEXT-ALIGN: left;">数量</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcRequestIDType</td>
<td style="TEXT-ALIGN: left;">RequestID</td>
<td style="TEXT-ALIGN: left;">请求编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">HedgeFlag</td>
<td style="TEXT-ALIGN: left;">投机套保标志</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOptSelfCloseFlagType</td>
<td style="TEXT-ALIGN: left;">OptSelfCloseFlag</td>
<td style="TEXT-ALIGN: left;">期权行权的头寸是否自对冲</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">1自对冲期权仓位、2保留期权仓位、3自对冲卖方履约后的期货仓位</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldIPAddressType</td>
<td style="TEXT-ALIGN: left;">reserve2</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>OptionSelfCloseRef：需要纯数字递增，不填则ctp自动填写</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="143c7d3a-2aba-483a-8428-db59bcd46e93"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5469909d-8b8a-4d59-b1ae-a8b3566278cc"></span>
## 4.调用示例
<pre><code>CThostFtdcInputOptionSelfCloseField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.UserID, "1000001");
a.Volume = 1;
a.HedgeFlag = THOST_FTDC_HF_Speculation;
a.OptSelfCloseFlag = THOST_FTDC_OSCF_CloseSelfOptionPosition;
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqOptionSelfCloseInsert(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="92968e2b-ce8e-49d0-9012-106a5980b61d"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为什么报入的OptionSelfCloseRef和返回的值不同？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>根据交易所规则，自对冲报单由首次报入的报单属性确定，之后不论是否对该报单进行任何操作（包括撤单和重新报单），报单的OptionSelfCloseRef都不变。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

<p>报价操作请求，用于撤销报价</p>
<p>错误响应:<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQUOTEACTION/">OnRspQuoteAction</a> <a href="../../CTHOSTFTDCTRADERAPI/ONERRRTNQUOTEACTION/">OnErrRtnQuoteAction</a></p>
<p>正确响应:<a href="../../CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a> <a href="../../CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a></p>
<span class="anchor" id="ee08b283-7744-4e3d-868f-f832fa2fa506"></span>
## 1.函数原型
<p>virtual int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) = 0;</p>
<span class="anchor" id="2ada7b24-d8d5-496c-816f-8021e4e38af9"></span>
## 2.参数
<p>pInputQuoteAction：输入报价操作</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*2</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">QuoteRef</td>
<td style="TEXT-ALIGN: left;">报价引用</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*2</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">QuoteSysID</td>
<td style="TEXT-ALIGN: left;">报价编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*2</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderActionRefType</td>
<td style="TEXT-ALIGN: left;">QuoteActionRef</td>
<td style="TEXT-ALIGN: left;">报价操作引用</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcRequestIDType</td>
<td style="TEXT-ALIGN: left;">RequestID</td>
<td style="TEXT-ALIGN: left;">请求编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcFrontIDType</td>
<td style="TEXT-ALIGN: left;">FrontID</td>
<td style="TEXT-ALIGN: left;">前置编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSessionIDType</td>
<td style="TEXT-ALIGN: left;">SessionID</td>
<td style="TEXT-ALIGN: left;">会话编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcActionFlagType</td>
<td style="TEXT-ALIGN: left;">ActionFlag</td>
<td style="TEXT-ALIGN: left;">操作标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
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
<p><strong><font color="#FF0000">必填*1、必填*2</font></strong>：两组选一组必填，能对应要撤的报价单。</p>
<p>FrontID：对应要撤销的报价的前置编号</p>
<p>SessionID：对应要撤销的报价的会话编号</p>
<p>QuoteSysID: 对应要撤销的报价的编号</p>
<p>ActionFlag：操作标志，支持删除，目前不支持改单。想实现改单操作可以先撤销之后再重新报单。</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="8b7b6e9f-76d6-4880-9dc2-bef8bb1e64d7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8733dc02-175e-44f4-a52a-0b51257634d5"></span>
## 4.调用示例
<pre><code>CThostFtdcInputQuoteActionField t = { 0 };
strcpy_s(t.BrokerID, "9999");
strcpy_s(t.InvestorID, "1000001");
strcpy_s(t.UserID, "1000001");
strcpy_s(t.ExchangeID, "SHFE");
strcpy_s(t.QuoteRef, "           1");
t.FrontID = 1;
t.SessionID = 6442531;
t.ActionFlag = THOST_FTDC_AF_Delete;
strcpy_s(t.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQuoteAction(&amp;t, nRequestID++);
</code></pre>
<span class="anchor" id="127ffe06-3882-41d3-8b81-02522d13b202"></span>
## 5.FAQ
<p>无</p>

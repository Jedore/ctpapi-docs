<p>执行宣告操作请求</p>
<p>错误响应: <a href="../../CTHOSTFTDCTRADERAPI/ONERRRTNEXECORDERACTION/">OnErrRtnExecOrderAction</a>，<a href="../../CTHOSTFTDCTRADERAPI/ONRSPEXECORDERACTION/">OnRspExecOrderAction</a></p>
<p>正确响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRTNEXECORDER/">OnRtnExecOrder</a></p>
<span class="anchor" id="fa66daf9-cb73-40ed-be30-04fcf3b30659"></span>
## 1.函数原型
<p>virtual int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="e8191255-7d0a-4152-bf7d-9fb77503523a"></span>
## 2.参数
<p>pInputExecOrderAction：输入执行宣告操作</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">ExecOrderRef</td>
<td style="TEXT-ALIGN: left;">报单引用</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExecOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">ExecOrderSysID</td>
<td style="TEXT-ALIGN: left;">执行宣告操作编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">与执行宣告记录该编号一致</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
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
<td style="TEXT-ALIGN: left;">ExecOrderActionRef</td>
<td style="TEXT-ALIGN: left;">报单操作引用</td>
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
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSessionIDType</td>
<td style="TEXT-ALIGN: left;">SessionID</td>
<td style="TEXT-ALIGN: left;">会话编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcActionFlagType</td>
<td style="TEXT-ALIGN: left;">ActionFlag</td>
<td style="TEXT-ALIGN: left;">操作标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">删除</font></strong></td>
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
<p>ActionFlag：只支持删除，不支持修改</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e7c358f1-ceca-40e5-bb55-cc71623ab903"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a865a86b-b84c-40fc-96c6-80851a75be71"></span>
## 4.调用示例
<pre><code>CThostFtdcInputExecOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
a.ExecOrderActionRef = 1;
strcpy_s(a.ExecOrderRef, "00000003");
a.FrontID = 1;
a.SessionID = -7844256;
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.ExecOrderSysID, "         285");
a.ActionFlag = THOST_FTDC_AF_Delete;//删除
strcpy_s(a.UserID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqExecOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="b1717cdf-b7b7-46da-9e36-8c53c9e842b1"></span>
## 5.FAQ
<p>无</p>

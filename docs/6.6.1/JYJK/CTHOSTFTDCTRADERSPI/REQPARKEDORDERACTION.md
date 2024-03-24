<p>预埋撤单录入请求</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYPARKEDORDERACTION/">OnRspQryParkedOrderAction</a></p>
<span class="anchor" id="3c38d215-e645-49a9-a961-8a1073748d6f"></span>
## 1.函数原型
<p>virtual int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="c899a270-5c3f-4fc6-b8f7-864fb01aa7bf"></span>
## 2.参数
<p>pParkedOrderAction：输入预埋单操作</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">OrderRef</td>
<td style="TEXT-ALIGN: left;">报单引用</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">OrderSysID</td>
<td style="TEXT-ALIGN: left;">报单编号</td>
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
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcParkedOrderActionIDType</td>
<td style="TEXT-ALIGN: left;">ParkedOrderActionID</td>
<td style="TEXT-ALIGN: left;">预埋撤单单编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcErrorMsgType</td>
<td style="TEXT-ALIGN: left;">ErrorMsg</td>
<td style="TEXT-ALIGN: left;">错误信息</td>
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
<td style="TEXT-ALIGN: left;">OrderActionRef</td>
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
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSessionIDType</td>
<td style="TEXT-ALIGN: left;">SessionID</td>
<td style="TEXT-ALIGN: left;">会话编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">VolumeChange</td>
<td style="TEXT-ALIGN: left;">数量变化</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcErrorIDType</td>
<td style="TEXT-ALIGN: left;">ErrorID</td>
<td style="TEXT-ALIGN: left;">错误代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcActionFlagType</td>
<td style="TEXT-ALIGN: left;">ActionFlag</td>
<td style="TEXT-ALIGN: left;">操作标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserTypeType</td>
<td style="TEXT-ALIGN: left;">UserType</td>
<td style="TEXT-ALIGN: left;">用户类型</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcParkedOrderStatusType</td>
<td style="TEXT-ALIGN: left;">Status</td>
<td style="TEXT-ALIGN: left;">预埋单状态</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">LimitPrice</td>
<td style="TEXT-ALIGN: left;">价格</td>
<td style="TEXT-ALIGN: left;">无</td>
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
<p><strong><font color="#FF0000">必填*1、必填*2</font></strong>：两组选一组必填，能对应要撤的报单。</p>
<p>OrderRef：对应要撤销的那笔报单的报单引用</p>
<p>FrontID: 对应要撤销的那笔报单的前置编号</p>
<p>SessionID: 对应要撤销的那笔报单的会话编号</p>
<p>ExchangeID: 对应要撤销的那笔报单的交易所ID</p>
<p>OrderSysID: 对应要撤销的那笔报单的报单编号</p>
<p>ActionFlag：只支持删除，不支持修改</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="87425520-364c-4d7f-9e7d-d5691795a914"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5df02894-2f39-4811-ade5-a10312c21091"></span>
## 4.调用示例
<pre><code>CThostFtdcParkedOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.OrderSysID, "    10061782"); 
strcpy_s(a.UserID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
ActionFlag = THOST_FTDC_AF_Delete;
m_pUserApi-&gt;ReqParkedOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="294ecc49-5f43-4081-883c-7c272a4fbbee"></span>
## 5.FAQ
<p>无</p>

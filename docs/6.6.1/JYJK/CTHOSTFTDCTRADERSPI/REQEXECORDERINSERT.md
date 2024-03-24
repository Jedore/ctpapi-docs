<p>执行宣告录入请求</p>
<p>错误响应: <a href="../../CTHOSTFTDCTRADERAPI/ONERRRTNEXECORDERINSERT/">OnErrRtnExecOrderInsert</a>，<a href="../../CTHOSTFTDCTRADERAPI/ONRSPEXECORDERINSERT/">OnRspExecOrderInsert</a></p>
<p>正确响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRTNEXECORDER/">OnRtnExecOrder</a></p>
<span class="anchor" id="50e42635-e7c7-400f-9e24-c6fc2cbeac42"></span>
## 1.函数原型
<p>virtual int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) = 0;</p>
<span class="anchor" id="d6414525-59cf-4c53-ad9d-d2a825e23e5b"></span>
## 2.参数
<p>pInputExecOrder：输入的执行宣告</p>
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
<td style="TEXT-ALIGN: left;">ExecOrderRef</td>
<td style="TEXT-ALIGN: left;">执行宣告引用</td>
<td style="TEXT-ALIGN: left;">选填</td>
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
<td style="TEXT-ALIGN: left;">无</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOffsetFlagType</td>
<td style="TEXT-ALIGN: left;">OffsetFlag</td>
<td style="TEXT-ALIGN: left;">开平标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">HedgeFlag</td>
<td style="TEXT-ALIGN: left;">投机套保标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">投机或套保</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcActionTypeType</td>
<td style="TEXT-ALIGN: left;">ActionType</td>
<td style="TEXT-ALIGN: left;">执行类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPosiDirectionType</td>
<td style="TEXT-ALIGN: left;">PosiDirection</td>
<td style="TEXT-ALIGN: left;">保留头寸申请的持仓方向</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">多头</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExecOrderPositionFlagType</td>
<td style="TEXT-ALIGN: left;">ReservePositionFlag</td>
<td style="TEXT-ALIGN: left;">期权行权后是否保留期货头寸的标记,该字段已废弃</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">该字段已废弃，调用时不能为空</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExecOrderCloseFlagType</td>
<td style="TEXT-ALIGN: left;">CloseFlag</td>
<td style="TEXT-ALIGN: left;">期权行权后生成的头寸是否自动平仓</td>
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
<p>ExecOrderRef：需要纯数字递增，不填则ctp自动填写</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3b2b6486-0f04-4723-9465-612599dcfbae"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ab711982-4c00-43c7-8fd8-c543c87edee9"></span>
## 4.调用示例
<pre><code>CThostFtdcInputExecOrderField OrderInsert = { 0 };
strcpy_s(OrderInsert.BrokerID, "9999");
strcpy_s(OrderInsert.InvestorID, "1000001");
strcpy_s(OrderInsert.InstrumentID, "rb1809");
strcpy_s(OrderInsert.ExchangeID, "SHFE");
strcpy_s(OrderInsert.ExecOrderRef, "00001");
strcpy_s(OrderInsert.UserID, "1000001");
OrderInsert.Volume = 1;
OrderInsert.RequestID = 1; 
OrderInsert.OffsetFlag = THOST_FTDC_OF_Close;//开平标志
OrderInsert.HedgeFlag = THOST_FTDC_HF_Speculation;//投机套保标志
OrderInsert.ActionType = THOST_FTDC_ACTP_Exec;//执行类型类型
OrderInsert.PosiDirection = THOST_FTDC_PD_Long;//持仓多空方向类型
OrderInsert.ReservePositionFlag = THOST_FTDC_EOPF_Reserve;//期权行权后是否保留期货头寸的标记类型
OrderInsert.CloseFlag = THOST_FTDC_EOCF_NotToClose;//期权行权后生成的头寸是否自动平仓类型
m_pUserApi-&gt;ReqExecOrderInsert(&amp;OrderInsert, nRequestID++);
</code></pre>
<span class="anchor" id="51340c46-a533-4fdf-9fc7-bc489927ee02"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">盘中通过api进行中金所行权，报错“CTP:不支持的功能”为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>中金所不支持通过api行权，只能盘后通过会服提交行权申请。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>

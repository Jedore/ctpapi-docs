<p>预埋单录入请求</p>
<p>注意：由于交易所不推送组合合约的开盘信号，而服务器预埋单依赖交易所合约开盘信号触发，所以服务器预埋单暂不支持下组合合约。</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPPARKEDORDERINSERT/">OnRspParkedOrderInsert</a></p>
<span class="anchor" id="ad2ba52c-ccaf-4329-82c1-9328f90b9310"></span>
## 1.函数原型
<p>virtual int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) = 0;</p>
<span class="anchor" id="bf6b0eba-9194-4cff-9a08-ed9f3346a47a"></span>
## 2.参数
<p>pParkedOrder：预埋单</p>
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
<td style="TEXT-ALIGN: left;">OrderRef</td>
<td style="TEXT-ALIGN: left;">报单引用</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">自定义或不填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCombOffsetFlagType</td>
<td style="TEXT-ALIGN: left;">CombOffsetFlag</td>
<td style="TEXT-ALIGN: left;">开平标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCombHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">CombHedgeFlag</td>
<td style="TEXT-ALIGN: left;">投机套保标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcDateType</td>
<td style="TEXT-ALIGN: left;">GTDDate</td>
<td style="TEXT-ALIGN: left;">GTD日期</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcParkedOrderIDType</td>
<td style="TEXT-ALIGN: left;">ParkedOrderID</td>
<td style="TEXT-ALIGN: left;">预埋报单编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcErrorMsgType</td>
<td style="TEXT-ALIGN: left;">ErrorMsg</td>
<td style="TEXT-ALIGN: left;">错误信息</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">VolumeTotalOriginal</td>
<td style="TEXT-ALIGN: left;">数量</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">MinVolume</td>
<td style="TEXT-ALIGN: left;">最小成交量</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBoolType</td>
<td style="TEXT-ALIGN: left;">IsAutoSuspend</td>
<td style="TEXT-ALIGN: left;">自动挂起标志</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcRequestIDType</td>
<td style="TEXT-ALIGN: left;">RequestID</td>
<td style="TEXT-ALIGN: left;">请求编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBoolType</td>
<td style="TEXT-ALIGN: left;">UserForceClose</td>
<td style="TEXT-ALIGN: left;">用户强评标志</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcErrorIDType</td>
<td style="TEXT-ALIGN: left;">ErrorID</td>
<td style="TEXT-ALIGN: left;">错误代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBoolType</td>
<td style="TEXT-ALIGN: left;">IsSwapOrder</td>
<td style="TEXT-ALIGN: left;">互换单标志</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderPriceTypeType</td>
<td style="TEXT-ALIGN: left;">OrderPriceType</td>
<td style="TEXT-ALIGN: left;">报单价格条件</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">限价</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcDirectionType</td>
<td style="TEXT-ALIGN: left;">Direction</td>
<td style="TEXT-ALIGN: left;">买卖方向</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeConditionType</td>
<td style="TEXT-ALIGN: left;">TimeCondition</td>
<td style="TEXT-ALIGN: left;">有效期类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">当日有效</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeConditionType</td>
<td style="TEXT-ALIGN: left;">VolumeCondition</td>
<td style="TEXT-ALIGN: left;">成交量类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">任何数量</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcContingentConditionType</td>
<td style="TEXT-ALIGN: left;">ContingentCondition</td>
<td style="TEXT-ALIGN: left;">触发条件</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">立即</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcForceCloseReasonType</td>
<td style="TEXT-ALIGN: left;">ForceCloseReason</td>
<td style="TEXT-ALIGN: left;">强平原因</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">非强平</font></strong></td>
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
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">StopPrice</td>
<td style="TEXT-ALIGN: left;">止损价</td>
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
<p>OrderRef：OrderRef是本地会话全局唯一编号，必须保持递增；可由用户维护，也可由系统自动填写。一定为数字。</p>
<p>OrderPriceType：确定输入的报单类型，比如限价单则填写<code>THOST_FTDC_OPT_LimitPrice</code>、市价单则填写<code>THOST_FTDC_OPT_AnyPrice</code>。</p>
<p>Direction：确定买卖方向</p>
<p>CombOffsetFlag：确定开平标志。注:上期所、能源交易所有平今指令，下平仓指令和平昨指令相同</p>
<p>CombHedgeFlag：确定投机套保标志 例:投机 <code>THOST_FTDC_BHF_Speculation</code></p>
<p>TimeCondition：确定报单有效期类型 例:立即完成，否则撤销 <code>THOST_FTDC_TC_IOC</code></p>
<p>VolumeCondition：确定成交量类型</p>
<p>ContingentCondition：确定触发条件</p>
<p>StopPrice：止损价，用于条件单的触发价格</p>
<p>ForceCloseReason：一般填写<code>THOST_FTDC_FCC_NotForceClose</code> 非强平</p>
<p>IsSwapOrder：用户互换单的标志，只有互换单需要填写，是互换单的则赋值为1</p>
<p>CurrencyID：不填写默认为CNY</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="f10bc773-6d59-4bab-accf-3935f64ec8b0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3176a31d-38f8-4629-a3b7-10297d7b2a6a"></span>
## 4.调用示例
<pre><code>CThostFtdcParkedOrderField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
strcpy(a.InstrumentID, "rb1809");
strcpy(a.UserID, "1000001");
strcpy(a.ExchangeID, "SHFE");
a.OrderPriceType = THOST_FTDC_OPT_LimitPrice;
a.Direction = THOST_FTDC_D_Buy; 
strcpy(a.CombOffsetFlag, "0"); 
strcpy(a.CombHedgeFlag, "1");
a.LimitPrice = 400;
a.VolumeTotalOriginal = 1;
a.TimeCondition = THOST_FTDC_TC_GFD;
strcpy(a.GTDDate, "");
a.VolumeCondition = THOST_FTDC_VC_CV;
a.MinVolume = 0;
a.ContingentCondition = THOST_FTDC_CC_Immediately;
a.StopPrice = 0;
a.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;
a.IsAutoSuspend = 0;
m_pUserApi-&gt;ReqParkedOrderInsert(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="41e1e4f9-9585-433b-be3f-df19f8a72a7a"></span>
## 5.FAQ
<p>无</p>

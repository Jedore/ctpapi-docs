<p>预埋单录入请求</p>
<p>响应: OnRspParkedOrderInsert</p>
<span class="anchor" id="bb4c9d3e-6440-4474-b097-92e0178d4cff"></span>
## 1.函数原型
<p>virtual int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) = 0;</p>
<span class="anchor" id="9b5c1867-0a83-403d-8a7a-4958cec6cec1"></span>
## 2.参数
<p>pParkedOrder：预埋单</p>
<pre><code>struct CThostFtdcParkedOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///报单引用
    TThostFtdcOrderRefType OrderRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///报单价格条件
    TThostFtdcOrderPriceTypeType OrderPriceType;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///组合开平标志
    TThostFtdcCombOffsetFlagType CombOffsetFlag;
    ///组合投机套保标志
    TThostFtdcCombHedgeFlagType CombHedgeFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量
    TThostFtdcVolumeType VolumeTotalOriginal;
    ///有效期类型
    TThostFtdcTimeConditionType TimeCondition;
    ///GTD日期
    TThostFtdcDateType GTDDate;
    ///成交量类型
    TThostFtdcVolumeConditionType VolumeCondition;
    ///最小成交量
    TThostFtdcVolumeType MinVolume;
    ///触发条件
    TThostFtdcContingentConditionType ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
    ///强平原因
    TThostFtdcForceCloseReasonType ForceCloseReason;
    ///自动挂起标志
    TThostFtdcBoolType IsAutoSuspend;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///用户强评标志
    TThostFtdcBoolType UserForceClose;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///预埋报单编号
    TThostFtdcParkedOrderIDType ParkedOrderID;
    ///用户类型
    TThostFtdcUserTypeType UserType;
    ///预埋单状态
    TThostFtdcParkedOrderStatusType Status;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
    ///互换单标志
    TThostFtdcBoolType IsSwapOrder;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
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
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a0fbb1e4-f49e-4d36-aa51-f8c3b3a5ed7b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9eaed456-859a-4caf-9f9d-bf777845c38d"></span>
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
<span class="anchor" id="5e54228a-0310-4db4-ac58-3c06dc981100"></span>
## 5.FAQ
<p>无</p>

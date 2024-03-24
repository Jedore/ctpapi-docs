<p>请求查询报单响应，当执行ReqQryOrder后，该方法被调用。</p>
<span class="anchor" id="497567a7-682a-4fcc-8dc7-4b471bd5f14c"></span>
## 1.函数原型
<p>virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4ad546d7-2e7d-4e8c-bff0-cdbfac8c9a0b"></span>
## 2.参数
<p>pOrder：报单</p>
<pre><code>struct CThostFtdcOrderField
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
    ///本地报单编号
    TThostFtdcOrderLocalIDType OrderLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///报单提交状态
    TThostFtdcOrderSubmitStatusType OrderSubmitStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType NotifySequence;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///报单编号
    TThostFtdcOrderSysIDType OrderSysID;
    ///报单来源
    TThostFtdcOrderSourceType OrderSource;
    ///报单状态
    TThostFtdcOrderStatusType OrderStatus;
    ///报单类型
    TThostFtdcOrderTypeType OrderType;
    ///今成交数量
    TThostFtdcVolumeType VolumeTraded;
    ///剩余数量
    TThostFtdcVolumeType VolumeTotal;
    ///报单日期
    TThostFtdcDateType InsertDate;
    ///委托时间
    TThostFtdcTimeType InsertTime;
    ///激活时间
    TThostFtdcTimeType ActiveTime;
    ///挂起时间
    TThostFtdcTimeType SuspendTime;
    ///最后修改时间
    TThostFtdcTimeType UpdateTime;
    ///撤销时间
    TThostFtdcTimeType CancelTime;
    ///最后修改交易所交易员代码
    TThostFtdcTraderIDType ActiveTraderID;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
    ///序号
    TThostFtdcSequenceNoType SequenceNo;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///用户强评标志
    TThostFtdcBoolType UserForceClose;
    ///操作用户代码
    TThostFtdcUserIDType ActiveUserID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType BrokerOrderSeq;
    ///相关报单
    TThostFtdcOrderSysIDType RelativeOrderSysID;
    ///郑商所成交数量
    TThostFtdcVolumeType ZCETotalTradedVolume;
    ///互换单标志
    TThostFtdcBoolType IsSwapOrder;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="62f8dd0d-f61a-49a5-81fb-d05060de3631"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7299fc22-ffe3-4e10-bead-ec07fd9325b0"></span>
## 4.FAQ
<p>无</p>

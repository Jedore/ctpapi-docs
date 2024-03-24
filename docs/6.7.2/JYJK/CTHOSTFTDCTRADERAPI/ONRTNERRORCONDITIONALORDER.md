<p>提示条件单校验错误。</p>
<span class="anchor" id="1fe60b9f-1b15-4132-8a65-1ec75f7847f9"></span>
## 1.函数原型
<p>virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {};</p>
<span class="anchor" id="8a38d870-1766-4af8-b2af-fd1600ef3c58"></span>
## 2.参数
<p>pErrorConditionalOrder：查询错误报单操作</p>
<pre><code>struct CThostFtdcErrorConditionalOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///报单引用
    TThostFtdcOrderRefType  OrderRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///报单价格条件
    TThostFtdcOrderPriceTypeType    OrderPriceType;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///组合开平标志
    TThostFtdcCombOffsetFlagType    CombOffsetFlag;
    ///组合投机套保标志
    TThostFtdcCombHedgeFlagType CombHedgeFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量
    TThostFtdcVolumeType    VolumeTotalOriginal;
    ///有效期类型
    TThostFtdcTimeConditionType TimeCondition;
    ///GTD日期
    TThostFtdcDateType  GTDDate;
    ///成交量类型
    TThostFtdcVolumeConditionType   VolumeCondition;
    ///最小成交量
    TThostFtdcVolumeType    MinVolume;
    ///触发条件
    TThostFtdcContingentConditionType   ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
    ///强平原因
    TThostFtdcForceCloseReasonType  ForceCloseReason;
    ///自动挂起标志
    TThostFtdcBoolType  IsAutoSuspend;
    ///业务单元
    TThostFtdcBusinessUnitType  BusinessUnit;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///本地报单编号
    TThostFtdcOrderLocalIDType  OrderLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///报单提交状态
    TThostFtdcOrderSubmitStatusType OrderSubmitStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType    NotifySequence;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///报单编号
    TThostFtdcOrderSysIDType    OrderSysID;
    ///报单来源
    TThostFtdcOrderSourceType   OrderSource;
    ///报单状态
    TThostFtdcOrderStatusType   OrderStatus;
    ///报单类型
    TThostFtdcOrderTypeType OrderType;
    ///今成交数量
    TThostFtdcVolumeType    VolumeTraded;
    ///剩余数量
    TThostFtdcVolumeType    VolumeTotal;
    ///报单日期
    TThostFtdcDateType  InsertDate;
    ///委托时间
    TThostFtdcTimeType  InsertTime;
    ///激活时间
    TThostFtdcTimeType  ActiveTime;
    ///挂起时间
    TThostFtdcTimeType  SuspendTime;
    ///最后修改时间
    TThostFtdcTimeType  UpdateTime;
    ///撤销时间
    TThostFtdcTimeType  CancelTime;
    ///最后修改交易所交易员代码
    TThostFtdcTraderIDType  ActiveTraderID;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
    ///序号
    TThostFtdcSequenceNoType    SequenceNo;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///用户端产品信息
    TThostFtdcProductInfoType   UserProductInfo;
    ///状态信息
    TThostFtdcErrorMsgType  StatusMsg;
    ///用户强评标志
    TThostFtdcBoolType  UserForceClose;
    ///操作用户代码
    TThostFtdcUserIDType    ActiveUserID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType    BrokerOrderSeq;
    ///相关报单
    TThostFtdcOrderSysIDType    RelativeOrderSysID;
    ///郑商所成交数量
    TThostFtdcVolumeType    ZCETotalTradedVolume;
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
    ///互换单标志
    TThostFtdcBoolType  IsSwapOrder;
    ///营业部编号
    TThostFtdcBranchIDType  BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType    CurrencyID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve3;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
};
</code></pre>
<p>StopPrice：条件单触发价格</p>
<p>ForceCloseReason：填0“非强平”</p>
<p>InstallID：CTP内部使用</p>
<p>OrderSubmitStatus：报单提交状态，查看是否通过ctp校验</p>
<p>OrderStatus：报单最终状态</p>
<p>ActiveTraderID：是从交易所收回来，原值填写，CTP核心不处理该字段。在撤单回报中，由报单席位号修改为撤单席位号，以方便操作员在撤单回报中看出撤单是从哪个席位发起的</p>
<p>BusinessUnit：是ctp内部使用字段，建议投资者不要使用</p>
<p>TraderID：是席位号</p>
<p>ActiveUserID：是ctp内部使用字段，建议投资者不要使用</p>
<span class="anchor" id="0cdec716-27a7-41e7-9392-614ad8da205a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="19d937f3-5e57-46e3-a791-6e0b1e5cc03b"></span>
## 4.FAQ
<p>无</p>

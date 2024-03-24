<p>成交通知，报单发出后有成交则通过此接口返回。私有流</p>
<span class="anchor" id="601fae5a-8585-4ffa-806a-b1684bdfe03a"></span>
## 1.函数原型
<p>virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {};</p>
<span class="anchor" id="1f501633-338f-44f6-b27d-1dce73fd815a"></span>
## 2.参数
<p>pTrade：成交</p>
<pre><code>struct CThostFtdcTradeField
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
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///成交编号
    TThostFtdcTradeIDType TradeID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///报单编号
    TThostFtdcOrderSysIDType OrderSysID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///交易角色
    TThostFtdcTradingRoleType TradingRole;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///开平标志
    TThostFtdcOffsetFlagType OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///价格
    TThostFtdcPriceType Price;
    ///数量
    TThostFtdcVolumeType Volume;
    ///成交时期
    TThostFtdcDateType TradeDate;
    ///成交时间
    TThostFtdcTimeType TradeTime;
    ///成交类型
    TThostFtdcTradeTypeType TradeType;
    ///成交价来源
    TThostFtdcPriceSourceType PriceSource;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///本地报单编号
    TThostFtdcOrderLocalIDType OrderLocalID;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///序号
    TThostFtdcSequenceNoType SequenceNo;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType BrokerOrderSeq;
    ///成交来源
    TThostFtdcTradeSourceType TradeSource;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<span class="anchor" id="97721d3b-7cea-4819-98c3-50b9235b511d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6aa9218f-acf4-4032-86c9-3c677ff5e910"></span>
## 4.FAQ
<p>无</p>

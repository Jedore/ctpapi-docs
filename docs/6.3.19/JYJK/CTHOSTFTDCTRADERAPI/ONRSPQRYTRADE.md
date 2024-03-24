<p>请求查询成交响应，当执行ReqQryTrade后，该方法被调用。</p>
<span class="anchor" id="fd04bd1e-a4d0-4c59-879c-52ae67428d52"></span>
## 1.函数原型
<p>virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="fde54e95-3a2d-4bb1-a4cc-6cfe2c4ab733"></span>
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
<span class="anchor" id="f1bb0061-bcb1-4164-970e-1285770d731a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f089d86f-90cc-438a-bc9b-ca32810acaf1"></span>
## 4.FAQ
<p>无</p>

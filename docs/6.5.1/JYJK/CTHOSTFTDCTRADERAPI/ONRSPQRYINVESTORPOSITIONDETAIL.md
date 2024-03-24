<p>请求查询投资者持仓明细响应，当执行ReqQryInvestorPositionDetail后，该方法被调用。</p>
<span class="anchor" id="9e70e6ba-483c-45d3-b0e1-8ff4cb919788"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2c1c182a-5d13-4c7e-8242-ba69267fc0e1"></span>
## 2.参数
<p>pInvestorPositionDetail：投资者持仓明细</p>
<pre><code>struct CThostFtdcInvestorPositionDetailField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///买卖
    TThostFtdcDirectionType Direction;
    ///开仓日期
    TThostFtdcDateType  OpenDate;
    ///成交编号
    TThostFtdcTradeIDType   TradeID;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///开仓价
    TThostFtdcPriceType OpenPrice;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///成交类型
    TThostFtdcTradeTypeType TradeType;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve2;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///逐日盯市平仓盈亏
    TThostFtdcMoneyType CloseProfitByDate;
    ///逐笔对冲平仓盈亏
    TThostFtdcMoneyType CloseProfitByTrade;
    ///逐日盯市持仓盈亏
    TThostFtdcMoneyType PositionProfitByDate;
    ///逐笔对冲持仓盈亏
    TThostFtdcMoneyType PositionProfitByTrade;
    ///投资者保证金
    TThostFtdcMoneyType Margin;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
    ///保证金率
    TThostFtdcRatioType MarginRateByMoney;
    ///保证金率(按手数)
    TThostFtdcRatioType MarginRateByVolume;
    ///昨结算价
    TThostFtdcPriceType LastSettlementPrice;
    ///结算价
    TThostFtdcPriceType SettlementPrice;
    ///平仓量
    TThostFtdcVolumeType    CloseVolume;
    ///平仓金额
    TThostFtdcMoneyType CloseAmount;
    ///先开先平剩余数量（DCE）
    TThostFtdcVolumeType    TimeFirstVolume;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///特殊持仓标志
    TThostFtdcSpecPosiTypeType  SpecPosiType;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///组合合约代码
    TThostFtdcInstrumentIDType  CombInstrumentID;
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
<span class="anchor" id="7b20a3ca-43fb-46ef-9f2b-e5b68d0ea43e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="84610281-4b39-420d-b9d1-ac1d0d498c22"></span>
## 4.FAQ
<p>无</p>

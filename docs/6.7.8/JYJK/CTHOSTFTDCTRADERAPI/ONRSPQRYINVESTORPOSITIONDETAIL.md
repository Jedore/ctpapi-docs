<p>请求查询投资者持仓明细响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPOSITIONDETAIL/">ReqQryInvestorPositionDetail</a>后，该方法被调用。</p>
<span class="anchor" id="b3df9106-8d10-4422-8bde-a6d5b63ce96c"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3665ca4a-f4aa-4667-a1c2-e6c1f0785c07"></span>
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
    ///先开先平剩余数量
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
<p>SettlementPrice：该字段日初为昨结算价，仓位变动时，会更新为当时的最新价，不随行情变动。例如某持仓对应的合约最新价为10，持仓手数为2，此时以成交价20平仓了1手，平仓后该多头持仓的SettlementPrice会变更为10。</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>Volume：如果是大商所的持仓则按照先单一后组合的平仓顺序显示平仓后的剩余手数。</p>
<p><span alt="" id="anchor-id-02"></span> </p>
<p>PositionProfitByTrade：大商所开启rule后，大商所的期权会计算持仓盈亏，其他交易所无影响（不计算持仓盈亏）。</p>
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
<span class="anchor" id="81abe723-6166-48f6-8178-6401c4fa5f9e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="67fee1ff-446b-47b6-9727-50f09a1db55b"></span>
## 4.FAQ
<p>无</p>

<p>投资者风险结算持仓查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRISKSETTLEINVSTPOSITION/">ReqQryRiskSettleInvstPosition</a>后，该方法被调用。</p>
<span class="anchor" id="b3c91925-e44d-4c27-8696-3ecbe0d4f217"></span>
## 1.函数原型
<p>virtual void OnRspQryRiskSettleInvstPosition(CThostFtdcRiskSettleInvstPositionField *pRiskSettleInvstPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6fb88ae7-409b-49c0-81b7-eb8b2e4373b1"></span>
## 2.参数
<p>pRiskSettleInvstPosition：投资者风险结算持仓</p>
<pre><code>struct CThostFtdcRiskSettleInvstPositionField
{
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///持仓多空方向
    TThostFtdcPosiDirectionType PosiDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///持仓日期
    TThostFtdcPositionDateType  PositionDate;
    ///上日持仓
    TThostFtdcVolumeType    YdPosition;
    ///今日持仓
    TThostFtdcVolumeType    Position;
    ///多头冻结
    TThostFtdcVolumeType    LongFrozen;
    ///空头冻结
    TThostFtdcVolumeType    ShortFrozen;
    ///开仓冻结金额
    TThostFtdcMoneyType LongFrozenAmount;
    ///开仓冻结金额
    TThostFtdcMoneyType ShortFrozenAmount;
    ///开仓量
    TThostFtdcVolumeType    OpenVolume;
    ///平仓量
    TThostFtdcVolumeType    CloseVolume;
    ///开仓金额
    TThostFtdcMoneyType OpenAmount;
    ///平仓金额
    TThostFtdcMoneyType CloseAmount;
    ///持仓成本
    TThostFtdcMoneyType PositionCost;
    ///上次占用的保证金
    TThostFtdcMoneyType PreMargin;
    ///占用的保证金
    TThostFtdcMoneyType UseMargin;
    ///冻结的保证金
    TThostFtdcMoneyType FrozenMargin;
    ///冻结的资金
    TThostFtdcMoneyType FrozenCash;
    ///冻结的手续费
    TThostFtdcMoneyType FrozenCommission;
    ///资金差额
    TThostFtdcMoneyType CashIn;
    ///手续费
    TThostFtdcMoneyType Commission;
    ///平仓盈亏
    TThostFtdcMoneyType CloseProfit;
    ///持仓盈亏
    TThostFtdcMoneyType PositionProfit;
    ///上次结算价
    TThostFtdcPriceType PreSettlementPrice;
    ///本次结算价
    TThostFtdcPriceType SettlementPrice;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///开仓成本
    TThostFtdcMoneyType OpenCost;
    ///交易所保证金
    TThostFtdcMoneyType ExchangeMargin;
    ///组合成交形成的持仓
    TThostFtdcVolumeType    CombPosition;
    ///组合多头冻结
    TThostFtdcVolumeType    CombLongFrozen;
    ///组合空头冻结
    TThostFtdcVolumeType    CombShortFrozen;
    ///逐日盯市平仓盈亏
    TThostFtdcMoneyType CloseProfitByDate;
    ///逐笔对冲平仓盈亏
    TThostFtdcMoneyType CloseProfitByTrade;
    ///今日持仓
    TThostFtdcVolumeType    TodayPosition;
    ///保证金率
    TThostFtdcRatioType MarginRateByMoney;
    ///保证金率(按手数)
    TThostFtdcRatioType MarginRateByVolume;
    ///执行冻结
    TThostFtdcVolumeType    StrikeFrozen;
    ///执行冻结金额
    TThostFtdcMoneyType StrikeFrozenAmount;
    ///放弃执行冻结
    TThostFtdcVolumeType    AbandonFrozen;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///执行冻结的昨仓
    TThostFtdcVolumeType    YdStrikeFrozen;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///大商所持仓成本差值，只有大商所使用（后台版本6.7.1后该字段废弃）
    TThostFtdcMoneyType PositionCostOffset;
    ///tas持仓手数
    TThostFtdcVolumeType    TasPosition;
    ///tas持仓成本
    TThostFtdcMoneyType TasPositionCost;
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
<span class="anchor" id="0dd332b2-c984-4caa-b105-4b7c7242da1b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="10994302-80c6-4290-81b2-8530b8c1f00c"></span>
## 4.FAQ
<p>无</p>

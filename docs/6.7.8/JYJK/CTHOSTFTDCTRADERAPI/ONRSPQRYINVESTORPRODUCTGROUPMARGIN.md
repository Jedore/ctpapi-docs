<p>请求查询投资者品种/跨品种保证金响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODUCTGROUPMARGIN/">ReqQryInvestorProductGroupMargin</a>后，该方法被调用。</p>
<span class="anchor" id="5585cbf7-89c8-4282-8fcf-7e2853a9b740"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="cd41c66a-c987-45cb-acfe-89d45d92f90d"></span>
## 2.参数
<p>pInvestorProductGroupMargin：投资者品种/跨品种保证金</p>
<pre><code>struct CThostFtdcInvestorProductGroupMarginField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///冻结的保证金
    TThostFtdcMoneyType FrozenMargin;
    ///多头冻结的保证金
    TThostFtdcMoneyType LongFrozenMargin;
    ///空头冻结的保证金
    TThostFtdcMoneyType ShortFrozenMargin;
    ///占用的保证金
    TThostFtdcMoneyType UseMargin;
    ///多头保证金
    TThostFtdcMoneyType LongUseMargin;
    ///空头保证金
    TThostFtdcMoneyType ShortUseMargin;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
    ///交易所多头保证金
    TThostFtdcMoneyType LongExchMargin;
    ///交易所空头保证金
    TThostFtdcMoneyType ShortExchMargin;
    ///平仓盈亏
    TThostFtdcMoneyType CloseProfit;
    ///冻结的手续费
    TThostFtdcMoneyType FrozenCommission;
    ///手续费
    TThostFtdcMoneyType Commission;
    ///冻结的资金
    TThostFtdcMoneyType FrozenCash;
    ///资金差额
    TThostFtdcMoneyType CashIn;
    ///持仓盈亏
    TThostFtdcMoneyType PositionProfit;
    ///折抵总金额
    TThostFtdcMoneyType OffsetAmount;
    ///多头折抵总金额
    TThostFtdcMoneyType LongOffsetAmount;
    ///空头折抵总金额
    TThostFtdcMoneyType ShortOffsetAmount;
    ///交易所折抵总金额
    TThostFtdcMoneyType ExchOffsetAmount;
    ///交易所多头折抵总金额
    TThostFtdcMoneyType LongExchOffsetAmount;
    ///交易所空头折抵总金额
    TThostFtdcMoneyType ShortExchOffsetAmount;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///品种/跨品种标示
    TThostFtdcInstrumentIDType  ProductGroupID;
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
<span class="anchor" id="91b61938-fec0-490e-ac53-27e6504e143a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="894aad75-d3ac-489d-a43d-8539144d37c6"></span>
## 4.FAQ
<p>无</p>

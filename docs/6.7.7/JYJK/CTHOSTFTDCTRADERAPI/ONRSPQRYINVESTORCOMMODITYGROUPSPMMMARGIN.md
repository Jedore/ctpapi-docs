<p>请求投资者商品群SPMM记录查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORCOMMODITYGROUPSPMMMARGIN/">ReqQryInvestorCommodityGroupSPMMMargin</a>后，该方法被调用。</p>
<span class="anchor" id="902c73d5-732c-4e0e-b8a7-f200c8420eef"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorCommodityGroupSPMMMargin(CThostFtdcInvestorCommodityGroupSPMMMarginField *pInvestorCommodityGroupSPMMMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8d54851b-a6bd-4922-8708-caf724c8a276"></span>
## 2.参数
<p>pInvestorCommodityGroupSPMMMargin：投资者商品群SPMM记录</p>
<pre><code>struct CThostFtdcInvestorCommodityGroupSPMMMarginField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///商品群代码
    TThostFtdcSPMMProductIDType CommodityGroupID;
    ///优惠仓位应收保证金
    TThostFtdcMoneyType MarginBeforeDiscount;
    ///不优惠仓位应收保证金
    TThostFtdcMoneyType MarginNoDiscount;
    ///多头风险
    TThostFtdcMoneyType LongRisk;
    ///空头风险
    TThostFtdcMoneyType ShortRisk;
    ///商品群平仓冻结保证金
    TThostFtdcMoneyType CloseFrozenMargin;
    ///SPMM跨品种优惠系数
    TThostFtdcSPMMDiscountRatioType InterCommodityRate;
    ///商品群最小保证金比例
    TThostFtdcSPMMDiscountRatioType MiniMarginRatio;
    ///投资者保证金和交易所保证金的比例
    TThostFtdcRatioType AdjustRatio;
    ///SPMM品种内优惠汇总
    TThostFtdcMoneyType IntraCommodityDiscount;
    ///SPMM跨品种优惠
    TThostFtdcMoneyType InterCommodityDiscount;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
    ///投资者保证金
    TThostFtdcMoneyType InvestorMargin;
    ///冻结的手续费
    TThostFtdcMoneyType FrozenCommission;
    ///手续费
    TThostFtdcMoneyType Commission;
    ///冻结的资金
    TThostFtdcMoneyType FrozenCash;
    ///资金差额
    TThostFtdcMoneyType CashIn;
    ///行权冻结资金
    TThostFtdcMoneyType StrikeFrozenMargin;
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
<span class="anchor" id="a9873a61-3261-458f-ac66-d93b3dec6be3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6eef65d9-3733-4303-b31d-947afe308746"></span>
## 4.FAQ
<p>无</p>

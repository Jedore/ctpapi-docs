<p>请求投资者商品群SPMM记录查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORCOMMODITYGROUPSPMMMARGIN/">ReqQryInvestorCommodityGroupSPMMMargin</a>后，该方法被调用。</p>
<span class="anchor" id="4d9656c5-88c4-4f0e-96ee-1a80c1443bb5"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorCommodityGroupSPMMMargin(CThostFtdcInvestorCommodityGroupSPMMMarginField *pInvestorCommodityGroupSPMMMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="545a1a96-95a4-4565-91bd-17ed56ef220b"></span>
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
<span class="anchor" id="58c097d7-d4f1-4cc9-9f81-752e60036af8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="22007b66-f301-4422-98a9-a34daabed77f"></span>
## 4.FAQ
<p>无</p>

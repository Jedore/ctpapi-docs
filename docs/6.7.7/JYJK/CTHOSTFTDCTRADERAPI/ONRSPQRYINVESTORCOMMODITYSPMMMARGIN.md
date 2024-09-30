<p>请求投资者商品组SPMM记录查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORCOMMODITYSPMMMARGIN/">ReqQryInvestorCommoditySPMMMargin</a>后，该方法被调用。</p>
<span class="anchor" id="302c9ca1-beec-472e-9812-8b6c91522513"></span>
## 1.函数原型
<p>virtual void <a href="../ONRSPQRYINVESTORPRODSPBMDETAIL/">OnRspQryInvestorProdSPBMDetail</a>(CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7893aee9-b506-42d6-81b8-eead6f765312"></span>
## 2.参数
<p>pInvestorProdSPBMDetail：投资者商品组SPMM记录</p>
<pre><code>struct CThostFtdcInvestorCommoditySPMMMarginField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///商品组代码
    TThostFtdcSPMMProductIDType CommodityID;
    ///优惠仓位应收保证金
    TThostFtdcMoneyType MarginBeforeDiscount;
    ///不优惠仓位应收保证金
    TThostFtdcMoneyType MarginNoDiscount;
    ///多头实仓风险
    TThostFtdcMoneyType LongPosRisk;
    ///多头开仓冻结风险
    TThostFtdcMoneyType LongOpenFrozenRisk;
    ///多头被平冻结风险
    TThostFtdcMoneyType LongCloseFrozenRisk;
    ///空头实仓风险
    TThostFtdcMoneyType ShortPosRisk;
    ///空头开仓冻结风险
    TThostFtdcMoneyType ShortOpenFrozenRisk;
    ///空头被平冻结风险
    TThostFtdcMoneyType ShortCloseFrozenRisk;
    ///SPMM品种内跨期优惠系数
    TThostFtdcSPMMDiscountRatioType IntraCommodityRate;
    ///SPMM期权优惠系数
    TThostFtdcSPMMDiscountRatioType OptionDiscountRate;
    ///实仓对冲优惠金额
    TThostFtdcMoneyType PosDiscount;
    ///开仓报单对冲优惠金额
    TThostFtdcMoneyType OpenFrozenDiscount;
    ///品种风险净头
    TThostFtdcMoneyType NetRisk;
    ///平仓冻结保证金
    TThostFtdcMoneyType CloseFrozenMargin;
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
<span class="anchor" id="4b8dfb4d-075f-4c20-8426-1be851b3ca76"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2e66240b-c885-4a30-8c6b-dcb79bd249b8"></span>
## 4.FAQ
<p>无</p>

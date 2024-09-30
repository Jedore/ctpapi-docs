<p>请求投资者品种RCAMS保证金查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODRCAMSMARGIN/">ReqQryInvestorProdRCAMSMargin</a>后，该方法被调用。</p>
<span class="anchor" id="a09b131a-d310-4104-a26d-a8eb3990c752"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProdRCAMSMargin(CThostFtdcInvestorProdRCAMSMarginField *pInvestorProdRCAMSMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a852c678-ae4e-4ca5-8826-873305d0a2ab"></span>
## 2.参数
<p>pInvestorProdRCAMSMargin：投资者品种RCAMS保证金</p>
<pre><code>struct CThostFtdcInvestorProdRCAMSMarginField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///产品组合代码
    TThostFtdcProductIDType CombProductID;
    ///投套标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///商品群代码
    TThostFtdcProductIDType ProductGroupID;
    ///品种组合前风险
    TThostFtdcMoneyType RiskBeforeDiscount;
    ///同合约对冲风险
    TThostFtdcMoneyType IntraInstrRisk;
    ///品种买持仓风险
    TThostFtdcMoneyType BPosRisk;
    ///品种卖持仓风险
    TThostFtdcMoneyType SPosRisk;
    ///品种内对冲风险
    TThostFtdcMoneyType IntraProdRisk;
    ///品种净持仓风险
    TThostFtdcMoneyType NetRisk;
    ///品种间对冲风险
    TThostFtdcMoneyType InterProdRisk;
    ///空头期权风险调整
    TThostFtdcMoneyType ShortOptRiskAdj;
    ///空头期权权利金
    TThostFtdcMoneyType OptionRoyalty;
    ///大边组合平仓冻结保证金
    TThostFtdcMoneyType MMSACloseFrozenMargin;
    ///策略组合平仓/行权冻结保证金
    TThostFtdcMoneyType CloseCombFrozenMargin;
    ///平仓/行权冻结保证金
    TThostFtdcMoneyType CloseFrozenMargin;
    ///大边组合开仓冻结保证金
    TThostFtdcMoneyType MMSAOpenFrozenMargin;
    ///交割月期货开仓冻结保证金
    TThostFtdcMoneyType DeliveryOpenFrozenMargin;
    ///开仓冻结保证金
    TThostFtdcMoneyType OpenFrozenMargin;
    ///投资者冻结保证金
    TThostFtdcMoneyType UseFrozenMargin;
    ///大边组合交易所持仓保证金
    TThostFtdcMoneyType MMSAExchMargin;
    ///交割月期货交易所持仓保证金
    TThostFtdcMoneyType DeliveryExchMargin;
    ///策略组合交易所保证金
    TThostFtdcMoneyType CombExchMargin;
    ///交易所持仓保证金
    TThostFtdcMoneyType ExchMargin;
    ///投资者持仓保证金
    TThostFtdcMoneyType UseMargin;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="b3ffec4b-7a0f-46ed-af7b-ada310c3037c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="589e31d0-9c3b-4ebb-b12a-c4575d6ce9f8"></span>
## 4.FAQ
<p>无</p>

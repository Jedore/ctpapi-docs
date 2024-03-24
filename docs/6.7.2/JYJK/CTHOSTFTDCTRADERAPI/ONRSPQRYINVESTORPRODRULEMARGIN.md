<p>请求投资者产品RULE保证金查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODRULEMARGIN/">ReqQryInvestorProdRULEMargin</a>后，该方法被调用。</p>
<span class="anchor" id="23b98217-3471-4b41-9887-0b46e2a39f34"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProdRULEMargin(CThostFtdcInvestorProdRULEMarginField *pInvestorProdRULEMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e5a6e3fd-60c5-454d-bf85-d986d134598c"></span>
## 2.参数
<p>pInvestorProdRULEMargin：投资者产品RULE保证金</p>
<pre><code>struct CThostFtdcInvestorProdRULEMarginField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///合约类型
    TThostFtdcInstrumentClassType   InstrumentClass;
    ///商品群号
    TThostFtdcCommodityGroupIDType  CommodityGroupID;
    ///买标准持仓
    TThostFtdcStdPositionType   BStdPosition;
    ///卖标准持仓
    TThostFtdcStdPositionType   SStdPosition;
    ///买标准开仓冻结
    TThostFtdcStdPositionType   BStdOpenFrozen;
    ///卖标准开仓冻结
    TThostFtdcStdPositionType   SStdOpenFrozen;
    ///买标准平仓冻结
    TThostFtdcStdPositionType   BStdCloseFrozen;
    ///卖标准平仓冻结
    TThostFtdcStdPositionType   SStdCloseFrozen;
    ///品种内对冲标准持仓
    TThostFtdcStdPositionType   IntraProdStdPosition;
    ///品种内单腿标准持仓
    TThostFtdcStdPositionType   NetStdPosition;
    ///品种间对冲标准持仓
    TThostFtdcStdPositionType   InterProdStdPosition;
    ///单腿标准持仓
    TThostFtdcStdPositionType   SingleStdPosition;
    ///品种内对锁保证金
    TThostFtdcMoneyType IntraProdMargin;
    ///品种间对锁保证金
    TThostFtdcMoneyType InterProdMargin;
    ///跨品种单腿保证金
    TThostFtdcMoneyType SingleMargin;
    ///非组合合约保证金
    TThostFtdcMoneyType NonCombMargin;
    ///附加保证金
    TThostFtdcMoneyType AddOnMargin;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
    ///附加冻结保证金
    TThostFtdcMoneyType AddOnFrozenMargin;
    ///开仓冻结保证金
    TThostFtdcMoneyType OpenFrozenMargin;
    ///平仓冻结保证金
    TThostFtdcMoneyType CloseFrozenMargin;
    ///品种保证金
    TThostFtdcMoneyType Margin;
    ///冻结保证金
    TThostFtdcMoneyType FrozenMargin;
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
<span class="anchor" id="50c65787-45a2-4548-8c39-c3e352991775"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="27e43cf2-6a71-4b6a-85c4-9810638b395b"></span>
## 4.FAQ
<p>无</p>

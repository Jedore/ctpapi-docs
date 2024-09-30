<p>请求投资者产品RULE保证金查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODRULEMARGIN/">ReqQryInvestorProdRULEMargin</a>后，该方法被调用。</p>
<span class="anchor" id="42e2423a-4248-4096-98ef-eadc064c2184"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProdRULEMargin(CThostFtdcInvestorProdRULEMarginField *pInvestorProdRULEMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="aca012e3-5d64-4345-96f9-e8d69f1a9a28"></span>
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
<span class="anchor" id="86dce038-bf79-4014-945e-6ee92f6374b6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c4f76701-b911-4e54-99ed-37c85a7241ed"></span>
## 4.FAQ
<p>无</p>

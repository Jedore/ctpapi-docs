<p>请求投资者产品RULE保证金查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODRULEMARGIN/">ReqQryInvestorProdRULEMargin</a>后，该方法被调用。</p>
<span class="anchor" id="de1e8e85-7930-456f-b2ad-6a437becc57e"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProdRULEMargin(CThostFtdcInvestorProdRULEMarginField *pInvestorProdRULEMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e552e929-d39f-4603-83fc-a929a82d5350"></span>
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
<span class="anchor" id="75837648-6bee-4b5a-bf35-3aedbf2dec54"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2da02fed-4487-4822-9f65-c1ba593ecb42"></span>
## 4.FAQ
<p>无</p>

<p>请求查询经纪公司交易算法响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGALGOS/">ReqQryBrokerTradingAlgos</a>后，该方法被调用</p>
<span class="anchor" id="226a5adb-c9f6-41b5-9d43-18f58a537cbf"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="452e71ba-1420-45fa-b976-5d3e105cf78b"></span>
## 2.参数
<p>pBrokerTradingAlgos：经纪公司交易算法</p>
<pre><code>struct CThostFtdcBrokerTradingAlgosField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///持仓处理算法编号
    TThostFtdcHandlePositionAlgoIDType  HandlePositionAlgoID;
    ///寻找保证金率算法编号
    TThostFtdcFindMarginRateAlgoIDType  FindMarginRateAlgoID;
    ///资金处理算法编号
    TThostFtdcHandleTradingAccountAlgoIDType    HandleTradingAccountAlgoID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>HandlePositionAlgoID：CTP内部使用</p>
<p>FindMarginRateAlgoID：CTP内部使用</p>
<p>HandleTradingAccountAlgoID：CTP内部使用</p>
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
<span class="anchor" id="042592c6-217c-4c24-8890-007af773ea3d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a5dcc325-83f6-4e7f-80f2-7f3199c05393"></span>
## 4.FAQ
<p>无</p>

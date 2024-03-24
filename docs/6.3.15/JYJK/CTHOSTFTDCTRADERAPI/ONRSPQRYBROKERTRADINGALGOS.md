<p>请求查询经纪公司交易算法响应，当执行ReqQryBrokerTradingAlgos后，该方法被调用</p>
<span class="anchor" id="f8b89bf4-8b2b-4c01-b15d-161219338ee2"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2c4ff195-c097-4533-ba45-a90d37b3fbcb"></span>
## 2.参数
<p>pBrokerTradingAlgos：经纪公司交易算法</p>
<pre><code>struct CThostFtdcBrokerTradingAlgosField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///持仓处理算法编号
    TThostFtdcHandlePositionAlgoIDType HandlePositionAlgoID;
    ///寻找保证金率算法编号
    TThostFtdcFindMarginRateAlgoIDType FindMarginRateAlgoID;
    ///资金处理算法编号
    TThostFtdcHandleTradingAccountAlgoIDType HandleTradingAccountAlgoID;
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
<span class="anchor" id="e965dec7-1d24-4e85-b1cc-d873a15db85f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="88addd77-42af-4632-bdfe-e28941256a24"></span>
## 4.FAQ
<p>无</p>

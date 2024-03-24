<p>请求查询经纪公司交易算法响应，当执行ReqQryBrokerTradingAlgos后，该方法被调用</p>
<span class="anchor" id="e3b38937-05b1-471d-ac9e-f16d691b1912"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2f2fc941-7627-4e9f-825e-11643d5261a9"></span>
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
<span class="anchor" id="f0dff827-fd71-4a6e-a5a9-f17693e69ceb"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="12354a50-efae-468a-b168-71cfb898fb67"></span>
## 4.FAQ
<p>无</p>

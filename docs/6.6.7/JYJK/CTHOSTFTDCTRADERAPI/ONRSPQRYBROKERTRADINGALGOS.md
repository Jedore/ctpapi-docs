<p>请求查询经纪公司交易算法响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGALGOS/">ReqQryBrokerTradingAlgos</a>后，该方法被调用</p>
<span class="anchor" id="8727de38-cd6b-424c-a60c-0a98050a8087"></span>
## 1.函数原型
<p>virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6c50971c-2dea-4920-809b-6b2a60f6d927"></span>
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
<span class="anchor" id="29f8237b-88be-489f-b923-7f74617d83bd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ab0c2405-c2cf-433c-995c-5b4e17306281"></span>
## 4.FAQ
<p>无</p>

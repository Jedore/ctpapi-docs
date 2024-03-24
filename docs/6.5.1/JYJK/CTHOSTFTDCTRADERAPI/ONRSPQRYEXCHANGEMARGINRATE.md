<p>请求查询交易所保证金率响应，当执行ReqQryExchangeMarginRate后，该方法被调用。</p>
<span class="anchor" id="4062522d-b553-476f-a8ad-34f80bdf29a7"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="05786272-f428-4ced-9316-1018876d3670"></span>
## 2.参数
<p>pExchangeMarginRate：交易所保证金率</p>
<pre><code>struct CThostFtdcExchangeMarginRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///多头保证金率
    TThostFtdcRatioType LongMarginRatioByMoney;
    ///多头保证金费
    TThostFtdcMoneyType LongMarginRatioByVolume;
    ///空头保证金率
    TThostFtdcRatioType ShortMarginRatioByMoney;
    ///空头保证金费
    TThostFtdcMoneyType ShortMarginRatioByVolume;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="4861ade5-e777-4ec2-8bca-db885a62697b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e73f7829-2300-4df4-970e-85fffcdb3e8b"></span>
## 4.FAQ
<p>无</p>

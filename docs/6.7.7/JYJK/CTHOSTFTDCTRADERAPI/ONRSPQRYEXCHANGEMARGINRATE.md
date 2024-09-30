<p>请求查询交易所保证金率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGEMARGINRATE/">ReqQryExchangeMarginRate</a>后，该方法被调用。</p>
<span class="anchor" id="fc79c004-34fd-41ea-9ad5-c68dce7620ca"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="907cf6ed-720a-4920-8f13-9b2fe9a21f2a"></span>
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
<span class="anchor" id="1bfac80a-f429-4767-bec2-77920e622739"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="02783de1-8b77-4bf6-b472-2a644591a3c5"></span>
## 4.FAQ
<p>无</p>

<p>请求查询合约保证金率响应，当执行ReqQryInstrumentMarginRate后，该方法被调用。</p>
<span class="anchor" id="95b9087e-c2ef-4fef-865e-bcb827aa672a"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="87d69444-2272-4182-90f2-a73bb0f3a348"></span>
## 2.参数
<p>///：合约保证金率</p>
<pre><code>struct CThostFtdcInstrumentMarginRateField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
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
    ///是否相对交易所收取
    TThostFtdcBoolType IsRelative;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="0bc5edf2-a9d4-473e-9b1a-a05d21257aa5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e024519e-c68f-4d58-990b-d2ea303da890"></span>
## 4.FAQ
<p>无</p>

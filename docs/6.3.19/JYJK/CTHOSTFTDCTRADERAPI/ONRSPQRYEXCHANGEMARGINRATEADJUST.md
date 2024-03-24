<p>请求查询交易所调整保证金率响应，当执行ReqQryExchangeMarginRateAdjust后，该方法被调用。</p>
<span class="anchor" id="8ddc46dc-21f5-44a2-a30d-0d869fcd445b"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="54649b26-e06e-4fc7-a343-7d75964c7e95"></span>
## 2.参数
<p>pExchangeMarginRateAdjust：交易所保证金率调整</p>
<pre><code>struct CThostFtdcExchangeMarginRateAdjustField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///跟随交易所投资者多头保证金率
    TThostFtdcRatioType LongMarginRatioByMoney;
    ///跟随交易所投资者多头保证金费
    TThostFtdcMoneyType LongMarginRatioByVolume;
    ///跟随交易所投资者空头保证金率
    TThostFtdcRatioType ShortMarginRatioByMoney;
    ///跟随交易所投资者空头保证金费
    TThostFtdcMoneyType ShortMarginRatioByVolume;
    ///交易所多头保证金率
    TThostFtdcRatioType ExchLongMarginRatioByMoney;
    ///交易所多头保证金费
    TThostFtdcMoneyType ExchLongMarginRatioByVolume;
    ///交易所空头保证金率
    TThostFtdcRatioType ExchShortMarginRatioByMoney;
    ///交易所空头保证金费
    TThostFtdcMoneyType ExchShortMarginRatioByVolume;
    ///不跟随交易所投资者多头保证金率
    TThostFtdcRatioType NoLongMarginRatioByMoney;
    ///不跟随交易所投资者多头保证金费
    TThostFtdcMoneyType NoLongMarginRatioByVolume;
    ///不跟随交易所投资者空头保证金率
    TThostFtdcRatioType NoShortMarginRatioByMoney;
    ///不跟随交易所投资者空头保证金费
    TThostFtdcMoneyType NoShortMarginRatioByVolume;
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
<span class="anchor" id="922c4287-bef5-4ef6-85ee-b11c3e9edef5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0efb0d08-26ee-4c61-befc-533556780b28"></span>
## 4.FAQ
<p>无</p>

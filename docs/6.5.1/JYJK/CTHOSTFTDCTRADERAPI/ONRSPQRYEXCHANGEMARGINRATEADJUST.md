<p>请求查询交易所调整保证金率响应，当执行ReqQryExchangeMarginRateAdjust后，该方法被调用。</p>
<span class="anchor" id="4809dd7f-aa43-4872-9cfa-3c6096ad3679"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6fc0eecd-1e0b-49eb-b6f1-0c5afea5102d"></span>
## 2.参数
<p>pExchangeMarginRateAdjust：交易所保证金率调整</p>
<pre><code>struct CThostFtdcExchangeMarginRateAdjustField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
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
<span class="anchor" id="0f8a4811-ed32-41e1-9748-82089ca14a13"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5bee713d-86b4-4b85-8a98-b36557839414"></span>
## 4.FAQ
<p>无</p>

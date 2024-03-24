<p>询价通知，使用SubscribeForQuoteRsp订阅该询价通知。私有流回报。</p>
<span class="anchor" id="cf4587f8-6f72-4b84-a3f1-0fed7d7d6e19"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="c937f6d2-5a1c-4fff-b55a-8dfa61658407"></span>
## 2.参数
<p>pForQuoteRsp：发给做市商的询价请求</p>
<pre><code>struct CThostFtdcForQuoteRspField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///询价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///询价时间
    TThostFtdcTimeType ForQuoteTime;
    ///业务日期
    TThostFtdcDateType ActionDay;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>ForQuoteSysID：交易所给的一个询价编号，以此定位一笔询价。</p>
<span class="anchor" id="c659923c-f47c-4922-a9c0-729a79a1ea32"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3f4a3bc5-d39d-4dae-bd54-ca3ed4923dc9"></span>
## 4.FAQ
<p>无</p>

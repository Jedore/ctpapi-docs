<p>询价通知，使用SubscribeForQuoteRsp订阅该询价通知。私有流回报。</p>
<span class="anchor" id="edec950b-1dfa-4c9b-af41-48dd3bf73463"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="20c4649c-ad53-41ce-bb53-8374dc1072ef"></span>
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
<span class="anchor" id="8ba5b5c8-f5ba-4b2b-9b97-3f0493909c98"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="185e7cf3-60da-4a56-8255-a6c34d9bc42f"></span>
## 4.FAQ
<p>无</p>

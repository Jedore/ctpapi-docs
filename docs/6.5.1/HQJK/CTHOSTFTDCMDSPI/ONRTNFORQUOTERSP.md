<p>询价通知，使用SubscribeForQuoteRsp订阅该询价通知。私有流回报。</p>
<span class="anchor" id="c01b2804-b99f-43f3-9bcc-3636246ec498"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="fd946706-0601-4939-81da-e4992b56e03f"></span>
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
<span class="anchor" id="07cd3156-a098-4382-bc4f-f177c3e89e20"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1d1d8751-9627-4aaa-ae24-e1d0364bd6c6"></span>
## 4.FAQ
<p>无</p>

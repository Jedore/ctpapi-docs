<p>询价通知，此接口暂时不用，目前使用的是行情的OnRtnForQuoteRsp。</p>
<span class="anchor" id="bda6100e-8c84-4da1-984c-cc23b64cb058"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="6bdeb5ff-637c-4337-93a3-f8696de5e2ed"></span>
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
<span class="anchor" id="3b5e90a1-5aa3-4b17-9e3b-ee721441ee43"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2377d718-04d5-453e-b63b-eedbcc20d4b1"></span>
## 4.FAQ
<p>无</p>

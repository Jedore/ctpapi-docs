<p>询价通知，此接口暂时不用，目前使用的是行情的OnRtnForQuoteRsp。</p>
<span class="anchor" id="33b66318-168f-4067-9932-23ca014f9de4"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="e07efef7-31d5-4057-a65b-339c41072dda"></span>
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
<span class="anchor" id="bc121e43-7005-426d-b8cf-7ffd2e8b2df0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e317bafc-f894-44db-bc6d-18e9e1e6bb9d"></span>
## 4.FAQ
<p>无</p>
